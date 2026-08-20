import numpy as np
import pandas as pd

EPS = 1e-8

def expanding_fill(s):
    med = s.expanding(min_periods=1).median()
    return s.fillna(med).fillna(0.0)

def robust_z(s, window=23):
    s = expanding_fill(s.astype(float))
    med = s.rolling(window, min_periods=3).median()
    mad = (s-med).abs().rolling(window, min_periods=3).median()
    return ((s-med)/(1.4826*mad+EPS)).replace([np.inf,-np.inf], np.nan).fillna(0.0)

def build_dolphin_features(df, edges, feature_columns, horizons=(3,7,23)):
    x_raw = df[feature_columns].astype(float).copy()
    x = pd.DataFrame(index=df.index)
    out = pd.DataFrame(index=df.index)

    for c in feature_columns:
        out[f"{c}__missing"] = x_raw[c].isna().astype(float)
        x[c] = expanding_fill(x_raw[c])
        out[f"{c}__z"] = robust_z(x[c], max(horizons))
        out[f"{c}__dx"] = x[c].diff().fillna(0.0)

    out["missing_fraction"] = out[[f"{c}__missing" for c in feature_columns]].mean(axis=1)

    relation_cols = []
    reconstruction_errors = []

    for _, row in edges.iterrows():
        source = row["source"]
        target = row["target"]
        lag = int(row.get("lag", 1))
        weight = float(row.get("weight", 1.0))
        if source not in feature_columns or target not in feature_columns:
            continue

        src = x[source].shift(lag)
        tgt = x[target]
        rel = tgt - src

        expected = rel.rolling(max(horizons), min_periods=3).median()
        residual = rel - expected
        mad = residual.abs().rolling(max(horizons), min_periods=3).median()

        name = f"relation__{source}__{target}__lag{lag}"
        out[name] = weight * (residual.abs()/(1.4826*mad+EPS)).replace([np.inf,-np.inf], np.nan).fillna(0.0)
        relation_cols.append(name)

        recon = src
        reconstruction_errors.append((tgt-recon).abs())

    if relation_cols:
        out["relational_residual_mean"] = out[relation_cols].mean(axis=1)
        out["relational_residual_max"] = out[relation_cols].max(axis=1)
        out["relational_dispersion"] = out[relation_cols].std(axis=1).fillna(0.0)
    else:
        out["relational_residual_mean"] = 0.0
        out["relational_residual_max"] = 0.0
        out["relational_dispersion"] = 0.0

    if reconstruction_errors:
        recon_mat = pd.concat(reconstruction_errors, axis=1)
        out["reconstruction_error"] = recon_mat.mean(axis=1).fillna(0.0)
    else:
        out["reconstruction_error"] = 0.0

    out["latent_velocity"] = out["relational_residual_mean"].diff().fillna(0.0)
    out["latent_acceleration"] = out["latent_velocity"].diff().fillna(0.0)

    for h in horizons:
        out[f"residual_mean_{h}"] = out["relational_residual_mean"].rolling(h, min_periods=1).mean()
        out[f"reconstruction_mean_{h}"] = out["reconstruction_error"].rolling(h, min_periods=1).mean()
        out[f"missing_mean_{h}"] = out["missing_fraction"].rolling(h, min_periods=1).mean()
        out[f"velocity_mean_{h}"] = out["latent_velocity"].rolling(h, min_periods=1).mean()

    components = [
        out["relational_residual_mean"],
        out["relational_residual_max"],
        out["relational_dispersion"],
        out["reconstruction_error"],
        out["missing_fraction"],
        out["latent_velocity"].clip(lower=0),
        out["latent_acceleration"].clip(lower=0),
    ]

    for h in horizons:
        components.extend([
            out[f"residual_mean_{h}"],
            out[f"reconstruction_mean_{h}"],
            out[f"missing_mean_{h}"],
            out[f"velocity_mean_{h}"].clip(lower=0),
        ])

    ranked = pd.concat(components, axis=1).rank(pct=True)
    out["dolphin_latent_score"] = ranked.mean(axis=1).fillna(0.0)

    return out.replace([np.inf,-np.inf], np.nan).fillna(0.0)

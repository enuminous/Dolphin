from dataclasses import dataclass
import pandas as pd

from features import build_dolphin_features
from baselines import LogisticModel, BaseRateModel, local_forward_fill, neighbor_average
from metrics import binary_metrics, stratify_missingness

@dataclass
class DOLPHINExperiment:
    time_column: str
    target_column: str
    feature_columns: list
    horizons: tuple = (3,7,23)
    train_fraction: float = 0.65
    random_state: int = 23

    def run(self, df, edges):
        df = df.sort_values(self.time_column).reset_index(drop=True).copy()
        cut = max(20, int(len(df)*self.train_fraction))
        y = df[self.target_column].astype(int).to_numpy()

        df_feat = build_dolphin_features(df, edges, self.feature_columns, self.horizons)
        local = local_forward_fill(df, self.feature_columns)
        neighbor = pd.concat([local, neighbor_average(df, edges, self.feature_columns)], axis=1).fillna(0.0)
        full = pd.concat([local, df_feat], axis=1).fillna(0.0)

        models = {
            "dolphin": (LogisticModel(self.random_state), full),
            "local_only": (LogisticModel(self.random_state), local),
            "neighbor_reconstruction": (LogisticModel(self.random_state), neighbor),
            "base_rate": (BaseRateModel(), local),
        }

        results = {}
        for name, (model, X) in models.items():
            model.fit(X.iloc[:cut], y[:cut])
            p = model.predict_proba(X.iloc[cut:])
            results[name] = {
                "overall": binary_metrics(y[cut:], p),
                "by_missingness": stratify_missingness(
                    y[cut:], p, df_feat["missing_fraction"].to_numpy()[cut:]
                )
            }

        return {
            "n_total": len(df),
            "train_n": cut,
            "test_n": len(df)-cut,
            "results": results,
            "primary_delta_brier_local_minus_dolphin": (
                results["local_only"]["overall"]["brier"]
                - results["dolphin"]["overall"]["brier"]
            ),
            "interpretation": (
                "Positive delta favors DOLPHIN over the matched local-only model. "
                "Inspect whether any gain grows with missingness."
            )
        }

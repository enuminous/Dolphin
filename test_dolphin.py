import pandas as pd
from features import build_dolphin_features
from dolphin import DOLPHINExperiment

FEATURES = ["obs_a","obs_b","obs_c","obs_d"]

def test_features():
    data = pd.read_csv("example_data.csv")
    edges = pd.read_csv("example_edges.csv")
    df = build_dolphin_features(data, edges, FEATURES)
    assert len(df) == len(data)
    assert "dolphin_latent_score" in df.columns
    assert df["dolphin_latent_score"].between(0,1).all()

def test_experiment_runs():
    data = pd.read_csv("example_data.csv")
    edges = pd.read_csv("example_edges.csv")
    exp = DOLPHINExperiment(
        time_column="time",
        target_column="latent_event",
        feature_columns=FEATURES,
    )
    out = exp.run(data, edges)
    assert "results" in out
    assert "dolphin" in out["results"]
    assert "local_only" in out["results"]

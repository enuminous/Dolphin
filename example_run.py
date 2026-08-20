import json
import pandas as pd
from dolphin import DOLPHINExperiment

data = pd.read_csv("example_data.csv")
edges = pd.read_csv("example_edges.csv")

exp = DOLPHINExperiment(
    time_column="time",
    target_column="latent_event",
    feature_columns=["obs_a","obs_b","obs_c","obs_d"],
    horizons=(3,7,23),
    random_state=23,
)

result = exp.run(data, edges)
print(json.dumps(result, indent=2))

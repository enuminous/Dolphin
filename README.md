# DOLPHIN

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Dolphin) · This repository is linked through its source; GitHub Pages is not enabled.

<details>
<summary>Recent repositories (9)</summary>

- [Oroboros](https://github.com/enuminous/Oroboros) · [README](https://github.com/enuminous/Oroboros/blob/main/README.md) · [Page](https://enuminous.github.io/Oroboros/)
- [P-NP](https://github.com/enuminous/P-NP) · [README](https://github.com/enuminous/P-NP/blob/main/README.md) · [Page](https://enuminous.github.io/P-NP/)
- [Research-Program](https://github.com/enuminous/Research-Program) · [README](https://github.com/enuminous/Research-Program/blob/main/README.md) · [Page](https://enuminous.github.io/Research-Program/)
- [I-Have-Guts](https://github.com/enuminous/I-Have-Guts) · [README](https://github.com/enuminous/I-Have-Guts/blob/main/README.md) · [Page](https://enuminous.github.io/I-Have-Guts/)
- [Wrights-Law](https://github.com/enuminous/Wrights-Law) · [README](https://github.com/enuminous/Wrights-Law/blob/main/README.md) · [Page](https://enuminous.github.io/Wrights-Law/)
- [Aristotle-eNuminous](https://github.com/enuminous/Aristotle-eNuminous) · [README](https://github.com/enuminous/Aristotle-eNuminous/blob/main/README.md) · [Page](https://enuminous.github.io/Aristotle-eNuminous/)
- [Multiverse-Simulator](https://github.com/enuminous/Multiverse-Simulator) · [README](https://github.com/enuminous/Multiverse-Simulator/blob/main/README.md) · [Page](https://enuminous.github.io/Multiverse-Simulator/)
- [accelerando-8192](https://github.com/enuminous/accelerando-8192) · [README](https://github.com/enuminous/accelerando-8192/blob/main/README.md) · [Page source](https://github.com/enuminous/accelerando-8192/blob/main/docs/index.html)
- [Codex-888](https://github.com/enuminous/Codex-888) · [README](https://github.com/enuminous/Codex-888/blob/main/README.md) · [Page](https://enuminous.github.io/Codex-888/)

</details>
<!-- ENUMINOUS-NETWORK:END -->

**Dynamic Observation of Latent Patterns through Historical Interaction Networks**

DOLPHIN is an EFMW-derived framework for partially observed systems.

Its narrow question is:

> Can hidden or latent system state be inferred from the historical interactions among the variables we can observe?

## Intended uses

- partially observed machinery
- multi-agent systems
- sensor networks
- logistics
- organizational dynamics
- network operations
- robotics
- ecological systems
- latent-demand systems
- systems with missing or indirect state

## Core signal path

```text
observable state
→ missingness map
→ lagged interactions
→ relational residuals
→ neighborhood reconstruction
→ latent-state proxy
→ multiscale persistence
→ DOLPHIN latent-state score
```

## Flat-stack repository

```text
README.md
LICENSE
CITATION.cff
pyproject.toml
requirements.txt
dolphin.py
features.py
baselines.py
metrics.py
freeze.py
latent_schema.json
example_config.yaml
example_data.csv
example_edges.csv
example_run.py
test_dolphin.py
MANIFEST.sha256
```

## Scientific hypothesis

> In partially observed systems, latent state may be recoverable from the changing relationships among observable components even when direct measurements are missing or incomplete.

DOLPHIN does not assume this is true.

## Example signals

- missingness fraction
- lagged relational residual
- neighbor disagreement
- reconstruction error
- interaction persistence
- distributed latent proxy
- hidden-state probability

## Baselines

Included:

- local-only logistic model
- forward-fill local model
- neighbor-average reconstruction model
- base-rate predictor

## Primary endpoint

> Does DOLPHIN improve out-of-sample prediction of a hidden/future state over matched local-only models?

Primary metric:

- Brier score

Secondary metrics:

- log loss
- ROC-AUC
- average precision
- performance by missingness regime
- reconstruction error

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python example_run.py
```

## Tests

```bash
pytest -q
```

## Minimal use

```python
import pandas as pd
from dolphin import DOLPHINExperiment

data = pd.read_csv("example_data.csv")
edges = pd.read_csv("example_edges.csv")

exp = DOLPHINExperiment(
    time_column="time",
    target_column="latent_event",
    feature_columns=["obs_a","obs_b","obs_c","obs_d"],
    horizons=(3,7,23),
)

print(exp.run(data, edges))
```

## Freeze discipline

Freeze before prospective use:

- observable variables
- missingness rules
- edge list
- allowed lags
- reconstruction rule
- latent proxy equations
- horizons
- target
- split
- baselines
- metrics
- seeds
- exclusions

Then run:

```bash
python freeze.py
```

## Negative results

If local-only or simple neighbor reconstruction matches DOLPHIN, then the explicit latent-interaction formulation has not demonstrated incremental value.

## Status

Research software. Experimental. Not validated for safety-critical decisions.

# DOLPHIN

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Dolphin) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#zoo-index-and-agents)

<details open>
<summary><strong>On this page</strong></summary>

- [Intended uses](#intended-uses)
- [Core signal path](#core-signal-path)
- [Flat-stack repository](#flat-stack-repository)
- [Scientific hypothesis](#scientific-hypothesis)
- [Example signals](#example-signals)
- [Baselines](#baselines)
- [Primary endpoint](#primary-endpoint)
- [Installation](#installation)
- [Run](#run)
- [Tests](#tests)
- [Minimal use](#minimal-use)
- [Freeze discipline](#freeze-discipline)
- [Negative results](#negative-results)
- [Status](#status)


</details>

**Related repositories:** [Tortoise](https://github.com/enuminous/Tortoise) · [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Ant](https://github.com/enuminous/Ant) · [Raven](https://github.com/enuminous/Raven) · [Moth](https://github.com/enuminous/Moth) · [Spider](https://github.com/enuminous/Spider)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


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

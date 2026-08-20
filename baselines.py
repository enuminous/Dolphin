import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import RobustScaler

class LogisticModel:
    def __init__(self, random_state=23):
        self.scaler = RobustScaler()
        self.model = LogisticRegression(max_iter=4000, random_state=random_state)
        self.constant_ = None

    def fit(self, X, y):
        y = np.asarray(y, dtype=int)
        if len(np.unique(y)) < 2:
            self.constant_ = float(y.mean()) if len(y) else 0.0
            return self
        self.scaler.fit(X)
        self.model.fit(self.scaler.transform(X), y)
        return self

    def predict_proba(self, X):
        if self.constant_ is not None:
            return np.full(len(X), self.constant_)
        return self.model.predict_proba(self.scaler.transform(X))[:,1]

class BaseRateModel:
    def fit(self, X, y):
        self.p_ = float(np.mean(y))
        return self
    def predict_proba(self, X):
        return np.full(len(X), self.p_, dtype=float)

def local_forward_fill(df, feature_columns):
    x = df[feature_columns].astype(float).copy()
    miss = x.isna().astype(float)
    x = x.ffill().fillna(0.0)
    miss.columns = [f"{c}__missing" for c in miss.columns]
    return pd.concat([x, miss], axis=1)

def neighbor_average(df, edges, feature_columns):
    x = df[feature_columns].astype(float).ffill().fillna(0.0)
    out = pd.DataFrame(index=df.index)
    for target in feature_columns:
        incoming = edges.loc[edges["target"] == target, "source"].tolist()
        incoming = [c for c in incoming if c in feature_columns]
        if incoming:
            out[f"{target}__neighbor_mean"] = x[incoming].mean(axis=1)
        else:
            out[f"{target}__neighbor_mean"] = 0.0
    return out.fillna(0.0)

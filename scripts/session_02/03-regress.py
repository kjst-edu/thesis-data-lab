# scripts/session_02/03-regress.py
#
# data/pwt_2023.csv を読み込み、欠損値を処理して分析用の変数を作り、
# 単回帰を実行する:
#
#   log(GDP per worker) = α + β * log(capital per worker) + ε
#
# 実行方法:
#   uv run scripts/session_02/03-regress.py
#
# 前提:
#   - 01-prepare_pwt_2023.py を先に実行して data/pwt_2023.csv があること

from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

INPUT_DATA = Path("data/pwt_2023.csv")

df = pd.read_csv(INPUT_DATA)
df = df.dropna(subset=["rgdpna", "emp", "rnna"]).copy()
df["gdp_per_worker"] = df["rgdpna"] / df["emp"]
df["capital_per_worker"] = df["rnna"] / df["emp"]

model = smf.ols(
    "np.log(gdp_per_worker) ~ np.log(capital_per_worker)",
    data=df,
).fit()

print(model.summary())

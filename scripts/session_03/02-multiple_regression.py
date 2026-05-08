# scripts/session_03/02-multiple_regression.py
#
# data/pwt_2023_oecd.csv を読み込み、重回帰・ダミー変数・交差項・
# 対数変換の解釈を順に確認する。
#
# 配布版 (scripts/session_03/) は `____` の穴埋め。
# 答えは notes/sessions/session-03.qmd か、完成版の demo/scripts/session_03/ にある。
# `____` を埋めずに実行すると AttributeError などが出る。
#
# 実行方法:
#   - VS Code: Python 拡張 (ms-python.python) が入っていれば、`# %%` で
#     区切られた各セルの上に「Run Cell」が表示され、Shift+Enter でも実行できる。
#     初回はカーネル選択を求められるので、このリポジトリの uv 環境を選ぶ。
#   - 全体を一括実行: uv run scripts/session_03/02-multiple_regression.py
#
# 前提:
#   - 01-prepare_pwt_2023_oecd.py を先に実行して
#     data/pwt_2023_oecd.csv が作られていること

# %%
from pathlib import Path

import numpy as np
import pandas as pd
import _____ as smf

INPUT_DATA = Path("data/pwt_2023_oecd.csv")

df = pd.read_csv(INPUT_DATA)
df = df.dropna(subset=["rgdpna", "emp", "rnna", "hc"]).copy()
df["gdp_per_worker"] = df["rgdpna"] / df["emp"]
df["capital_per_worker"] = df["rnna"] / df["emp"]

print("サンプル数:", len(df))
print("OECD 国数 :", int(df["is_oecd"].sum()))
df.head()

# %% [1] 単回帰の復習
# log(y/L) = α + β log(K/L) + ε

# 1. モデルを定義する
model1 = smf.____(
    "______ ~ ______",
    data=df,
)

# 2. 推定する
m1 = model1.____()

# 3. 結果を見る
print(m1.____())

# %% [2] 重回帰: 人的資本を加える
# log(y/L) = α + β1 log(K/L) + β2 log(hc) + ε

model2 = smf.____(
    "______ ~ ______ + ______",
    data=df,
)
m2 = model2.____()
print(m2.____())

# %%
print(f"単回帰  β(log K/L) = {m1.params['np.log(capital_per_worker)']:.3f}")
print(f"重回帰  β(log K/L) = {m2.params['np.log(capital_per_worker)']:.3f}")
print(f"重回帰  β(log hc)  = {m2.params['np.log(hc)']:.3f}")

# %% [3] ダミー変数: OECD 加盟国かどうか
# log(y/L) = α + β1 log(K/L) + β2 log(hc) + γ × is_oecd + ε

model3 = smf.____(
    "______ ~ ______ + ______ + ______",
    data=df,
)
m3 = model3.____()
print(m3.____())

# %% [4] 交差項: グループで効果は違うか
# log(y/L) = α + β1 log(K/L) + β2 log(hc) + γ is_oecd + δ (log(K/L) × is_oecd) + ε

model4 = smf.____(
    "______ ~ ______ _ ______ + ______",
    data=df,
)
m4 = model4.____()
print(m4.____())

# %%
beta_non = m4.params["______"]
delta = m4.params["______"]
print(f"非 OECD での資本弾力性 : {beta_non:.3f}")
print(f"OECD での資本弾力性    : {beta_non + delta:.3f}")
print(f"差 (交差項の係数)       : {delta:.3f}")

# %% [5] モデル比較

summary = pd.DataFrame({
    "model":    ["単回帰", "重回帰", "+ ダミー", "+ 交差項"],
    "n":        [int(m.nobs) for m in (m1, m2, m3, m4)],
    "R^2":      [m.rsquared for m in (m1, m2, m3, m4)],
    "Adj.R^2":  [m.____ for m in (m1, m2, m3, m4)],
}).round(3)
print(summary.to_string(index=False))

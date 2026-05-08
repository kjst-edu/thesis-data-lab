# scripts/session_02/02-describe_and_plot.py
#
# data/pwt_2023.csv を読み込み、欠損値を確認・処理して分析用の変数を作り、
# 記述統計量と図を表示・保存する。
#
# 実行方法:
#   uv run scripts/session_02/02-describe_and_plot.py
#
# 前提:
#   - 01-prepare_pwt_2023.py を先に実行して data/pwt_2023.csv があること

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

INPUT_DATA = Path("data/pwt_2023.csv")
FIG_DIR = Path("output/figures")
FIG_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_DATA)

# 欠損値の確認
print("欠損値の件数:")
print(df.isna().sum())

# 分析に必要な変数の欠損行を落とし、労働者あたり指標を計算する
df = df.dropna(subset=["rgdpna", "emp", "rnna", "hc"]).copy()
df["gdp_per_worker"] = df["rgdpna"] / df["emp"]
df["capital_per_worker"] = df["rnna"] / df["emp"]

print()
print("分析サンプルの記述統計量:")
print(df[["gdp_per_worker", "capital_per_worker", "hc"]].describe().round(2))

# ヒストグラム（対数軸）
fig, ax = plt.subplots(figsize=(6, 4))
sns.histplot(data=df, x="gdp_per_worker", bins=20, log_scale=True, ax=ax)
ax.set_title("GDP per worker, 2023 (log scale)")
fig.tight_layout()
fig.savefig(FIG_DIR / "session_02_hist_log_gdp.png", dpi=150)
plt.close(fig)

# 散布図 + 回帰直線（log-log）
fig, ax = plt.subplots(figsize=(6, 4))
sns.regplot(
    x=np.log(df["capital_per_worker"]),
    y=np.log(df["gdp_per_worker"]),
    ax=ax,
    line_kws={"color": "red"},
    scatter_kws={"alpha": 0.6},
)
ax.set_xlabel("log(capital per worker)")
ax.set_ylabel("log(GDP per worker)")
ax.set_title("Capital per worker vs GDP per worker, 2023 (log-log)")
fig.tight_layout()
fig.savefig(FIG_DIR / "session_02_scatter_k_y.png", dpi=150)
plt.close(fig)

print()
print("Saved figures to", FIG_DIR)

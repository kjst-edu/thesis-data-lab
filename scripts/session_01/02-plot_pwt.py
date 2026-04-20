# data/pwt_gdp_per_capita.csv を読み込み、
# 国別の一人あたり実質 GDP の推移を折れ線グラフにして
# output/pwt_gdp_per_capita.png として保存する。
#
# 実行方法:
#   uv run scripts/session_01/02-plot_pwt.py
#
# 前提:
#   - 01-prepare_pwt.py を先に実行して data/ にファイルがあること

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

INPUT_DATA = Path("data/pwt_gdp_per_capita.csv")
OUTPUT_FIGURE = Path("output/pwt_gdp_per_capita.png")

df = pd.read_csv(INPUT_DATA)

OUTPUT_FIGURE.parent.mkdir(exist_ok=True)

fig, ax = plt.subplots()
for code, group in df.groupby("countrycode"):
    group.plot(x="year", y="gdp_per_capita", ax=ax, label=code)
ax.set_title("Real GDP per capita")
ax.set_ylabel("Million 2017 USD per person")
ax.legend()
plt.tight_layout()
plt.savefig(OUTPUT_FIGURE, dpi=150)
plt.close()

print("Saved:", OUTPUT_FIGURE)

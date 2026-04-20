# Penn World Table (PWT 11.0) から一人あたり実質 GDP を計算し、
# data/pwt_gdp_per_capita.csv として保存する。
#
# 実行方法:
#   uv run scripts/session_01/01-prepare_pwt.py
#
# 前提:
#   - .env に RAW_DATA_DIR が設定されていること
#   - RAW_DATA_DIR に pwt110.dta が置かれていること

from pathlib import Path
import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

RAW_DATA_DIR = Path(os.environ["RAW_DATA_DIR"])

COUNTRIES = ["JPN", "USA", "KOR", "CHN"]
YEAR_START = 1990

OUTPUT_DATA = Path("data/pwt_gdp_per_capita.csv")

# データ読み込み
df = pd.read_stata(RAW_DATA_DIR / "pwt110.dta")

# 国・期間を絞り込み、一人あたり実質 GDP を計算
subset = df[df["countrycode"].isin(COUNTRIES) & (df["year"] >= YEAR_START)].copy()
subset["gdp_per_capita"] = subset["rgdpna"] / subset["pop"]

result = subset[["countrycode", "country", "year", "gdp_per_capita"]]

OUTPUT_DATA.parent.mkdir(exist_ok=True)
result.to_csv(OUTPUT_DATA, index=False)

print("Saved:", OUTPUT_DATA)
print()
print(result.head(10).to_string(index=False))

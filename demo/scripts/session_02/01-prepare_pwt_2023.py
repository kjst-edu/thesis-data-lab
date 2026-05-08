# scripts/session_02/01-prepare_pwt_2023.py
#
# Penn World Table (PWT 11.0) から 2023 年のクロスセクションを抽出し、
# data/pwt_2023.csv として保存する。欠損値の処理や派生変数の作成は
# 行わず、後段の分析スクリプトに任せる。
#
# 実行方法:
#   uv run scripts/session_02/01-prepare_pwt_2023.py
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

YEAR = 2023
OUTPUT_DATA = Path("data/pwt_2023.csv")

USE_COLS = [
    "countrycode", "country", "year",
    "rgdpna", "pop", "emp", "avh",
    "rnna", "hc", "labsh",
]

raw = pd.read_stata(RAW_DATA_DIR / "pwt110.dta", columns=USE_COLS)
df = raw[raw["year"] == YEAR].copy()

OUTPUT_DATA.parent.mkdir(exist_ok=True)
df.to_csv(OUTPUT_DATA, index=False)

print("Saved:", OUTPUT_DATA)
print("Shape:", df.shape)
print()
print("欠損値の件数:")
print(df.isna().sum())

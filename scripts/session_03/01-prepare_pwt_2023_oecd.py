# scripts/session_03/01-prepare_pwt_2023_oecd.py
#
# Penn World Table (PWT 11.0) から 2023 年のクロスセクションを抽出し、
# OECD 加盟国ダミー is_oecd を付けて data/pwt_2023_oecd.csv に保存する。
# 欠損処理や派生変数の作成は後段の分析スクリプトに任せる。
#
# 実行方法:
#   uv run scripts/session_03/01-prepare_pwt_2023_oecd.py
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
OUTPUT_DATA = Path("data/pwt_2023_oecd.csv")

USE_COLS = [
    "countrycode", "country", "year",
    "rgdpna", "pop", "emp", "avh",
    "rnna", "hc", "labsh",
]

# OECD 加盟 38 か国 (2024 年時点)
# 出所: https://www.oecd.org/about/document/ratification-oecd-convention.htm
OECD_ISO3 = {
    "AUS", "AUT", "BEL", "CAN", "CHL", "COL", "CRI", "CZE",
    "DNK", "EST", "FIN", "FRA", "DEU", "GRC", "HUN", "ISL",
    "IRL", "ISR", "ITA", "JPN", "KOR", "LVA", "LTU", "LUX",
    "MEX", "NLD", "NZL", "NOR", "POL", "PRT", "SVK", "SVN",
    "ESP", "SWE", "CHE", "TUR", "GBR", "USA",
}

raw = pd.read_stata(RAW_DATA_DIR / "pwt110.dta", columns=USE_COLS)
df = raw[raw["year"] == YEAR].copy()
df["is_oecd"] = df["countrycode"].isin(OECD_ISO3).astype(int)

OUTPUT_DATA.parent.mkdir(exist_ok=True)
df.to_csv(OUTPUT_DATA, index=False)

print("Saved:", OUTPUT_DATA)
print("Shape:", df.shape)
print("OECD 加盟国数 (サンプル中):", int(df["is_oecd"].sum()))
print()
print("欠損値の件数:")
print(df.isna().sum())

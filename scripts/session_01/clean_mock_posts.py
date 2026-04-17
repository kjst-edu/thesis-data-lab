from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


INPUT_PATH = Path("assets/session_01/mock_x_posts.csv")
OUTPUT_DATA_PATH = Path("data/processed/session_01_posts_cleaned.csv")
OUTPUT_SUMMARY_PATH = Path("output/session_01_posts_by_day.csv")
OUTPUT_FIGURE_PATH = Path("output/session_01_posts_by_day.png")


def load_data() -> pd.DataFrame:
    return pd.read_csv(INPUT_PATH)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned["posted_at"] = pd.to_datetime(cleaned["posted_at"])
    cleaned["likes"] = cleaned["likes"].fillna(0).astype(int)
    cleaned["text"] = cleaned["text"].str.strip()
    cleaned["date"] = cleaned["posted_at"].dt.date.astype(str)
    cleaned["text_length"] = cleaned["text"].str.len()
    cleaned["mentions_python"] = cleaned["text"].str.contains("Python", case=False)
    return cleaned


def make_daily_summary(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("date", as_index=False)
        .agg(posts=("post_id", "count"), avg_likes=("likes", "mean"))
        .sort_values("date")
    )


def save_outputs(cleaned: pd.DataFrame, summary: pd.DataFrame) -> None:
    OUTPUT_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)

    cleaned.to_csv(OUTPUT_DATA_PATH, index=False)
    summary.to_csv(OUTPUT_SUMMARY_PATH, index=False)

    ax = summary.plot.bar(x="date", y="posts", legend=False, title="Posts per day")
    ax.set_xlabel("date")
    ax.set_ylabel("posts")
    plt.savefig(OUTPUT_FIGURE_PATH, dpi=150, bbox_inches="tight")
    plt.close()


def main() -> None:
    raw_df = load_data()
    cleaned_df = clean_data(raw_df)
    summary_df = make_daily_summary(cleaned_df)
    save_outputs(cleaned_df, summary_df)

    print("Input:", INPUT_PATH)
    print("Cleaned data saved to:", OUTPUT_DATA_PATH)
    print("Daily summary saved to:", OUTPUT_SUMMARY_PATH)
    print("Figure saved to:", OUTPUT_FIGURE_PATH)
    print()
    print("Preview of cleaned data")
    print(cleaned_df.head())
    print()
    print("Daily summary")
    print(summary_df)


if __name__ == "__main__":
    main()

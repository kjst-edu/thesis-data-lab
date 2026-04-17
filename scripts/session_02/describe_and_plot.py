from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def make_example_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "study_hours": [1, 2, 3, 4, 5, 6],
            "score": [52, 55, 61, 68, 72, 78],
        }
    )


def main() -> None:
    figures_dir = Path("output/figures")
    figures_dir.mkdir(parents=True, exist_ok=True)

    df = make_example_data()

    print("記述統計量")
    print(df.describe())

    ax = df.plot.scatter(x="study_hours", y="score", title="学習時間と得点")
    ax.set_xlabel("study_hours")
    ax.set_ylabel("score")

    output_path = figures_dir / "session_02_scatter.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()

    print()
    print(f"散布図を保存しました: {output_path}")


if __name__ == "__main__":
    main()

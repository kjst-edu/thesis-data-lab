from pathlib import Path


def main() -> None:
    processed_data_dir = Path("data/processed")
    metadata_dir = Path("data/metadata")
    figures_dir = Path("output/figures")

    figures_dir.mkdir(parents=True, exist_ok=True)

    print("教材リポジトリの基本パス")
    print(f"- processed data: {processed_data_dir}")
    print(f"- metadata: {metadata_dir}")
    print(f"- figures: {figures_dir}")
    print()
    print("このスクリプトは、repo のルートで実行する前提の最小例です。")


if __name__ == "__main__":
    main()

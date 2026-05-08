# demo

`thesis-data-lab` の動作確認用ディレクトリ。各 session の **完成版スクリプト** を置き、ここで実行確認をする。

ディレクトリ構成は [thesis-starter](https://github.com/kjst-edu/thesis-starter) を踏襲（`thesis.docx` などは省略）。学生が自分の卒論プロジェクトを `thesis-starter` テンプレートから作ったときと同じ階層になる。

## ルートの .venv を共有する

このディレクトリには `pyproject.toml` を置かない。`uv run ...` を実行すると、uv は親ディレクトリの `pyproject.toml` を探しに行くので、`thesis-data-lab/.venv` がそのまま使われる。

```bash
cd demo
uv run scripts/session_03/01-prepare_pwt_2023_oecd.py
uv run scripts/session_03/02-multiple_regression.py
```

## .env

生データの保存先は `.env` の `RAW_DATA_DIR` で指定する。`.env` は commit しない。

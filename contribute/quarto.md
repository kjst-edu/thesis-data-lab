# Quarto メモ

このファイルは、講義ノート (`notes/`) を書くときに参照するための Quarto の記法メモです。

---

## コールアウト

参照: <https://quarto.org/docs/authoring/callouts.html>

### 種類

| タイプ | 用途の目安 |
|--------|-----------|
| `note` | 補足情報 |
| `tip` | おすすめの方法・ヒント |
| `important` | 見落とさないでほしい重要事項 |
| `warning` | 注意・よくあるミス |
| `caution` | 操作前に確認してほしいこと |

: コールアウトの種類 {#tbl-callout-types}

### 基本的な書き方

```markdown
::: {.callout-note}
本文テキスト
:::

::: {.callout-tip}
## タイトルを見出しで指定する方法
本文テキスト
:::

::: {.callout-warning title="タイトルを属性で指定する方法"}
本文テキスト
:::
```

### オプション

#### collapse（折りたたみ）

```markdown
::: {.callout-note collapse="true"}
デフォルトで折りたたまれた状態になります。
:::
```

- `collapse="true"` → デフォルトで折りたたみ
- `collapse="false"` → デフォルトで展開

#### appearance（外観）

```markdown
::: {.callout-note appearance="simple"}
本文テキスト
:::
```

| 値 | 見た目 |
|----|--------|
| `default` | カラーヘッダー＋アイコン（デフォルト） |
| `simple` | 軽量デザイン |
| `minimal` | ボーダーのみ |

: appearance オプションの値 {#tbl-callout-appearance}

#### icon（アイコン非表示）

```markdown
::: {.callout-note icon=false}
アイコンなしで表示されます。
:::
```

ドキュメント全体で非表示にする場合は YAML フロントマターに記載:

```yaml
callout-icon: false
```

### 相互参照

ID を付けると本文中から参照できます。プレフィックスはタイプごとに決まっています。

| タイプ | ID プレフィックス |
|--------|----------------|
| `note` | `#nte-` |
| `tip` | `#tip-` |
| `warning` | `#wrn-` |
| `important` | `#imp-` |
| `caution` | `#cau-` |

: コールアウト相互参照のプレフィックス {#tbl-callout-xref}

```markdown
::: {#tip-example .callout-tip}
## タイトル
本文テキスト
:::

詳細は @tip-example を参照してください。
```

### 対応フォーマット

HTML, PDF, Typst, DOCX, EPUB, Revealjs

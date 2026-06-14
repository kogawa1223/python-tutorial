# Python Tutorial

Python 公式チュートリアル（[The Python Tutorial](https://docs.python.org/3/tutorial/)）を章ごとに実装した学習リポジトリ。**コードを書く全章を実装済み**。

各章は「公式の節立てに沿った関数 + `assert` による自己検証 + ラベル付き出力」で構成し、**読むだけで何を学んだかが分かる**ことを意図している。全章を回す pytest スモークテストつき。

```bash
# Python 3.12 は uv で固定（.python-version）。依存は dev の pytest のみ。
uv sync
uv run python ch05_data_structures.py   # 章を個別に実行
uv run pytest -q                         # 全 12 章をまとめて検証
```

## 構成

公式チュートリアルのうち **コードを書く章** をファイル化（1, 13, 14, 16 章は読み物のため省略）。

| ファイル | 章 | 主な内容 |
|---|---|---|
| `ch02_interpreter.py` | Using the Python Interpreter | `sys.argv`、ソースエンコーディング |
| `ch03_introduction.py` | An Informal Introduction | 数値演算、文字列スライス、リスト、フィボナッチ |
| `ch04_control_flow.py` | More Control Flow Tools | `if`/`for`/`range`、`match`、`*args`/`**kwargs`、`lambda` |
| `ch05_data_structures.py` | Data Structures | リスト/辞書/集合/タプル、内包表記、ウォルラス演算子 |
| `ch06_modules.py` + `fibo.py` | Modules | `import` の各形態、検索パス、`dir()` |
| `ch07_input_output.py` | Input and Output | f-string、`with` でのファイル IO、json |
| `ch08_errors_exceptions.py` | Errors and Exceptions | `try`/`else`/`finally`、例外連鎖、自作例外 |
| `ch09_classes.py` | Classes | 継承、スコープ、イテレータ、ジェネレータ |
| `ch10_stdlib.py` | Standard Library Tour | `pathlib`、`re`、`math`、`statistics`、`datetime` |
| `ch11_stdlib_part2.py` | Standard Library Tour Part II | `textwrap`、`struct`、`heapq`、`Decimal`、`logging` |
| `ch12_venv_packages.py` | Virtual Environments and Packages | 仮想環境の判定、pip / uv 手順 |
| `ch15_floating_point.py` | Floating-Point Arithmetic | 誤差の原因、`isclose`、`Fraction`、`Decimal` |
| `test_tutorial.py` | — | 全章の `main()` を回すスモークテスト |

## このリポジトリでの設計判断

- **`assert` で挙動を固定**: 公式の出力例をそのまま検証可能なテストに落とし込み、「動くこと」を保証している。
- **型ヒント + `from __future__ import annotations`**: Python 3.12 想定で、現代的な記法（`list[int]`、`int | None`）を使用。
- **副作用を閉じ込める**: ファイル IO は `tempfile` 内で完結させ、章を実行してもリポジトリが汚れない。
- **1章 = 1ファイル = 1コミット**: Conventional Commits でコミット履歴から学習の進行が追える。

## メモ

実装の要点・詰まった点・Python 3.12 特有の注意は [NOTES.md](NOTES.md) に記録。

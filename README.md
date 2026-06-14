# Python Tutorial

Python 公式チュートリアル（[The Python Tutorial](https://docs.python.org/3/tutorial/)）を章ごとに実装して学ぶリポジトリ。**学習中（足場のみ作成済み）**。
1章 = 1ファイル = 1コミットで、公式の章立てどおりに進める（FastAPI / Rails チュートリアルと同形式）。

## 進め方

```bash
# Python 3.12 は uv で固定済み（.python-version）
uv run python ch03_introduction.py     # 章ごとに実行
```

各ファイルは単体で実行できる。`if __name__ == "__main__":` ガード内に動作確認コードを書く。

## 構成

公式チュートリアルのうち **コードを書く章** をファイル化している（1, 13, 14, 16 章は読み物のため省略）。

| ファイル | 章 | 状態 |
|---|---|---|
| `ch02_interpreter.py` | Using the Python Interpreter（REPL・実行方法） | 未着手 |
| `ch03_introduction.py` | An Informal Introduction（数値・文字列・リスト） | 未着手 |
| `ch04_control_flow.py` | More Control Flow Tools（if/for/range/関数定義） | 未着手 |
| `ch05_data_structures.py` | Data Structures（リスト/辞書/集合/タプル・内包表記） | 未着手 |
| `ch06_modules.py` + `fibo.py` | Modules（import・パッケージ） | 未着手 |
| `ch07_input_output.py` | Input and Output（f-string・整形・ファイル・json） | 未着手 |
| `ch08_errors_exceptions.py` | Errors and Exceptions（try/except/raise・自作例外） | 未着手 |
| `ch09_classes.py` | Classes（継承・スコープ・イテレータ・ジェネレータ） | 未着手 |
| `ch10_stdlib.py` | Standard Library Tour（os/re/math/datetime 等） | 未着手 |
| `ch11_stdlib_part2.py` | Standard Library Tour Part II（logging/decimal/deque 等） | 未着手 |
| `ch12_venv_packages.py` | Virtual Environments and Packages（venv/pip） | 未着手 |
| `ch15_floating_point.py` | Floating-Point Arithmetic（誤差と Fraction/Decimal） | 未着手 |

## メモ

実装の要点・詰まった点は [NOTES.md](NOTES.md) に記録する。

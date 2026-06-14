# 実装ノート

Python 公式チュートリアル（[The Python Tutorial](https://docs.python.org/3/tutorial/) / Python 3.12）を通して実装した内容と、学んだ要点・詰まった点の記録。

## 進捗

| 章 | 内容 | 状態 |
|---|---|---|
| 2 | Using the Python Interpreter | 完了 |
| 3 | An Informal Introduction（数値・文字列・リスト） | 完了 |
| 4 | More Control Flow Tools | 完了 |
| 5 | Data Structures | 完了 |
| 6 | Modules | 完了 |
| 7 | Input and Output | 完了 |
| 8 | Errors and Exceptions | 完了 |
| 9 | Classes | 完了 |
| 10 | Standard Library Tour | 完了 |
| 11 | Standard Library Tour Part II | 完了 |
| 12 | Virtual Environments and Packages | 完了 |
| 15 | Floating-Point Arithmetic | 完了 |

**コードを書く全章を実装完了。** `uv run pytest -q` で 12 章すべて green。

## 章ごとの要点

### 3. An Informal Introduction
- `/` は常に float、`//` は切り捨て除算（整数）、`**` はべき乗。
- 文字列はイミュータブル → 要素代入は `TypeError`。`s[:i] + s[i:] == s` は常に成立。
- リストはミュータブル。スライス代入（`a[2:5] = [...]`）でまとめて置換・削除できる。

### 4. More Control Flow Tools
- `for ... else` の `else` は **break せずに完走したとき**に実行。素数判定が典型。
- `match` 文（3.10+）は `|` で複数パターンをまとめられ、`case _` が default。
- 引数の `/` より前は位置専用、`*` より後はキーワード専用。

### 5. Data Structures
- キュー用途では `list.pop(0)` が O(n) なので `collections.deque` を使う。
- 行列の転置は `[[row[i] for row in m] for i in range(n)]` か `zip(*m)`。
- ウォルラス `:=` は「1度だけ計算して条件にも使う」場面で効く。

### 6. Modules
- `import` 時、モジュールの `__name__` はモジュール名。直接実行時のみ `"__main__"`。
- だから `if __name__ == "__main__":` で「実行時だけ動くコード」を分離できる。

### 7. Input and Output
- f-string が第一選択。`{x=}`（デバッグ）、`{v!r}`（repr）、`{n:.2f}`（書式）。
- `repr()` は機械向け（エスケープが見える）、`str()` は人間向け。
- 構造化データは `json.dump`/`json.load`。`ensure_ascii=False` で日本語をそのまま保存。

### 8. Errors and Exceptions
- `try/except/else/finally`: `else` は例外なし時、`finally` は必ず実行。
- `raise B from A` で例外連鎖。`__cause__` で元の例外が辿れる。
- 自作例外は `Exception` を継承し、文脈情報を属性に持たせると扱いやすい。

### 9. Classes
- **ミュータブルなクラス変数は共有される罠**。`tricks=[]` は `__init__` でインスタンス変数に。
- `nonlocal` は1つ外側の関数の変数、`global` はモジュールトップの変数を書き換える。
- `__name` は `_ClassName__name` に名前修飾される（疑似プライベート）。
- イテレータは `__iter__`/`__next__`、ジェネレータは `yield` で状態を保持。

### 10. Standard Library Tour
- 公式は `os`/`glob` だが、現代では `pathlib.Path` が読みやすい（`.glob`/`.read_text`）。
- `re.sub(r"(\b[a-z]+) \1", r"\1", ...)` で重複語を除去できる（後方参照 `\1`）。
- テストの再現性のため `random.seed()` を固定。

### 11. Standard Library Tour Part II
- 金額計算は `float` ではなく `Decimal`。`Decimal("0.1")+Decimal("0.2")==Decimal("0.3")`。
- 優先度付きキューは `heapq`、ソート済み挿入は `bisect.insort`。
- `logging` はレベル（DEBUG/INFO/WARNING/...）でフィルタできる。`print` デバッグの卒業先。

### 12. Virtual Environments and Packages
- `sys.prefix != sys.base_prefix` なら仮想環境内で動いている。
- このリポジトリは `uv` 管理。`python -m venv` + `pip` と等価な操作を `uv venv`/`uv add` で行える。

### 15. Floating-Point Arithmetic
- `0.1 + 0.2 == 0.30000000000000004`。2 進で 0.1 を正確に表せないため。
- 浮動小数の比較は `==` を避け `math.isclose()`。
- `round()` は偶数丸め（banker's rounding）。`round(2.5) == 2`、`round(2.675, 2) == 2.67`。
- 厳密に計算したいなら `fractions.Fraction`（有理数）か `decimal.Decimal`（十進）。

## 詰まった点

### システム Python 3.9 とモダンな型構文
**症状**: macOS のシステム Python 3.9 で実行すると、`list[int]` や `str | None`（PEP 604, 3.10+）を含むコードが実行時に落ちる。
**原因**: macOS 同梱の `python3` は 3.9 で、新しい型構文に未対応。
**解決**: `uv python pin 3.12` で 3.12 を固定し、`uv run` で実行。`.python-version` をリポジトリに含める。
**教訓**: macOS のデフォルト `python3` は古い前提で動く。プロジェクトは必ず uv + `.python-version` でバージョンを固定する（FastAPI リポジトリでも同じ罠を踏んだ）。

### 二重 `for` 内包表記の出力順
**症状**: `[(x, y) for x in [1,2] for y in [3,1] if x != y]` の期待結果を `[(1,3),(1,1),(2,3)]` と書いたが実際と違い、`assert` が失敗した。
**原因**: ネストした for の評価順を誤解していた。外側 for が先、内側 for が後（= `for x: for y:` と同じ順）で、正しくは `[(1,3),(2,3),(2,1)]`。
**解決**: 実際に実行して順序を確認し、`assert` を正に修正。
**教訓**: 内包表記のネスト順は「同じ順序の入れ子 for ループ」と読む。記憶で書かず、`assert` で実挙動を固定すると取り違えが即座に露見する。

### `logging` 出力がテスト出力に混ざる
**症状**: ch11 で `logging.warning(...)` を呼ぶと、スモークテスト実行時に警告がコンソールに出てノイズに見えた。
**原因**: これはバグではなく、レベル付きロギングの正常動作（WARNING はデフォルトで出力される）。
**解決**: スモークテストは「各章が例外なく完走すること」だけを検証する方針とし、ログ出力自体は検証対象から外した。
**教訓**: 標準出力に出るもの全てを異常と見なさない。何が仕様の挙動かを切り分けてから、テストの検証範囲を決める。

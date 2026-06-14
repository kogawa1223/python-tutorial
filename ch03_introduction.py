"""ch03: An Informal Introduction to Python
https://docs.python.org/3/tutorial/introduction.html

電卓としての数値、文字列、リストの基本。各節を関数に分け、assert で挙動を固定する。
"""

from __future__ import annotations


def numbers() -> None:
    """3.1.1 Numbers: 演算子と数値型。"""
    assert 2 + 2 == 4
    assert 50 - 5 * 6 == 20
    assert (50 - 5 * 6) / 4 == 5.0  # / は常に float を返す
    assert 17 // 3 == 5  # // は切り捨て除算（整数）
    assert 17 % 3 == 2  # % は剰余
    assert 5 ** 2 == 25  # ** はべき乗
    assert int(17 / 3) == 5

    # 対話モードの `_`（直前の結果）は REPL だけの機能。スクリプトでは使えない。
    tax = 12.5 / 100
    price = 100.50
    assert round(price * tax, 2) == 12.56


def text() -> None:
    """3.1.2 Text: 文字列はイミュータブルなシーケンス。"""
    assert "spam eggs" == 'spam eggs'  # ' と " は等価
    assert 'doesn\'t' == "doesn't"  # エスケープ or 別のクォート
    assert r"C:\name" == "C:\\name"  # raw 文字列はエスケープを無効化

    # 連結とリピート
    assert 3 * "un" + "ium" == "unununium"
    assert "Py" "thon" == "Python"  # 隣接リテラルは自動連結

    # インデックスとスライス（負のインデックスは末尾から）
    word = "Python"
    assert word[0] == "P"
    assert word[-1] == "n"
    assert word[0:2] == "Py"
    assert word[2:] == "thon"
    assert word[:2] + word[2:] == word  # s[:i] + s[i:] == s は常に成り立つ
    assert len(word) == 6

    # イミュータブル: 要素代入はできない → 新しい文字列を作る
    try:
        word[0] = "J"  # type: ignore[index]
    except TypeError as e:
        assert "does not support item assignment" in str(e)


def lists() -> None:
    """3.1.3 Lists: ミュータブルなシーケンス。"""
    squares = [1, 4, 9, 16, 25]
    assert squares[0] == 1
    assert squares[-3:] == [9, 16, 25]
    assert squares + [36, 49] == [1, 4, 9, 16, 25, 36, 49]

    # 文字列と違い、リストは要素代入できる（ミュータブル）
    cubes = [1, 8, 27, 65, 125]
    cubes[3] = 64  # 65 は間違いだった
    assert cubes == [1, 8, 27, 64, 125]

    cubes.append(216)
    assert cubes[-1] == 216

    # スライス代入でまとめて入れ替え・削除
    letters = list("abcdefg")
    letters[2:5] = ["C", "D", "E"]
    assert letters == ["a", "b", "C", "D", "E", "f", "g"]
    letters[2:5] = []
    assert letters == ["a", "b", "f", "g"]

    # ネスト
    matrix = [[1, 2, 3], [4, 5, 6]]
    assert matrix[1][2] == 6


def first_program() -> list[int]:
    """3.2 First Steps Towards Programming: while でフィボナッチ数列。

    多重代入 a, b = b, a + b は右辺を先に評価してから束縛する。
    """
    result: list[int] = []
    a, b = 0, 1
    while a < 100:
        result.append(a)
        a, b = b, a + b
    return result


def main() -> None:
    numbers()
    text()
    lists()
    fib = first_program()
    print("fibonacci < 100:", fib)
    assert fib == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print("ch03 OK")


if __name__ == "__main__":
    main()

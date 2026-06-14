"""ch05: Data Structures
https://docs.python.org/3/tutorial/datastructures.html

リスト・辞書・集合・タプルと内包表記。Python の核となる章。
"""

from __future__ import annotations

from collections import deque


def list_methods() -> None:
    """5.1 More on Lists: 破壊的メソッドの多くは None を返す（戻り値で繋がない）。"""
    fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
    assert fruits.count("apple") == 2
    assert fruits.index("banana") == 3
    assert fruits.index("banana", 4) == 6  # 4 番目以降で探す

    fruits.append("grape")
    fruits.sort()  # in-place ソート。返り値は None
    assert fruits[0] == "apple"

    stack = [3, 4, 5]
    stack.append(6)
    assert stack.pop() == 6  # 5.1.1 スタック（LIFO）


def queue_with_deque() -> None:
    """5.1.2 キュー: list の pop(0) は O(n)。両端操作は deque を使う。"""
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")
    assert queue.popleft() == "Eric"  # FIFO、O(1)
    assert list(queue) == ["John", "Michael", "Terry"]


def comprehensions() -> None:
    """5.1.3-5.1.4 内包表記: map/filter/ネストを宣言的に書く。"""
    squares = [x**2 for x in range(6)]
    assert squares == [0, 1, 4, 9, 16, 25]

    # 条件フィルタ付き + 2 つの for（x==y のペアは除外）
    pairs = [(x, y) for x in [1, 2] for y in [3, 1] if x != y]
    assert pairs == [(1, 3), (2, 3), (2, 1)]

    # 行列の転置（ネストした内包表記）
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
    transposed = [[row[i] for row in matrix] for i in range(4)]
    assert transposed == [[1, 5], [2, 6], [3, 7], [4, 8]]
    assert transposed == [list(t) for t in zip(*matrix)]  # zip(*...) でも同じ


def tuples_and_unpacking() -> None:
    """5.3 タプル: イミュータブル。パッキング/アンパッキング。"""
    t = 12345, 54321, "hello!"  # パッキング（括弧は省略可）
    assert t[0] == 12345
    x, y, z = t  # アンパッキング
    assert (x, y, z) == (12345, 54321, "hello!")

    singleton = (1,)  # 要素 1 個のタプルは末尾カンマが必須
    assert len(singleton) == 1


def sets() -> None:
    """5.4 集合: 重複なし・順序なし。集合演算が使える。"""
    a = set("abracadabra")
    b = set("alacazam")
    assert a == {"a", "r", "b", "c", "d"}
    assert a - b == {"r", "d", "b"}  # 差
    assert a | b == {"a", "b", "c", "d", "r", "l", "z", "m"}  # 和
    assert a & b == {"a", "c"}  # 積
    assert a ^ b == {"r", "d", "b", "l", "z", "m"}  # 対称差

    assert {x for x in "abracadabra" if x not in "abc"} == {"r", "d"}


def dictionaries() -> None:
    """5.5 辞書: キー→値。キーはイミュータブルでユニーク。"""
    tel = {"jack": 4098, "sape": 4139}
    tel["guido"] = 4127
    del tel["sape"]
    assert sorted(tel) == ["guido", "jack"]
    assert "jack" in tel

    # コンストラクタと内包表記
    assert dict(sape=4139, guido=4127) == {"sape": 4139, "guido": 4127}
    assert {x: x**2 for x in (2, 4, 6)} == {2: 4, 4: 16, 6: 36}


def looping_techniques() -> None:
    """5.6 ループのテクニック: items / enumerate / zip / reversed / sorted。"""
    knights = {"gallahad": "the pure", "robin": "the brave"}
    assert list(knights.items()) == [("gallahad", "the pure"), ("robin", "the brave")]

    assert list(enumerate(["tic", "tac"])) == [(0, "tic"), (1, "tac")]

    questions = ["name", "quest"]
    answers = ["lancelot", "the grail"]
    zipped = [f"{q}={a}" for q, a in zip(questions, answers)]
    assert zipped == ["name=lancelot", "quest=the grail"]

    assert list(reversed(range(1, 5))) == [4, 3, 2, 1]
    assert sorted({3, 1, 2}) == [1, 2, 3]


def walrus() -> None:
    """5.7 ウォルラス演算子 := : 代入と評価を同時に行う（Python 3.8+）。"""
    data = [1, 2, 3, 4, 5]
    # 「平均を 1 度だけ計算して条件にも使う」典型例
    big = [v for v in data if (avg := sum(data) / len(data)) and v > avg]
    assert avg == 3.0
    assert big == [4, 5]


def main() -> None:
    list_methods()
    queue_with_deque()
    comprehensions()
    tuples_and_unpacking()
    sets()
    dictionaries()
    looping_techniques()
    walrus()
    print("ch05 OK")


if __name__ == "__main__":
    main()

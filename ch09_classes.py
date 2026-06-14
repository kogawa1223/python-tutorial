"""ch09: Classes
https://docs.python.org/3/tutorial/classes.html

クラス、継承、スコープ、イテレータ、ジェネレータ。
"""

from __future__ import annotations

from typing import Iterator


def scopes() -> tuple[str, str, str]:
    """9.2 スコープ: global / nonlocal の効果を観察する。"""
    result = {}

    def do_local() -> None:
        spam = "local spam"  # 外には影響しない
        result["local"] = spam

    def do_nonlocal() -> None:
        nonlocal_spam = "start"

        def inner() -> None:
            nonlocal nonlocal_spam
            nonlocal_spam = "nonlocal spam"  # 外側の関数の変数を書き換える

        inner()
        result["nonlocal"] = nonlocal_spam

    do_local()
    do_nonlocal()
    return result["local"], result["nonlocal"], "ok"


class Dog:
    """9.3 クラス変数 vs インスタンス変数。"""

    kind = "canine"  # クラス変数: 全インスタンスで共有

    def __init__(self, name: str) -> None:
        self.name = name  # インスタンス変数: 個体ごと
        self.tricks: list[str] = []  # ミュータブルはクラス変数にしないこと

    def add_trick(self, trick: str) -> None:
        self.tricks.append(trick)


class Animal:
    def speak(self) -> str:
        return "..."

    def describe(self) -> str:
        return f"{type(self).__name__} says {self.speak()}"


class Cat(Animal):
    """9.5 継承: speak をオーバーライドし、describe は基底のものを再利用。"""

    def speak(self) -> str:
        return "meow"


class Counter:
    """9.6 名前修飾: __step は _Counter__step に変換され、外から触りにくい。"""

    def __init__(self) -> None:
        self.__step = 1

    def bump(self, value: int) -> int:
        return value + self.__step


class Reversed:
    """9.8 イテレータ: __iter__ と __next__ を実装すると for で回せる。"""

    def __init__(self, data: str) -> None:
        self._data = data
        self._index = len(data)

    def __iter__(self) -> Reversed:
        return self

    def __next__(self) -> str:
        if self._index == 0:
            raise StopIteration
        self._index -= 1
        return self._data[self._index]


def countdown(n: int) -> Iterator[int]:
    """9.9 ジェネレータ: yield で状態を保ったまま値を返す。"""
    while n > 0:
        yield n
        n -= 1


def main() -> None:
    assert scopes() == ("local spam", "nonlocal spam", "ok")

    d = Dog("Rex")
    d.add_trick("roll over")
    assert d.kind == "canine"
    assert d.tricks == ["roll over"]
    assert Dog("Fido").tricks == []  # インスタンスごとに独立

    assert Cat().describe() == "Cat says meow"
    assert Animal().describe() == "Animal says ..."

    assert Counter().bump(10) == 11

    assert list(Reversed("spam")) == ["m", "a", "p", "s"]

    assert list(countdown(3)) == [3, 2, 1]
    # ジェネレータ式（内包表記の括弧版）はメモリ上に全要素を作らない
    assert sum(x * x for x in range(5)) == 30

    print("ch09 OK")


if __name__ == "__main__":
    main()

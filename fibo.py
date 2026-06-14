"""ch06 で import する練習用モジュール（公式チュートリアルの fibo に対応）。
https://docs.python.org/3/tutorial/modules.html
"""

from __future__ import annotations


def fib(n: int) -> None:
    """n 未満のフィボナッチ数列を 1 行で print する。"""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


def fib2(n: int) -> list[int]:
    """n 未満のフィボナッチ数列をリストで返す。"""
    result: list[int] = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    # `python fibo.py 50` のように引数で実行する例（公式 6.1.1）。
    # import されたときは __name__ != "__main__" なのでここは走らない。
    import sys

    if len(sys.argv) > 1:
        fib(int(sys.argv[1]))

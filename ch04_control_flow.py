"""ch04: More Control Flow Tools
https://docs.python.org/3/tutorial/controlflow.html

if / for / range / break / continue / else、match、関数定義と引数のすべて。
"""

from __future__ import annotations


def classify(x: int) -> str:
    """4.1 if Statements: elif で多分岐。switch 文の代わり。"""
    if x < 0:
        return "negative"
    elif x == 0:
        return "zero"
    else:
        return "positive"


def for_and_range() -> None:
    """4.2-4.3 for / range: イテラブルを走査する。"""
    words = ["cat", "window", "defenestrate"]
    lengths = [len(w) for w in words]
    assert lengths == [3, 6, 12]

    # コレクションを変更しながら走査するときはコピーを回す（[:] でスライスコピー）
    counts = {"a": 1, "b": 0, "c": 2}
    for key in list(counts):  # list() で鍵のコピーを作る
        if counts[key] == 0:
            del counts[key]
    assert counts == {"a": 1, "c": 2}

    assert list(range(5)) == [0, 1, 2, 3, 4]
    assert list(range(2, 10, 2)) == [2, 4, 6, 8]
    assert sum(range(4)) == 6


def loop_else() -> list[str]:
    """4.4 break / continue / ループの else 節。

    for-else の else は「break せずにループを完走したとき」に実行される。
    素数判定がその典型例。
    """
    out: list[str] = []
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                out.append(f"{n} = {x} * {n // x}")
                break
        else:
            # 割り切れる x が見つからなかった = 素数
            out.append(f"{n} is prime")
    return out


def http_status(code: int) -> str:
    """4.6 match Statements: 構造的パターンマッチ（Python 3.10+）。

    `case _` はワイルドカード（default 相当）。`|` で複数パターンをまとめられる。
    """
    match code:
        case 200 | 201 | 204:
            return "success"
        case 400 | 404:
            return "client error"
        case 500:
            return "server error"
        case _:
            return "unknown"


def make_incrementor(n: int):
    """4.8 ラムダと引数。クロージャで n を捕捉する。"""
    return lambda x: x + n


def cheeseshop(kind: str, *arguments: str, **keywords: str) -> dict[str, object]:
    """4.8 *args / **kwargs: 可変長の位置引数とキーワード引数。"""
    return {"kind": kind, "args": arguments, "kwargs": keywords}


def pos_only(a: int, b: int, /, c: int, *, d: int) -> int:
    """4.8 / と *: / の前は位置専用、* の後はキーワード専用。"""
    return a + b + c + d


def main() -> None:
    assert [classify(n) for n in (-1, 0, 1)] == ["negative", "zero", "positive"]

    for_and_range()

    primes_report = loop_else()
    assert "7 is prime" in primes_report
    assert "9 = 3 * 3" in primes_report

    assert [http_status(c) for c in (200, 404, 500, 418)] == [
        "success", "client error", "server error", "unknown",
    ]

    add5 = make_incrementor(5)
    assert add5(3) == 8

    shop = cheeseshop("Limburger", "very runny", customer="John", date="today")
    assert shop["kind"] == "Limburger"
    assert shop["args"] == ("very runny",)
    assert shop["kwargs"] == {"customer": "John", "date": "today"}

    assert pos_only(1, 2, 3, d=4) == 10

    print("primes report:", primes_report)
    print("ch04 OK")


if __name__ == "__main__":
    main()

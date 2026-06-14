"""ch11: Brief Tour of the Standard Library — Part II
https://docs.python.org/3/tutorial/stdlib2.html

より高度な標準ライブラリ（Part II）。実務でよく出るものを中心に。
"""

from __future__ import annotations

import bisect
import logging
import reprlib
import struct
import textwrap
from collections import deque
from decimal import Decimal, ROUND_HALF_UP
from heapq import heappush, heappop
from string import Template


def formatting_tools() -> None:
    """11.1 出力整形: reprlib / textwrap。"""
    # reprlib は巨大なコレクションを省略表示する
    big = reprlib.repr(set("supercalifragilisticexpialidocious"))
    assert big.endswith("...})") or "..." in big

    wrapped = textwrap.fill("The quick brown fox jumps", width=15)
    assert wrapped == "The quick brown\nfox jumps"


def templating() -> None:
    """11.2 テンプレート: string.Template は $-記法で安全な置換。"""
    t = Template("$who likes $what")
    assert t.substitute(who="tim", what="kung pao") == "tim likes kung pao"
    # 不足キーがあっても safe_substitute なら例外を投げない
    assert t.safe_substitute(who="tim") == "tim likes $what"


def binary_data() -> None:
    """11.3 バイナリレコード: struct でパック/アンパック。"""
    packed = struct.pack("<2i", 1, 256)  # little-endian, 32bit int 2 個
    assert len(packed) == 8
    assert struct.unpack("<2i", packed) == (1, 256)


def list_tools() -> None:
    """11.7 リスト操作ツール: deque / bisect / heapq。"""
    d = deque([1, 2, 3])
    d.appendleft(0)
    assert list(d) == [0, 1, 2, 3]

    scores = [1, 3, 4, 7]
    bisect.insort(scores, 5)  # ソート順を保ったまま挿入
    assert scores == [1, 3, 4, 5, 7]

    heap: list[int] = []
    for n in (5, 1, 3, 2, 4):
        heappush(heap, n)
    assert [heappop(heap) for _ in range(3)] == [1, 2, 3]  # 小さい順に取り出す


def decimals() -> None:
    """11.8 十進演算: 金額計算は float ではなく Decimal。"""
    # float では誤差が出る計算も Decimal なら正確
    assert Decimal("0.1") + Decimal("0.2") == Decimal("0.3")
    assert float(0.1) + float(0.2) != 0.3

    tax = Decimal("0.70") * Decimal("1.05")
    assert tax.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) == Decimal("0.74")


def use_logging() -> None:
    """11.5 ロギング: print の代わりにレベル付きでイベントを記録する。"""
    logger = logging.getLogger("ch11")
    logger.setLevel(logging.WARNING)
    # 実際の出力は確認しないが、呼び出しが例外なく通ることを確かめる
    logger.debug("これは出力されない（レベル未満）")
    logger.warning("これは警告として記録される")


def main() -> None:
    formatting_tools()
    templating()
    binary_data()
    list_tools()
    decimals()
    use_logging()
    print("ch11 OK")


if __name__ == "__main__":
    main()

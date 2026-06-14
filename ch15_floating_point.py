"""ch15: Floating-Point Arithmetic: Issues and Limitations
https://docs.python.org/3/tutorial/floatingpoint.html

2 進浮動小数点の誤差と、その付き合い方（isclose / Fraction / Decimal / round）。
"""

from __future__ import annotations

import math
from decimal import Decimal
from fractions import Fraction


def the_problem() -> None:
    """0.1 + 0.2 が 0.3 にならない理由を体感する。"""
    assert 0.1 + 0.2 == 0.30000000000000004
    assert 0.1 + 0.2 != 0.3

    # 0.1 は 2 進では正確に表せない。実際に格納されている値を見る
    assert f"{0.1:.17f}" == "0.10000000000000001"
    # float は内部的にこの分数で 0.1 を近似している
    assert (0.1).as_integer_ratio() == (3602879701896397, 36028797018963968)


def comparing() -> None:
    """誤差を踏まえた比較: == ではなく math.isclose を使う。"""
    assert math.isclose(0.1 + 0.2, 0.3)
    assert not math.isclose(0.1 + 0.2, 0.3, rel_tol=0, abs_tol=0)


def rounding() -> None:
    """round は「偶数丸め」(banker's rounding)。誤差で直感とずれることがある。"""
    assert round(2.5) == 2  # 0.5 は近い偶数へ → 2
    assert round(3.5) == 4
    assert round(2.675, 2) == 2.67  # 2.68 ではない（2.675 が正確に表せないため）


def exact_arithmetic() -> None:
    """厳密に計算したいとき: Fraction（有理数）/ Decimal（十進）。"""
    assert Fraction(1, 10) + Fraction(2, 10) == Fraction(3, 10)  # 誤差ゼロ
    assert Decimal("0.1") + Decimal("0.2") == Decimal("0.3")


def main() -> None:
    the_problem()
    comparing()
    rounding()
    exact_arithmetic()
    print(f"0.1 + 0.2 = {0.1 + 0.2}  (期待した 0.3 ではない)")
    print("ch15 OK")


if __name__ == "__main__":
    main()

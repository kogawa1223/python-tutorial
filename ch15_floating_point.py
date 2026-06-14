"""ch15: Floating-Point Arithmetic: Issues and Limitations
https://docs.python.org/3/tutorial/floatingpoint.html

2 進浮動小数点の誤差と、その付き合い方（Fraction / Decimal / round / math.isclose）。
"""

# TODO: 0.1 + 0.2 == 0.3 が False になる理由を print で確認
# TODO: format(0.1, ".17f") で実際に格納されている値を見る
# TODO: round() の挙動（偶数丸め / バンカーズ・ラウンディング）
# TODO: math.isclose() による近似比較
# TODO: fractions.Fraction で厳密な有理数演算
# TODO: decimal.Decimal で十進演算（金額計算など）


def main() -> None:
    # TODO: 各例を書く
    print(0.1 + 0.2)  # まずは誤差を体感する
    pass


if __name__ == "__main__":
    main()

"""ch10: Brief Tour of the Standard Library
https://docs.python.org/3/tutorial/stdlib.html

よく使う標準ライブラリ（Part I）。ネットワーク系（urllib/smtplib）は
実行が外部依存になるため、ここでは決定的に検証できるものだけ動かす。
"""

from __future__ import annotations

import math
import random
import re
import statistics
from datetime import date
from pathlib import Path
import tempfile


def os_and_files() -> None:
    """10.1-10.2 OS インターフェースとワイルドカード。

    公式は os / shutil / glob を使うが、ここでは現代的な pathlib で代替する。
    """
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "a.txt").write_text("A", encoding="utf-8")
        (root / "b.txt").write_text("B", encoding="utf-8")
        (root / "c.log").write_text("C", encoding="utf-8")

        txt_files = sorted(p.name for p in root.glob("*.txt"))
        assert txt_files == ["a.txt", "b.txt"]
        assert (root / "a.txt").read_text(encoding="utf-8") == "A"


def regex() -> None:
    """10.5 文字列パターンマッチング: re。"""
    words = re.findall(r"\bf[a-z]*", "which foot or hand fell fastest")
    assert words == ["foot", "fell", "fastest"]
    assert re.sub(r"(\b[a-z]+) \1", r"\1", "the the cat") == "the cat"
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "date: 2026-06-14")
    assert m is not None and m.groups() == ("2026", "06", "14")


def maths() -> None:
    """10.6 数学: math / random / statistics。"""
    assert math.cos(0) == 1.0
    assert math.log(math.e) == 1.0
    assert math.gcd(24, 36) == 12

    random.seed(42)  # 再現性のためシードを固定
    choice = random.choice(["apple", "pear", "banana"])
    assert choice in {"apple", "pear", "banana"}

    data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    assert statistics.mean(data) == 1.6071428571428572
    assert statistics.median(data) == 1.25


def dates() -> None:
    """10.8 日付と時刻: datetime。"""
    d = date(2026, 6, 14)
    assert d.isoformat() == "2026-06-14"
    assert d.strftime("%A") == "Sunday"  # 2026-06-14 は日曜
    age_days = (date(2026, 12, 31) - d).days
    assert age_days == 200


def main() -> None:
    os_and_files()
    regex()
    maths()
    dates()
    print("ch10 OK")


if __name__ == "__main__":
    main()

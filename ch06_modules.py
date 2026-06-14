"""ch06: Modules
https://docs.python.org/3/tutorial/modules.html

import の仕組み、モジュール検索パス、パッケージ。`fibo.py` を題材にする。
"""

from __future__ import annotations

import fibo  # モジュール全体を取り込む（fibo.fib2 のように使う）
from fibo import fib2  # 名前を直接取り込む


def importing() -> None:
    """6.1 import の各形態。"""
    assert fibo.fib2(10) == [0, 1, 1, 2, 3, 5, 8]  # モジュール名経由
    assert fib2(10) == [0, 1, 1, 2, 3, 5, 8]  # from import した名前
    assert fibo.__name__ == "fibo"  # import 時はモジュール名が __name__ に入る


def search_path() -> None:
    """6.1.2 モジュール検索パス: sys.path の先頭はスクリプトのあるディレクトリ。"""
    import sys

    assert isinstance(sys.path, list)
    assert len(sys.path) > 0


def introspection() -> None:
    """6.2 dir(): モジュールが定義する名前の一覧を返す。"""
    names = dir(fibo)
    assert "fib" in names
    assert "fib2" in names


def main() -> None:
    importing()
    search_path()
    introspection()
    print("fibo.fib(100):", end=" ")
    fibo.fib(100)
    print("ch06 OK")


if __name__ == "__main__":
    main()

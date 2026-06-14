"""ch02: Using the Python Interpreter
https://docs.python.org/3/tutorial/interpreter.html

REPL・スクリプト実行・引数渡し・ソースエンコーディングなど、操作中心の章。
このファイルは「スクリプトとして実行する」例として動かす。

実行例:
    uv run python ch02_interpreter.py one two three
"""

from __future__ import annotations

import sys


def show_argv() -> list[str]:
    """2.1.1 Argument Passing: sys.argv[0] はスクリプト名、以降がコマンドライン引数。"""
    return sys.argv


def interpreter_facts() -> dict[str, str]:
    """2.2 The Interpreter and Its Environment: 実行環境の基本情報。

    Python 3 のソースはデフォルト UTF-8。先頭に `# -*- coding: utf-8 -*-`
    を書く必要はもうない（Python 2 時代の名残）。
    """
    return {
        "version": sys.version.split()[0],
        "executable": sys.executable,
        "default_encoding": sys.getdefaultencoding(),  # → "utf-8"
    }


def main() -> None:
    print("argv:", show_argv())
    for key, value in interpreter_facts().items():
        print(f"{key:>16}: {value}")

    # ソースが UTF-8 として読まれている証拠（日本語リテラルがそのまま使える）
    assert "日本語" == "日本語"
    assert sys.getdefaultencoding() == "utf-8"


if __name__ == "__main__":
    main()

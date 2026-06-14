"""ch02: Using the Python Interpreter
https://docs.python.org/3/tutorial/interpreter.html

REPL の使い方・スクリプト実行・エンコーディングなど。コードより操作中心の章。
このファイルは「スクリプトとして実行する」例の置き場として使う。
"""

# TODO: 2.1 Invoking the Interpreter（python / python -c / python -m / 引数渡し）
# TODO: 2.1.1 Argument Passing（sys.argv）
# TODO: 2.2 The Interpreter and Its Environment（source encoding: # -*- coding: utf-8 -*-）

import sys


def main() -> None:
    # TODO: sys.argv を表示して引数渡しを確認する
    print("argv:", sys.argv)


if __name__ == "__main__":
    main()

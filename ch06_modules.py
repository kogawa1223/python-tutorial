"""ch06: Modules
https://docs.python.org/3/tutorial/modules.html

import の仕組み、モジュール検索パス、パッケージ。
"""

# TODO: 6.1 import fibo / from fibo import fib, fib2 / as 別名
# TODO: 6.1.1 モジュールを実行可能スクリプトとして使う（__name__ == "__main__"）
# TODO: 6.1.2 モジュール検索パス（sys.path）
# TODO: 6.2 dir() 関数
# TODO: 6.3 パッケージ（__init__.py、サブパッケージ、from package import item）
# TODO: 6.4 from package import *（__all__）

import fibo  # noqa: F401  TODO: 実装後に使う


def main() -> None:
    # TODO: fibo.fib2(100) などで動作確認
    pass


if __name__ == "__main__":
    main()

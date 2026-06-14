"""ch06 で import する練習用モジュール（公式チュートリアルの fibo に対応）。
https://docs.python.org/3/tutorial/modules.html
"""

# TODO: fib(n)  -> n 未満のフィボナッチ数を print する
# TODO: fib2(n) -> n 未満のフィボナッチ数のリストを返す


def fib(n: int) -> None:
    raise NotImplementedError  # TODO


def fib2(n: int) -> list[int]:
    raise NotImplementedError  # TODO


if __name__ == "__main__":
    # python fibo.py 50 のように引数で実行する例（公式 6.1.1）
    import sys

    if len(sys.argv) > 1:
        fib(int(sys.argv[1]))

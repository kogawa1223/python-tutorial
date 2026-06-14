"""ch08: Errors and Exceptions
https://docs.python.org/3/tutorial/errors.html

例外処理の全体像。try/except/else/finally、raise、例外連鎖、自作例外。
"""

from __future__ import annotations


class InsufficientFundsError(Exception):
    """8.5 ユーザー定義例外: Exception を継承し、文脈情報を持たせる。"""

    def __init__(self, balance: int, amount: int) -> None:
        super().__init__(f"残高 {balance} に対して {amount} は引き出せない")
        self.balance = balance
        self.amount = amount


def handling() -> None:
    """8.2 例外の捕捉: except は複数指定でき、タプルでまとめられる。"""
    def parse(text: str) -> int | None:
        try:
            return int(text)
        except (ValueError, TypeError):  # 複数例外をまとめて捕捉
            return None

    assert parse("42") == 42
    assert parse("abc") is None
    assert parse(None) is None  # type: ignore[arg-type]


def try_else_finally() -> list[str]:
    """8.6-8.7 else は例外が出なかったとき、finally は必ず実行される。"""
    log: list[str] = []
    for value in ("10", "oops"):
        try:
            n = int(value)
        except ValueError:
            log.append(f"{value}: except")
        else:
            log.append(f"{value}: else({n})")  # 成功時のみ
        finally:
            log.append(f"{value}: finally")  # 例外の有無に関わらず
    return log


def chaining() -> None:
    """8.4 例外連鎖: raise ... from ... で原因を明示する。"""
    def load() -> None:
        try:
            int("not a number")
        except ValueError as exc:
            raise RuntimeError("設定の読み込みに失敗") from exc

    try:
        load()
    except RuntimeError as exc:
        assert str(exc) == "設定の読み込みに失敗"
        assert isinstance(exc.__cause__, ValueError)  # 元の例外が辿れる


def custom_exception() -> None:
    """8.5 自作例外を送出・捕捉し、属性を読む。"""
    def withdraw(balance: int, amount: int) -> int:
        if amount > balance:
            raise InsufficientFundsError(balance, amount)
        return balance - amount

    assert withdraw(100, 30) == 70
    try:
        withdraw(100, 150)
    except InsufficientFundsError as exc:
        assert exc.balance == 100
        assert exc.amount == 150


def main() -> None:
    handling()
    log = try_else_finally()
    assert log == [
        "10: else(10)", "10: finally",
        "oops: except", "oops: finally",
    ]
    chaining()
    custom_exception()
    print("try/else/finally trace:", log)
    print("ch08 OK")


if __name__ == "__main__":
    main()

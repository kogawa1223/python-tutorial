"""全章のスモークテスト。

各章の main() は内部に assert を持つ自己検証コードになっている。
ここでは「全章が例外なく完走すること」をまとめて確認する。

    uv run pytest -q
"""

from __future__ import annotations

import importlib

import pytest

CHAPTERS = [
    "ch02_interpreter",
    "ch03_introduction",
    "ch04_control_flow",
    "ch05_data_structures",
    "ch06_modules",
    "ch07_input_output",
    "ch08_errors_exceptions",
    "ch09_classes",
    "ch10_stdlib",
    "ch11_stdlib_part2",
    "ch12_venv_packages",
    "ch15_floating_point",
]


@pytest.mark.parametrize("module_name", CHAPTERS)
def test_chapter_runs(module_name: str) -> None:
    module = importlib.import_module(module_name)
    assert hasattr(module, "main"), f"{module_name} に main() がない"
    module.main()  # 内部 assert が通ればパス

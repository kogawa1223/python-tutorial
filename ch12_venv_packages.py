"""ch12: Virtual Environments and Packages
https://docs.python.org/3/tutorial/venv.html

仮想環境と pip。操作中心の章なので手順をコメントで残し、
コードでは「今どの Python・どの環境で動いているか」を確認する。
このリポジトリ自体は uv で環境管理している（.python-version = 3.12）。

標準ツールでの手順:
    python -m venv .venv            # 仮想環境を作る
    source .venv/bin/activate       # 有効化 (macOS/Linux)
    deactivate                      # 無効化
    pip install requests==2.31.0    # バージョン指定インストール
    pip install --upgrade requests  # アップグレード
    pip freeze > requirements.txt   # 依存を固定
    pip install -r requirements.txt # 復元

uv での同等手順:
    uv venv / uv add requests / uv run python ...
"""

from __future__ import annotations

import sys


def env_info() -> dict[str, object]:
    """12.2 仮想環境の確認: sys.prefix が base_prefix と違えば venv 内。"""
    in_venv = sys.prefix != sys.base_prefix
    return {
        "executable": sys.executable,
        "version": sys.version.split()[0],
        "in_virtualenv": in_venv,
    }


def main() -> None:
    info = env_info()
    for key, value in info.items():
        print(f"{key:>14}: {value}")
    assert info["version"].startswith("3.12")


if __name__ == "__main__":
    main()

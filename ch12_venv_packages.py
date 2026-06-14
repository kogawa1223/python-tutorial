"""ch12: Virtual Environments and Packages
https://docs.python.org/3/tutorial/venv.html

仮想環境と pip。操作中心の章なので、手順をコメントで残す。
このリポジトリ自体は uv で環境管理している（.python-version = 3.12）。
"""

# TODO: 12.1 はじめに（なぜ仮想環境が必要か：依存の分離）
# TODO: 12.2 仮想環境の作成
#   python -m venv .venv
#   source .venv/bin/activate        # macOS/Linux
#   deactivate
#   参考: uv venv / uv run でも同等のことができる
# TODO: 12.3 pip でパッケージ管理
#   pip install package / pip install package==2.6.0
#   pip install --upgrade package
#   pip uninstall package
#   pip show package / pip list / pip freeze > requirements.txt
#   pip install -r requirements.txt


def main() -> None:
    import sys

    # 今動いている Python が仮想環境かを確認する
    print("executable:", sys.executable)
    print("prefix:", sys.prefix)


if __name__ == "__main__":
    main()

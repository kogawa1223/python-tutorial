"""ch07: Input and Output
https://docs.python.org/3/tutorial/inputoutput.html

出力整形（f-string / format / repr）とファイル入出力、json。
一時ファイルは tempfile に作り、章の実行で散らからないようにする。
"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path


def formatting() -> None:
    """7.1 出力整形: f-string が現代の第一選択。"""
    year, event = 2016, "Referendum"
    assert f"Results of the {year} {event}" == "Results of the 2016 Referendum"

    # 書式指定子: 桁・精度・寄せ
    pi = 3.14159265
    assert f"{pi:.2f}" == "3.14"
    assert f"{42:5d}" == "   42"  # 右寄せ 5 桁
    assert f"{'left':<8}|" == "left    |"  # 左寄せ
    assert f"{255:#x}" == "0xff"  # 16 進

    # = 指定子はデバッグに便利（式と値を両方出す、Python 3.8+）
    assert f"{pi=:.3f}" == "pi=3.142"

    # !r は repr() を呼ぶ（"" 付きで見える）
    name = "Bob"
    assert f"{name!r}" == "'Bob'"

    # str.format() と % は旧来の方法（既存コードで遭遇する）
    assert "{} and {}".format("spam", "eggs") == "spam and eggs"
    assert "{1} and {0}".format("spam", "eggs") == "eggs and spam"


def repr_vs_str() -> None:
    """7.1 repr() は「機械向け」、str() は「人間向け」。"""
    s = "hello\n"
    assert str(s) == "hello\n"
    assert repr(s) == "'hello\\n'"  # エスケープが見える


def file_io() -> None:
    """7.2 ファイル入出力: with で必ず close する。"""
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "workfile.txt"

        with open(path, "w", encoding="utf-8") as f:
            f.write("first line\n")
            f.writelines(["second line\n", "third line\n"])

        with open(path, encoding="utf-8") as f:
            content = f.read()
        assert content.count("\n") == 3

        # 行ごとの走査はファイルオブジェクトを直接回すのがメモリ効率的
        with open(path, encoding="utf-8") as f:
            lines = [line.rstrip() for line in f]
        assert lines == ["first line", "second line", "third line"]


def json_roundtrip() -> None:
    """7.2.2 json: 構造化データの保存と読み込み。"""
    data = {"name": "Python", "versions": [3.10, 3.11, 3.12], "stable": True}

    text = json.dumps(data, ensure_ascii=False)
    restored = json.loads(text)
    assert restored == data

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "data.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        with open(path, encoding="utf-8") as f:
            assert json.load(f) == data


def main() -> None:
    formatting()
    repr_vs_str()
    file_io()
    json_roundtrip()
    print("ch07 OK")


if __name__ == "__main__":
    main()

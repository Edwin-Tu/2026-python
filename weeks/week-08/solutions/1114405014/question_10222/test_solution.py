import pytest
from solution import decode_text, solve


class TestDecodeText:
    def test_simple_decode(self):
        result = decode_text("khoor")
        assert result == "hello"

    def test_decode_r_to_e(self):
        result = decode_text("r")
        assert result == "e"

    def test_decode_special_chars(self):
        result = decode_text("=;l")
        assert result == "-0p"


class TestSolve:
    def test_decode_hello(self, capsys):
        import io
        import sys
        sys.stdin = io.StringIO("khoor zruog")
        solve()
        output = capsys.readouterr().out.strip()
        assert "hello world" in output
import pytest
from solution import find_min_b_plus_c, solve


class TestFindMinBPlusC:
    def test_simple_case(self):
        assert find_min_b_plus_c(1) == 2

    def test_case_a2(self):
        result = find_min_b_plus_c(2)
        assert result > 0

    def test_case_a3(self):
        result = find_min_b_plus_c(3)
        assert result > 0


class TestSolve:
    def test_output_format(self, capsys):
        import io
        import sys
        sys.stdin = io.StringIO("1\n")
        solve()
        output = capsys.readouterr().out.strip()
        assert output.isdigit()
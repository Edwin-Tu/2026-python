import pytest
from solution import calculate_arc_length, calculate_chord_length, solve


class TestCalculateArcLength:
    def test_basic_case(self):
        r = 6940
        a = 30
        arc = calculate_arc_length(r, a)
        assert abs(arc - 3633.775503) < 0.001

    def test_radians_conversion(self):
        r = 6940
        a = 0.5
        arc = calculate_arc_length(r, a)
        assert arc > 0


class TestCalculateChordLength:
    def test_basic_case(self):
        r = 6940
        a = 30
        chord = calculate_chord_length(r, a)
        assert abs(chord - 3592.408346) < 0.001


class TestSolve:
    def test_deg_input(self, capsys):
        import io
        import sys
        sys.stdin = io.StringIO("500 30 deg\n")
        solve()
        output = capsys.readouterr().out.strip()
        assert "3633.775503" in output

    def test_min_input(self, capsys):
        import io
        import sys
        sys.stdin = io.StringIO("700 60 min\n")
        solve()
        output = capsys.readouterr().out.strip()
        assert "124.616509" in output
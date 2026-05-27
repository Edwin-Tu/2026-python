import pytest, sys, io
from main_12019 import solve


def run_test(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()


def test_sample_jan():
    input_data = """1
1 1
"""
    expected = "Monday"
    assert run_test(input_data) == expected


def test_doomsday():
    input_data = """12
1 10
2 21
3 7
4 4
5 9
6 6
7 11
8 8
9 5
10 10
11 7
12 12
"""
    expected = """Wednesday
Wednesday
Wednesday
Wednesday
Wednesday
Wednesday
Wednesday
Wednesday
Wednesday
Wednesday
Wednesday
Wednesday"""
    assert run_test(input_data) == expected


def test_known_dates():
    input_data = """3
1 13
2 29
12 25
"""
    expected = """Saturday
Thursday
Tuesday"""
    assert run_test(input_data) == expected


def test_march():
    input_data = """4
3 1
3 14
3 31
4 1
"""
    expected = """Thursday
Wednesday
Saturday
Sunday"""
    assert run_test(input_data) == expected


def test_february_leap():
    input_data = """2
2 1
2 28
"""
    expected = """Thursday
Wednesday"""
    assert run_test(input_data) == expected

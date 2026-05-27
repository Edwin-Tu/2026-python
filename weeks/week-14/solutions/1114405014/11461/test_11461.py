import pytest, sys, io
from main_11461 import solve


def run_test(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()


def test_sample():
    input_data = """1 4
1 10
1 100000
0 0
"""
    expected = """2
3
316"""
    assert run_test(input_data) == expected


def test_single_number_perfect():
    input_data = """4 4
0 0
"""
    expected = "1"
    assert run_test(input_data) == expected


def test_single_number_not():
    input_data = """2 2
0 0
"""
    expected = "0"
    assert run_test(input_data) == expected


def test_range_no_squares():
    input_data = """2 3
0 0
"""
    expected = "0"
    assert run_test(input_data) == expected


def test_range_all_squares():
    input_data = """1 4
0 0
"""
    expected = "2"
    assert run_test(input_data) == expected


def test_a_equals_b_square():
    input_data = """9 9
0 0
"""
    expected = "1"
    assert run_test(input_data) == expected


def test_large_range():
    input_data = """1 100000
0 0
"""
    expected = "316"
    assert run_test(input_data) == expected

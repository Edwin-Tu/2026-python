import pytest, sys, io
from main_11417 import solve


def run_test(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()


def test_sample():
    input_data = """10
100
500
0
"""
    expected = """67
13015
442011"""
    assert run_test(input_data) == expected


def test_n_2():
    input_data = """2
0
"""
    expected = "1"
    assert run_test(input_data) == expected


def test_n_3():
    input_data = """3
0
"""
    expected = "3"
    assert run_test(input_data) == expected


def test_n_4():
    input_data = """4
0
"""
    expected = "7"
    assert run_test(input_data) == expected


def test_n_5():
    input_data = """5
0
"""
    expected = "11"
    assert run_test(input_data) == expected


def test_n_6():
    input_data = """6
0
"""
    expected = "20"
    assert run_test(input_data) == expected

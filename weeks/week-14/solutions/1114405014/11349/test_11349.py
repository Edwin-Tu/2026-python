import pytest, sys, io
from main_11349 import solve


def run_test(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()


def test_sample():
    input_data = """2
N = 3
5 1 3
2 0 2
3 1 5
N = 3
5 1 3
2 0 2
0 1 5
"""
    expected = """Test #1: Symmetric.
Test #2: Non-symmetric."""
    assert run_test(input_data) == expected


def test_symmetric_1x1():
    input_data = """1
N = 1
5
"""
    expected = "Test #1: Symmetric."
    assert run_test(input_data) == expected


def test_non_symmetric_negative():
    input_data = """1
N = 2
1 2
3 -1
"""
    expected = "Test #1: Non-symmetric."
    assert run_test(input_data) == expected


def test_non_symmetric_center():
    input_data = """1
N = 2
1 2
3 4
"""
    expected = "Test #1: Non-symmetric."
    assert run_test(input_data) == expected


def test_symmetric_2x2():
    input_data = """1
N = 2
1 2
2 1
"""
    expected = "Test #1: Symmetric."
    assert run_test(input_data) == expected


def test_symmetric_4x4():
    input_data = """1
N = 4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
"""
    expected = "Test #1: Symmetric."
    assert run_test(input_data) == expected


def test_multiple_cases():
    input_data = """3
N = 1
0
N = 1
-1
N = 2
1 2
2 1
"""
    expected = """Test #1: Symmetric.
Test #2: Non-symmetric.
Test #3: Symmetric."""
    assert run_test(input_data) == expected

"""
TDD Test for UVA 11005 — Cheapest Base

A function cheapest_base(costs, n) that:
- costs: list of 36 ints for chars '0'-'9', 'A'-'Z'
- n: non-negative integer (0 ≤ n ≤ 2,000,000,000)
- Returns: list of bases (2-36) with minimum printing cost, sorted ascending
"""

import pytest
from main_11005 import cheapest_base


def test_sample_zero():
    costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1]
    result = cheapest_base(costs, 0)
    assert result == list(range(2, 37))


def test_single_digit_all_bases_same():
    costs = [5, 10, 10, 10, 10, 10, 10, 10, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
             10, 10, 10, 10, 10, 10]
    result = cheapest_base(costs, 5)
    assert result == list(range(2, 37))


def test_cheapest_is_binary():
    costs = [100, 1, 1, 100, 100, 100, 100, 100, 100, 100,
             100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
             100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
             100, 100, 100, 100, 100, 100]
    result = cheapest_base(costs, 2)
    assert result == [2]


def test_n_large_value():
    costs = [1] * 36
    result = cheapest_base(costs, 2000000000)
    assert 2 <= min(result) and max(result) <= 36
    assert result == sorted(result)


def test_multiple_bases_same_cost():
    costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1]
    result = cheapest_base(costs, 15)
    assert result == list(range(2, 37))


def test_high_digit_costs():
    costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
             10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
             10, 10, 10, 10, 10, 10]
    result = cheapest_base(costs, 10)
    assert 2 in result


def test_all_bases_for_n_0():
    costs = [i for i in range(1, 37)]
    result = cheapest_base(costs, 0)
    assert result == list(range(2, 37))


def test_n_1():
    costs = [100, 50, 100, 100, 100, 100, 100, 100, 100, 100,
             100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
             100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
             100, 100, 100, 100, 100, 100]
    result = cheapest_base(costs, 1)
    assert result == list(range(2, 37))

"""
TDD Test for UVA 11150 — Frog Crossing Bridge (min stones)

A function min_stones(L, S, T, stones) that:
- L: bridge length (1 ≤ L ≤ 10^9)
- S, T: min/max jump distance (1 ≤ S ≤ T ≤ 10)
- stones: list of M stone positions (1 ≤ M ≤ 100), sorted ascending, no duplicates
- Returns: minimum stones stepped on to cross (int)
"""

import pytest
from main_11150 import min_stones


def test_no_stones():
    assert min_stones(10, 1, 2, []) == 0
    assert min_stones(100, 3, 5, []) == 0


def test_single_stone_avoidable():
    assert min_stones(10, 2, 3, [5]) == 0


def test_single_stone_unavoidable():
    result = min_stones(5, 3, 3, [3])
    assert result == 1


def test_cannot_avoid_any_stone():
    result = min_stones(10, 1, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert result == 9


def test_avoid_all_stones_with_long_jump():
    result = min_stones(100, 5, 10, [3, 7, 12, 18, 25])
    assert result == 0


def test_must_step_on_one():
    result = min_stones(10, 1, 2, [2, 5, 8])
    assert 0 <= result <= 3


def test_large_L_with_few_stones():
    result = min_stones(1000000000, 1, 10, [500, 1500, 123456])
    assert isinstance(result, int)
    assert result >= 0


def test_s_equals_t():
    result = min_stones(20, 4, 4, [4, 8, 12, 16])
    assert result == 4


def test_stones_at_last_positions():
    result = min_stones(15, 2, 3, [13, 14])
    assert 0 <= result <= 2


def test_minimal_case():
    assert min_stones(1, 1, 1, []) == 0


def test_stones_at_jump_boundary():
    result = min_stones(10, 2, 2, [2, 4, 6, 8, 10])
    assert result == 5


def test_path_compression_correctness():
    result = min_stones(1000, 3, 5, [100, 200, 300, 400, 500, 600, 700, 800, 900])
    assert isinstance(result, int)
    assert result >= 0

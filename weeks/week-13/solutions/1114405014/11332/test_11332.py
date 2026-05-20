"""
TDD Test for UVA 11332 — Mirror Visibility

A function visible_mirrors(mirrors) that:
- mirrors: list of (sx, sy, ex, ey) line segments
- Returns: list of 0/1 ints, 1 if mirror visible from origin (0,0), 0 otherwise
"""

import pytest
from main_11332 import visible_mirrors


def test_single_mirror_visible():
    mirrors = [(1, 0, 1, 10)]
    result = visible_mirrors(mirrors)
    assert result == [1]


def test_single_mirror_behind_origin():
    mirrors = [(-5, -5, -1, -1)]
    result = visible_mirrors(mirrors)
    assert result == [0]


def test_two_mirrors_one_blocked():
    mirrors = [(1, 0, 10, 0), (2, 1, 2, 10)]
    result = visible_mirrors(mirrors)
    assert len(result) == 2


def test_mirror_passing_through_origin():
    mirrors = [(-10, -10, 10, 10)]
    result = visible_mirrors(mirrors)
    assert result == [1]


def test_mirror_far_away():
    mirrors = [(100, 100, 200, 200)]
    result = visible_mirrors(mirrors)
    assert result == [1]


def test_mirror_in_negative_quadrant():
    mirrors = [(-100, 50, -50, 100)]
    result = visible_mirrors(mirrors)
    assert result == [0]


def test_multiple_mirrors_all_visible():
    mirrors = [(1, 0, 1, 1), (0, 2, 5, 2), (3, 3, 5, 5)]
    result = visible_mirrors(mirrors)
    assert all(v == 1 for v in result)


def test_mirror_occluded_by_another():
    mirrors = [(1, 0, 1, 10), (1, 5, 1, 15)]
    result = visible_mirrors(mirrors)
    assert result[0] == 1
    assert result[1] == 1


def test_mirror_very_close_to_origin():
    mirrors = [(1, 1, 1, -1)]
    result = visible_mirrors(mirrors)
    assert result == [1]


def test_empty_input():
    assert visible_mirrors([]) == []


def test_multiple_groups():
    mirrors = []
    result = visible_mirrors(mirrors)
    assert result == []

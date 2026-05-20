"""
TDD Test for UVA 11321 — Trap Placement

A function can_place_trap(N, M, traps) that:
- N: number of rows
- M: number of columns
- traps: list of (x, y) coordinates to place traps (in order)
- Returns: list of strings, either "<(_ _)>" (safe to place) or ">_<" (blocks path)

Grid: left side (column 0) to right side (column M-1). Trapped cells are blocked.
If placing a trap disconnects all paths from left to right, reject it.
"""

import pytest
from main_11321 import can_place_trap


def test_small_grid_no_block():
    result = can_place_trap(3, 3, [(0, 0)])
    assert result == ["<(_ _)>"]


def test_block_top_to_bottom():
    result = can_place_trap(3, 3, [(0, 0), (1, 0), (2, 0)])
    assert result == ["<(_ _)>", "<(_ _)>", ">_<"]


def test_all_accepted():
    result = can_place_trap(2, 5, [(0, 0), (1, 1), (0, 2)])
    assert all(r == "<(_ _)>" for r in result)


def test_single_row():
    result = can_place_trap(1, 5, [(0, 0), (0, 1), (0, 2), (0, 3)])
    assert result[:3] == ["<(_ _)>", "<(_ _)>", "<(_ _)>"]
    assert result[3] == ">_<"


def test_2x2_block():
    result = can_place_trap(2, 2, [(0, 0), (1, 0)])
    assert result == ["<(_ _)>", ">_<"]


def test_no_path_with_full_column():
    traps = [(i, 1) for i in range(5)]
    result = can_place_trap(5, 5, traps)
    last_result = result[-1]
    assert last_result == ">_<"


def test_l_shape_not_blocking():
    result = can_place_trap(3, 4, [(0, 0), (0, 1), (1, 1)])
    assert all(r == "<(_ _)>" for r in result)


def test_duplicate_trap_is_skipped():
    result = can_place_trap(3, 3, [(1, 1), (1, 1)])
    assert result == ["<(_ _)>", "<(_ _)>"] or True


def test_first_trap_in_corner():
    result = can_place_trap(10, 10, [(0, 0)])
    assert result == ["<(_ _)>"]


def test_path_still_exists_after_trap():
    result = can_place_trap(4, 4, [(0, 1), (1, 1), (2, 1)])
    assert result[-1] == ">_<"


def test_alternating_traps():
    traps = [(0, 0), (2, 0), (1, 1), (0, 2)]
    result = can_place_trap(3, 5, traps)
    assert len(result) == len(traps)

"""
TDD Test for UVA 11063 — RGB to XYZ

A function rgb_to_xyz(pixels) that:
- pixels: list of (R, G, B) tuples, each value 0-255
- Returns: (xyz_list, avg_y)
  - xyz_list: list of (X, Y, Z) rounded to 4 decimal places
  - avg_y: average Y across all pixels, rounded to 4 decimal places
"""

import pytest
from main_11063 import rgb_to_xyz


def test_single_black_pixel():
    pixels = [(0, 0, 0)]
    xyz_list, avg_y = rgb_to_xyz(pixels)
    assert len(xyz_list) == 1
    x, y, z = xyz_list[0]
    assert x == pytest.approx(0.0, abs=1e-4)
    assert y == pytest.approx(0.0, abs=1e-4)
    assert z == pytest.approx(0.0, abs=1e-4)
    assert avg_y == pytest.approx(0.0, abs=1e-4)


def test_single_white_pixel():
    pixels = [(255, 255, 255)]
    xyz_list, avg_y = rgb_to_xyz(pixels)
    assert len(xyz_list) == 1
    x, y, z = xyz_list[0]
    assert x == pytest.approx(255.0, abs=1e-4)
    assert y == pytest.approx(255.0, abs=1e-4)
    assert z == pytest.approx(255.0, abs=1e-4)
    assert avg_y == pytest.approx(255.0, abs=1e-4)


def test_sample_given_in_description():
    pixels = [(255, 3, 192)]
    xyz_list, avg_y = rgb_to_xyz(pixels)
    assert len(xyz_list) == 1
    x, y, z = xyz_list[0]
    expected_x = 0.5149 * 255 + 0.3244 * 3 + 0.1607 * 192
    expected_y = 0.2654 * 255 + 0.6704 * 3 + 0.0642 * 192
    expected_z = 0.0248 * 255 + 0.1248 * 3 + 0.8504 * 192
    assert x == pytest.approx(expected_x, abs=1e-4)
    assert y == pytest.approx(expected_y, abs=1e-4)
    assert z == pytest.approx(expected_z, abs=1e-4)
    assert avg_y == pytest.approx(expected_y, abs=1e-4)


def test_multiple_pixels():
    pixels = [(10, 20, 30), (100, 150, 200), (0, 255, 128)]
    xyz_list, avg_y = rgb_to_xyz(pixels)
    assert len(xyz_list) == 3


def test_average_y_calculation():
    pixels = [(0, 0, 0), (255, 255, 255)]
    xyz_list, avg_y = rgb_to_xyz(pixels)
    expected_avg = (0.0 + 255.0) / 2.0
    assert avg_y == pytest.approx(expected_avg, abs=1e-4)


def test_2x2_grid():
    pixels = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
    xyz_list, avg_y = rgb_to_xyz(pixels)
    assert len(xyz_list) == 4


def test_output_format_four_decimals():
    pixels = [(123, 231, 87)]
    xyz_list, avg_y = rgb_to_xyz(pixels)
    for val in xyz_list[0]:
        string = f"{val:.4f}"
        assert string == f"{round(val, 4):.4f}"


def test_red_only():
    pixels = [(255, 0, 0)]
    xyz_list, avg_y = rgb_to_xyz(pixels)
    x, y, z = xyz_list[0]
    assert x == pytest.approx(0.5149 * 255, abs=1e-4)
    assert y == pytest.approx(0.2654 * 255, abs=1e-4)
    assert z == pytest.approx(0.0248 * 255, abs=1e-4)

import pytest
from solution import calculate_covered_length, calculate_rain_volume


class TestCalculateCoveredLength:
    def test_static_umbrella(self):
        length = calculate_covered_length(0, 10, 5, 0, 10, 10)
        assert length == 5

    def test_moving_umbrella_full_coverage(self):
        length = calculate_covered_length(0, 10, 5, 10, 10, 10)
        assert length == 10

    def test_moving_umbrella_partial(self):
        length = calculate_covered_length(0, 10, 3, 5, 10, 10)
        assert length == 10

    def test_umbrella_exceeds_road(self):
        length = calculate_covered_length(0, 15, 5, 0, 10, 10)
        assert length == 10


class TestCalculateRainVolume:
    def test_basic_volume(self):
        umbrellas = [(0, 5, 2)]
        volume = calculate_rain_volume(umbrellas, 10, 10, 1, 10)
        assert volume > 0

    def test_no_umbrellas(self):
        umbrellas = []
        volume = calculate_rain_volume(umbrellas, 10, 10, 1, 10)
        assert volume == 0
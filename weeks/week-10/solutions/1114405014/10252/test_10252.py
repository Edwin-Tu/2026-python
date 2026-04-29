import unittest
from main_10252 import solve, find_min_distance_and_count

class TestUVA10252(unittest.TestCase):
    def test_basic(self):
        """測試基本案例"""
        points = [(0, 0), (1, 1), (2, 2)]
        min_dist, count = find_min_distance_and_count(points)
        self.assertEqual(min_dist, 4)
        self.assertEqual(count, 1)

    def test_single_point(self):
        """測試單一點"""
        points = [(5, 5)]
        min_dist, count = find_min_distance_and_count(points)
        self.assertEqual(min_dist, 0)
        self.assertEqual(count, 1)

    def test_two_points(self):
        """測試兩點"""
        points = [(0, 0), (0, 2)]
        min_dist, count = find_min_distance_and_count(points)
        self.assertEqual(min_dist, 2)
        self.assertEqual(count, 3)

    def test_collinear_points(self):
        """測試共線點"""
        points = [(0, 0), (1, 0), (2, 0)]
        min_dist, count = find_min_distance_and_count(points)
        self.assertEqual(min_dist, 2)
        self.assertEqual(count, 3)

if __name__ == '__main__':
    unittest.main()
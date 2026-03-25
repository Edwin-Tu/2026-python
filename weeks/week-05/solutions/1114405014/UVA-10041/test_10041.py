import unittest

from UVA_10041 import solve, min_total_distance


class TestMinTotalDistance(unittest.TestCase):
    def test_single_relative(self):
        self.assertEqual(min_total_distance([10]), 0)

    def test_two_relatives(self):
        self.assertEqual(min_total_distance([2, 4]), 2)

    def test_odd_count_addresses(self):
        self.assertEqual(min_total_distance([2, 4, 6]), 4)

    def test_even_count_addresses(self):
        self.assertEqual(min_total_distance([1, 2, 10, 20]), 27)

    def test_duplicate_addresses(self):
        self.assertEqual(min_total_distance([5, 5, 5]), 0)

    def test_duplicate_and_distinct_addresses(self):
        self.assertEqual(min_total_distance([1, 2, 2, 3]), 2)

    def test_unsorted_input(self):
        self.assertEqual(min_total_distance([10, 2, 6, 4]), 10)


class TestSolve(unittest.TestCase):
    def test_single_case(self):
        data = """1
3 2 4 6
"""
        expected = """4
"""
        self.assertEqual(solve(data), expected)

    def test_multiple_cases(self):
        data = """3
2 2 4
3 2 4 6
4 1 2 10 20
"""
        expected = """2
4
27
"""
        self.assertEqual(solve(data), expected)

    def test_case_with_duplicate_addresses(self):
        data = """2
3 5 5 5
4 1 2 2 3
"""
        expected = """0
2
"""
        self.assertEqual(solve(data), expected)


if __name__ == "__main__":
    unittest.main()
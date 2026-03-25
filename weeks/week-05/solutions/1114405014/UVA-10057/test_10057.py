import unittest
from UVA_10057 import analyze_password, solve


class TestAnalyzePassword(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(analyze_password([5]), (5, 1, 1))

    def test_odd_count(self):
        self.assertEqual(analyze_password([1, 2, 3, 4, 5]), (3, 1, 1))

    def test_even_count_single_value_range(self):
        self.assertEqual(analyze_password([1, 2, 3, 4]), (2, 2, 2))

    def test_large_range(self):
        self.assertEqual(analyze_password([1, 2, 3, 100]), (2, 2, 2))

    def test_duplicates(self):
        self.assertEqual(analyze_password([2, 2, 2, 2]), (2, 4, 1))

    def test_multiple_medians_with_duplicates(self):
        self.assertEqual(analyze_password([1, 2, 2, 3]), (2, 2, 1))


class TestSolve(unittest.TestCase):

    def test_single_case(self):
        data = """5
1 2 3 4 5
"""
        expected = """3 1 1
"""
        self.assertEqual(solve(data), expected)

    def test_multiple_cases(self):
        data = """4
1 2 3 4
4
2 2 2 2
"""
        expected = """2 2 2
2 4 1
"""
        self.assertEqual(solve(data), expected)


if __name__ == "__main__":
    unittest.main()
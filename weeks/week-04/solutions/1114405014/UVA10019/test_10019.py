import unittest
from UVA10019 import diff, solve


class TestUVA10019(unittest.TestCase):
    def test_diff_basic(self):
        self.assertEqual(diff(10, 12), 2)

    def test_diff_same_numbers(self):
        self.assertEqual(diff(100, 100), 0)

    def test_diff_reverse_order(self):
        self.assertEqual(diff(1000, 1), 999)

    def test_diff_large_numbers(self):
        self.assertEqual(diff(1234567890123, 1234567890000), 123)

    def test_solve_single_line(self):
        input_data = "10 12\n"
        expected = "2"
        self.assertEqual(solve(input_data).strip(), expected)

    def test_solve_multiple_lines(self):
        input_data = """10 12
10 14
100 200
"""
        expected = """2
4
100"""
        self.assertEqual(solve(input_data).strip(), expected)

    def test_solve_same_numbers(self):
        input_data = """5 5
999 999
"""
        expected = """0
0"""
        self.assertEqual(solve(input_data).strip(), expected)

    def test_solve_ignores_extra_spaces(self):
        input_data = """10   12
   100  90
"""
        expected = """2
10"""
        self.assertEqual(solve(input_data).strip(), expected)

    def test_solve_with_empty_lines(self):
        input_data = """

10 12

20 50

"""
        expected = """2
30"""
        self.assertEqual(solve(input_data).strip(), expected)


if __name__ == "__main__":
    unittest.main()
import unittest
from UVA10038 import is_jolly, solve


class TestUVA10038(unittest.TestCase):

    def test_jolly_basic(self):
        self.assertTrue(is_jolly([1, 4, 2, 3]))

    def test_not_jolly_duplicate_difference(self):
        self.assertFalse(is_jolly([1, 4, 2, -1, 6]))

    def test_not_jolly_missing_difference(self):
        self.assertFalse(is_jolly([1, 2, 4]))

    def test_single_element_is_jolly(self):
        self.assertTrue(is_jolly([10]))

    def test_two_elements_is_jolly(self):
        self.assertTrue(is_jolly([5, 6]))  # 差值為1

    def test_large_valid_jolly(self):
        self.assertTrue(is_jolly([1, 3, 2, 5, 4]))

    def test_large_invalid_jolly(self):
        self.assertFalse(is_jolly([1, 3, 5, 7, 9]))

    def test_solve_single_case(self):
        input_data = "4 1 4 2 3\n"
        expected = "Jolly"
        self.assertEqual(solve(input_data).strip(), expected)

    def test_solve_multiple_cases(self):
        input_data = """4 1 4 2 3
5 1 4 2 -1 6
"""
        expected = """Jolly
Not jolly"""
        self.assertEqual(solve(input_data).strip(), expected)

    def test_solve_multiple_lines_with_spaces(self):
        input_data = """1 10
3 1 2 4
"""
        expected = """Jolly
Not jolly"""
        self.assertEqual(solve(input_data).strip(), expected)


if __name__ == "__main__":
    unittest.main()
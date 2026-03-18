import unittest
from UVA10035 import count_carries, solve


class TestUVA10035(unittest.TestCase):

    def test_no_carry(self):
        self.assertEqual(count_carries("123", "456"), 0)

    def test_single_carry(self):
        self.assertEqual(count_carries("123", "594"), 1)

    def test_multiple_carries(self):
        self.assertEqual(count_carries("555", "555"), 3)

    def test_different_length(self):
        self.assertEqual(count_carries("1", "999"), 3)

    def test_with_zero(self):
        self.assertEqual(count_carries("0", "0"), 0)

    def test_solve_basic(self):
        input_data = """123 456
555 555
123 594
0 0
"""
        expected = """No carry operation.
3 carry operations.
1 carry operation."""
        self.assertEqual(solve(input_data).strip(), expected)

    def test_solve_with_single_carry_format(self):
        input_data = """1 9
0 0
"""
        expected = "1 carry operation."
        self.assertEqual(solve(input_data).strip(), expected)

    def test_solve_multiple_lines(self):
        input_data = """1 1
2 2
3 3
0 0
"""
        expected = """No carry operation.
No carry operation.
No carry operation."""
        self.assertEqual(solve(input_data).strip(), expected)


if __name__ == "__main__":
    unittest.main()
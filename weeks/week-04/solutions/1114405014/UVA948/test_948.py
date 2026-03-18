import unittest
from UVA948 import is_possible_fake, find_fake_coin, solve


class TestFakeCoin(unittest.TestCase):
    def test_equal_result_eliminates_coin_on_scale(self):
        weighings = [([1], [2], "=")]
        self.assertFalse(is_possible_fake(1, True, weighings))
        self.assertFalse(is_possible_fake(1, False, weighings))
        self.assertFalse(is_possible_fake(2, True, weighings))
        self.assertFalse(is_possible_fake(2, False, weighings))

    def test_single_unbalanced_weighing_has_multiple_candidates(self):
        weighings = [([1], [2], "<")]
        self.assertEqual(find_fake_coin(2, weighings), 0)

    def test_unique_fake_coin_can_be_found(self):
        weighings = [
            ([1], [2], "="),
            ([3], [4], "<"),
            ([3], [1], "<"),
        ]
        self.assertEqual(find_fake_coin(4, weighings), 3)

    def test_solve_output_format(self):
        input_data = """1

4 3
1 1 2
=
1 3 4
<
1 3 1
<
"""
        self.assertEqual(solve(input_data).strip(), "3")


if __name__ == "__main__":
    unittest.main()
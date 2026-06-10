"""數字根 — 測試檔

題目：digit_root(n) 反覆把 n 的各位數字相加，
直到剩一位數，回傳該一位數。

若 n < 1，應 raise ValueError("n must be >= 1")。
"""

import unittest

from digit_root import digit_root


class TestDigitRoot(unittest.TestCase):
    def test_basic_24_should_return_6(self):
        self.assertEqual(digit_root(24), 6)

    def test_basic_199_should_return_1(self):
        self.assertEqual(digit_root(199), 1)

    def test_edge_single_digit_should_return_itself(self):
        self.assertEqual(digit_root(5), 5)

    def test_large_number_should_return_digit_root(self):
        self.assertEqual(digit_root(2000000000), 2)

    def test_invalid_input_raises(self):
        with self.assertRaises(ValueError) as context:
            digit_root(0)

        self.assertEqual(str(context.exception), "n must be >= 1")


if __name__ == "__main__":
    unittest.main()
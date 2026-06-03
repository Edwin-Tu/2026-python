import unittest
from gcd import sum_of_gcd


class TestGCDBasic(unittest.TestCase):

    def test_n_2_should_return_1(self):
        self.assertEqual(sum_of_gcd(2), 1)


if __name__ == "__main__":
    unittest.main()
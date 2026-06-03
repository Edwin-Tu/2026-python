import unittest
from gcd import sum_of_gcd


class TestGCDEdgeCase(unittest.TestCase):

    def test_n_1_should_return_0(self):
        self.assertEqual(sum_of_gcd(1), 0)


if __name__ == "__main__":
    unittest.main()
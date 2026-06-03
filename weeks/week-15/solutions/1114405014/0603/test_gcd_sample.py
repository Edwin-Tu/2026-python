import unittest
from gcd import sum_of_gcd


class TestGCDSample(unittest.TestCase):

    def test_n_10_should_return_67(self):
        self.assertEqual(sum_of_gcd(10), 67)


if __name__ == "__main__":
    unittest.main()
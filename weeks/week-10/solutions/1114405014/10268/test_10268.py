import unittest
from main_10268 import solve, min_trials

class TestUVA10268(unittest.TestCase):
    def test_basic(self):
        """測試基本案例"""
        self.assertEqual(min_trials(2, 10), 4)
        self.assertEqual(min_trials(2, 100), 14)
        self.assertEqual(min_trials(10, 786599), 21)

    def test_single_egg(self):
        """測試只有一顆蛋"""
        self.assertEqual(min_trials(1, 10), 10)
        self.assertEqual(min_trials(1, 100), 100)

    def test_many_eggs(self):
        """測試很多蛋的情況"""
        self.assertEqual(min_trials(100, 1), 1)
        self.assertEqual(min_trials(100, 10), 4)

    def test_large_floors(self):
        """測試很多樓層"""
        result = min_trials(60, 1844674407370955161)
        self.assertEqual(result, "More than 63 trials needed.")

    def test_63_trials(self):
        """測試需要 63 次"""
        result = min_trials(63, 9223372036854775807)
        self.assertEqual(result, 63)

if __name__ == '__main__':
    unittest.main()
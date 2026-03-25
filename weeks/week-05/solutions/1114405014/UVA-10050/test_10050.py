import unittest
from UVA_10050 import count_hartals, solve


class TestHartals(unittest.TestCase):

    def test_single_party(self):
        # 每3天罷會，14天內 → 第3,6,9,12天
        # 6是Friday → 不算
        # → 3,9,12 → 共3天
        self.assertEqual(count_hartals(14, [3]), 3)

    def test_multiple_parties(self):
        # 範例題
        # 3,4,8 → 結果為5
        self.assertEqual(count_hartals(14, [3, 4, 8]), 5)

    def test_skip_weekends(self):
        # 每2天罷會 → 2,4,6,8,10...
        # 6,7 (Fri,Sat) 要跳過
        self.assertEqual(count_hartals(10, [2]), 4)

    def test_overlap_days(self):
        # 2與4 → 有重疊日
        self.assertEqual(count_hartals(10, [2, 4]), 4)

    def test_no_party(self):
        self.assertEqual(count_hartals(10, []), 0)


class TestSolve(unittest.TestCase):

    def test_single_case(self):
        data = """1
14
3
3
4
8
"""
        expected = """5
"""
        self.assertEqual(solve(data), expected)

    def test_multiple_cases(self):
        data = """2
14
3
3
4
8
10
1
2
"""
        expected = """5
4
"""
        self.assertEqual(solve(data), expected)


if __name__ == "__main__":
    unittest.main()
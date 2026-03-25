import unittest

from UVA_10056 import win_probability, solve


class TestWinProbability(unittest.TestCase):
    def test_single_player(self):
        # 只有一位玩家，最終一定會是他贏（只要 p > 0）
        self.assertAlmostEqual(win_probability(1, 0.25, 1), 1.0, places=10)

    def test_two_players_first_player(self):
        # n=2, p=0.5
        # 玩家1獲勝 = 0.5 + 0.5^2 * 0.5 + 0.5^4 * 0.5 + ...
        # = 0.5 / (1 - 0.25) = 2/3
        self.assertAlmostEqual(win_probability(2, 0.5, 1), 2 / 3, places=10)

    def test_two_players_second_player(self):
        # 玩家2獲勝 = 0.5 * 0.5 + 0.5^3 * 0.5 + ...
        # = 0.25 / (1 - 0.25) = 1/3
        self.assertAlmostEqual(win_probability(2, 0.5, 2), 1 / 3, places=10)

    def test_zero_probability(self):
        # 永遠不會成功，任何玩家獲勝機率都是 0
        self.assertAlmostEqual(win_probability(5, 0.0, 3), 0.0, places=10)

    def test_example_style_case(self):
        # 第 i 位玩家先在第 i 次出手成功，
        # 前 i-1 位都失敗，所以第一輪成功機率為 (1-p)^(i-1) * p
        # 之後每輪都乘上 (1-p)^n
        result = ((1 - 0.2) ** 2) * 0.2 / (1 - ((1 - 0.2) ** 3))
        self.assertAlmostEqual(win_probability(3, 0.2, 3), result, places=10)


class TestSolve(unittest.TestCase):
    def test_single_case(self):
        data = """1
2 0.5 1
"""
        expected = """0.6667
"""
        self.assertEqual(solve(data), expected)

    def test_multiple_cases(self):
        data = """3
1 0.25 1
2 0.5 2
5 0.0 3
"""
        expected = """1.0000
0.3333
0.0000
"""
        self.assertEqual(solve(data), expected)


if __name__ == "__main__":
    unittest.main()
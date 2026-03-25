import unittest

from UVA_10055 import flip_function, query_monotonicity, solve


class TestFunctionMonotonicity(unittest.TestCase):
    def test_initial_single_function_is_increasing(self):
        states = [0]  # 0 表示增函數，1 表示減函數
        self.assertEqual(query_monotonicity(states, 1, 1), 0)

    def test_flip_single_function_becomes_decreasing(self):
        states = [0]
        flip_function(states, 1)
        self.assertEqual(query_monotonicity(states, 1, 1), 1)

    def test_even_number_of_decreasing_functions_is_increasing(self):
        states = [0, 1, 1, 0]
        self.assertEqual(query_monotonicity(states, 1, 4), 0)

    def test_odd_number_of_decreasing_functions_is_decreasing(self):
        states = [0, 1, 0, 1, 1]
        self.assertEqual(query_monotonicity(states, 1, 5), 1)

    def test_subrange_query(self):
        states = [0, 1, 0, 1, 1]
        self.assertEqual(query_monotonicity(states, 2, 4), 0)

    def test_flip_twice_returns_to_original_state(self):
        states = [0, 0, 0]
        flip_function(states, 2)
        flip_function(states, 2)
        self.assertEqual(query_monotonicity(states, 1, 3), 0)


class TestSolve(unittest.TestCase):
    def test_single_query_without_flip(self):
        data = """1 1
2 1 1
"""
        expected = """0
"""
        self.assertEqual(solve(data), expected)

    def test_flip_then_query(self):
        data = """3 3
1 2
2 1 3
2 2 2
"""
        expected = """1
1
"""
        self.assertEqual(solve(data), expected)

    def test_multiple_flips_and_queries(self):
        data = """5 6
2 1 5
1 2
2 1 5
1 4
2 2 4
2 3 5
"""
        expected = """0
1
0
1
"""
        self.assertEqual(solve(data), expected)


if __name__ == "__main__":
    unittest.main()
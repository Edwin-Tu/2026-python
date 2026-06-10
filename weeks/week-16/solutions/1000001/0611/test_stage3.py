"""Stage 3 — baseline and optimized sorting tests."""

import unittest
from random import Random

from benchmark import SORT_FUNCTIONS, run_benchmark
from sorts import builtin_sort, quick_sort_optimized


SORT_FUNCTIONS_STAGE3 = [builtin_sort, quick_sort_optimized]


class TestStage3SortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        cases = [
            [3, 1, 2],
            [5, -1, 0, 5, 2],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
        ]

        for sort_func in SORT_FUNCTIONS_STAGE3:
            for data in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
                    self.assertEqual(sort_func(data), sorted(data))

    def test_edge_cases(self):
        cases = [
            [],
            [7],
            [2, 2, 2],
            [-3, -10, -1],
        ]

        for sort_func in SORT_FUNCTIONS_STAGE3:
            for data in cases:
                with self.subTest(sort_func=sort_func.__name__, data=data):
                    self.assertEqual(sort_func(data), sorted(data))

    def test_random_data_matches_builtin(self):
        rng = Random(42)
        cases = [
            [rng.randint(-100, 100) for _ in range(20)],
            [rng.randint(-1000, 1000) for _ in range(75)],
        ]

        for sort_func in SORT_FUNCTIONS_STAGE3:
            for data in cases:
                with self.subTest(sort_func=sort_func.__name__, size=len(data)):
                    self.assertEqual(sort_func(data), sorted(data))

    def test_input_not_mutated_and_returns_new_list(self):
        original = [3, 1, 2, 1]

        for sort_func in SORT_FUNCTIONS_STAGE3:
            with self.subTest(sort_func=sort_func.__name__):
                data = original.copy()
                result = sort_func(data)
                self.assertEqual(data, original)
                self.assertIsNot(result, data)

    def test_benchmark_includes_baseline_and_optimized_sort(self):
        sort_names = {sort_func.__name__ for sort_func in SORT_FUNCTIONS}

        self.assertIn("builtin_sort", sort_names)
        self.assertIn("quick_sort_optimized", sort_names)

        results = run_benchmark(sizes=(10,), repeats=1)
        self.assertIn("builtin_sort", results["algorithms"])
        self.assertIn("quick_sort_optimized", results["algorithms"])


if __name__ == "__main__":
    unittest.main()

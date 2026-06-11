import json
import os
import tempfile
import unittest

from benchmark import make_data, run_benchmark, save_results
from sorts import optimized_quick_sort


class TestBenchmark(unittest.TestCase):
    def test_make_data_is_deterministic_with_same_seed(self):
        data1 = make_data(10, seed=42)
        data2 = make_data(10, seed=42)

        self.assertEqual(data1, data2)
        self.assertEqual(len(data1), 10)

    def test_make_data_boundary_zero_size(self):
        data = make_data(0, seed=42)

        self.assertEqual(data, [])

    def test_optimized_quick_sort_correctness(self):
        cases = [
            [],
            [1],
            [3, 1, 2],
            [5, 5, 1, 3],
            [0, -1, 4, -3],
        ]

        for data in cases:
            with self.subTest(data=data):
                original = data.copy()
                result = optimized_quick_sort(data)

                self.assertEqual(result, sorted(original))
                self.assertEqual(data, original)
                self.assertIsNot(result, data)

    def test_run_benchmark_contains_required_algorithms_and_sizes(self):
        results = run_benchmark(sizes=(0, 1, 10), repeats=1)

        expected_algorithms = {
            "bubble_sort",
            "quick_sort",
            "merge_sort",
            "sorted",
            "optimized_quick_sort",
        }

        self.assertIsInstance(results, dict)
        self.assertTrue(expected_algorithms.issubset(results.keys()))

        for algorithm_name in expected_algorithms:
            with self.subTest(algorithm_name=algorithm_name):
                self.assertIn("0", results[algorithm_name])
                self.assertIn("1", results[algorithm_name])
                self.assertIn("10", results[algorithm_name])

                self.assertGreaterEqual(results[algorithm_name]["0"], 0)
                self.assertGreaterEqual(results[algorithm_name]["1"], 0)
                self.assertGreaterEqual(results[algorithm_name]["10"], 0)

    def test_save_results_creates_json_file(self):
        sample_results = {
            "bubble_sort": {"1": 0.001},
            "quick_sort": {"1": 0.001},
            "merge_sort": {"1": 0.001},
            "sorted": {"1": 0.001},
            "optimized_quick_sort": {"1": 0.001},
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = os.path.join(temp_dir, "results.json")

            save_results(sample_results, output_path)

            self.assertTrue(os.path.exists(output_path))
            self.assertGreater(os.path.getsize(output_path), 0)

            with open(output_path, "r", encoding="utf-8") as file:
                loaded = json.load(file)

            self.assertEqual(loaded, sample_results)


if __name__ == "__main__":
    unittest.main()
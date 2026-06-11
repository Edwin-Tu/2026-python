import tempfile
import unittest
from pathlib import Path

from benchmark import make_data, run_benchmark
from plot import plot_results


class TestSecurityValidation(unittest.TestCase):
    def test_make_data_rejects_negative_size(self):
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_run_benchmark_rejects_zero_repeats(self):
        with self.assertRaises(ValueError):
            run_benchmark(sizes=(10,), repeats=0)

    def test_run_benchmark_rejects_negative_size(self):
        with self.assertRaises(ValueError):
            run_benchmark(sizes=(-1,), repeats=1)

    def test_plot_results_rejects_empty_results(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "assets" / "benchmark.png"

            with self.assertRaises(ValueError):
                plot_results({}, output_path)

    def test_plot_results_rejects_results_without_data_points(self):
        results = {
            "quick_sort": {},
            "merge_sort": {},
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "assets" / "benchmark.png"

            with self.assertRaises(ValueError):
                plot_results(results, output_path)

    def test_plot_results_rejects_zero_or_negative_elapsed_time(self):
        results = {
            "quick_sort": {
                "10": 0.0,
                "100": -0.001,
            }
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "assets" / "benchmark.png"

            with self.assertRaises(ValueError):
                plot_results(results, output_path)

    def test_plot_results_rejects_non_numeric_size_key(self):
        results = {
            "quick_sort": {
                "small": 0.001,
            }
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "assets" / "benchmark.png"

            with self.assertRaises(ValueError):
                plot_results(results, output_path)


if __name__ == "__main__":
    unittest.main()
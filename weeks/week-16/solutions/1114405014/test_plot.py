import json
import os
import tempfile
import unittest
from pathlib import Path

import matplotlib

from plot import load_results, plot_results, main


class TestPlot(unittest.TestCase):
    def test_load_results_reads_json_file(self):
        sample_results = {
            "quick_sort": {
                "10": 0.0001,
                "100": 0.001,
            },
            "merge_sort": {
                "10": 0.0002,
                "100": 0.002,
            },
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = Path(temp_dir) / "results.json"

            with input_path.open("w", encoding="utf-8") as file:
                json.dump(sample_results, file)

            loaded = load_results(input_path)

            self.assertEqual(loaded, sample_results)

    def test_plot_results_creates_non_empty_png_file(self):
        sample_results = {
            "quick_sort": {
                "10": 0.0001,
                "100": 0.001,
            },
            "merge_sort": {
                "10": 0.0002,
                "100": 0.002,
            },
            "sorted": {
                "10": 0.00001,
                "100": 0.00005,
            },
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "assets" / "benchmark.png"

            plot_results(sample_results, output_path)

            self.assertTrue(output_path.exists())
            self.assertGreater(os.path.getsize(output_path), 0)

    def test_plot_results_boundary_single_algorithm_single_size(self):
        sample_results = {
            "quick_sort": {
                "1": 0.0001,
            },
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "assets" / "benchmark.png"

            plot_results(sample_results, output_path)

            self.assertTrue(output_path.exists())
            self.assertGreater(output_path.stat().st_size, 0)

    def test_main_reads_results_and_creates_output_png(self):
        sample_results = {
            "bubble_sort": {
                "10": 0.001,
                "100": 0.01,
            },
            "quick_sort": {
                "10": 0.0001,
                "100": 0.001,
            },
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = Path(temp_dir) / "results.json"
            output_path = Path(temp_dir) / "assets" / "benchmark.png"

            with input_path.open("w", encoding="utf-8") as file:
                json.dump(sample_results, file)

            main(input_path=input_path, output_path=output_path)

            self.assertTrue(output_path.exists())
            self.assertGreater(output_path.stat().st_size, 0)

    def test_load_results_missing_file_raises_file_not_found_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            missing_path = Path(temp_dir) / "missing_results.json"

            with self.assertRaises(FileNotFoundError):
                load_results(missing_path)

    def test_plot_uses_agg_backend(self):
        backend = matplotlib.get_backend().lower()

        self.assertEqual(backend, "agg")


if __name__ == "__main__":
    unittest.main()
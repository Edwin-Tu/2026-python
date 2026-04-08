import unittest
import subprocess


class Test10062(unittest.TestCase):
    """Test cases for UVA 10062 - Lost Cows"""

    def test_sample(self):
        """Sample input from problem"""
        input_data = "5\n1\n2\n1\n0\n"
        expected_output = "2\n4\n5\n3\n1\n"

        result = subprocess.run(
            ["python3", "/mnt/d/Edwin/program/program-python/2026-python/weeks/week-07/solutions/1114405014/10062/main.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), expected_output.strip())

    def test_small_n(self):
        """Test with N=2"""
        input_data = "2\n0\n"
        expected_output = "2\n1\n"

        result = subprocess.run(
            ["python3", "/mnt/d/Edwin/program/program-python/2026-python/weeks/week-07/solutions/1114405014/10062/main.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), expected_output.strip())

    def test_sorted_input(self):
        """Test already sorted (largest first in input)"""
        input_data = "5\n0\n0\n0\n0\n"
        expected_output = "5\n4\n3\n2\n1\n"

        result = subprocess.run(
            ["python3", "/mnt/d/Edwin/program/program-python/2026-python/weeks/week-07/solutions/1114405014/10062/main.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main()
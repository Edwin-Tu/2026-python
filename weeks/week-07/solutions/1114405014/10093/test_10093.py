import unittest
import subprocess


class Test10093(unittest.TestCase):
    """Test cases for UVA 10093 - The Battle of Phony War"""

    def test_sample(self):
        """Sample input from problem"""
        input_data = "3 10\nPPPPPPPPPP\nPPPPPPPPPP\nPPPPPPPPPP\n"
        expected_output = "7"

        result = subprocess.run(
            ["python3", "/mnt/d/Edwin/program/program-python/2026-python/weeks/week-07/solutions/1114405014/10093/main.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), expected_output.strip())

    def test_no_placement(self):
        """No plain cells"""
        input_data = "2 3\nHHH\nHHH\n"
        expected_output = "0"

        result = subprocess.run(
            ["python3", "/mnt/d/Edwin/program/program-python/2026-python/weeks/week-07/solutions/1114405014/10093/main.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), expected_output.strip())

    def test_single_row(self):
        """Single row"""
        input_data = "1 5\nPPPPP\n"
        expected_output = "2"

        result = subprocess.run(
            ["python3", "/mnt/d/Edwin/program/program-python/2026-python/weeks/week-07/solutions/1114405014/10093/main.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main()
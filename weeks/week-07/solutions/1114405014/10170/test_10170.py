import unittest
import subprocess


class Test10170(unittest.TestCase):
    """Test cases for UVA 10170 - The Hotel with Infinite Rooms"""

    def test_sample1(self):
        """Sample 1: S=4, D=1"""
        input_data = "4 1\n"
        expected_output = "4"

        result = subprocess.run(
            ["python3", "/mnt/d/Edwin/program/program-python/2026-python/weeks/week-07/solutions/1114405014/10170/main.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), expected_output.strip())

    def test_sample2(self):
        """Sample 2: S=3, D=4"""
        input_data = "3 4\n"
        expected_output = "4"

        result = subprocess.run(
            ["python3", "/mnt/d/Edwin/program/program-python/2026-python/weeks/week-07/solutions/1114405014/10170/main.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), expected_output.strip())

    def test_sample3(self):
        """Sample 3: S=3, D=5"""
        input_data = "3 5\n"
        expected_output = "4"

        result = subprocess.run(
            ["python3", "/mnt/d/Edwin/program/program-python/2026-python/weeks/week-07/solutions/1114405014/10170/main.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main()
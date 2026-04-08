import unittest
import subprocess


class Test10101(unittest.TestCase):
    """Test cases for UVA 10101 - Mad Counting / Bangla Numbers"""

    def test_sample1(self):
        """Sample 1"""
        input_data = "1+1=2#\n"
        expected_output = "1+1=2#"

        result = subprocess.run(
            ["python3", "/mnt/d/Edwin/program/program-python/2026-python/weeks/week-07/solutions/1114405014/10101/main.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), expected_output.strip())

    def test_no_solution(self):
        """No solution case - 1+2=4 can become 1+3=4 which is valid"""
        input_data = "1+2=4#\n"
        expected_output = "1+3=4#"

        result = subprocess.run(
            ["python3", "/mnt/d/Edwin/program/program-python/2026-python/weeks/week-07/solutions/1114405014/10101/main.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main()
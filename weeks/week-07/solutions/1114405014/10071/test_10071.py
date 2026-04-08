import unittest
import subprocess


class Test10071(unittest.TestCase):
    """Test cases for UVA 10071 - ABCDEF"""

    def test_sample1(self):
        """N=1, S={1} -> output 1 (single test case)"""
        input_data = "1\n1\n"
        expected_output = "1"

        result = subprocess.run(
            ["python3", "/mnt/d/Edwin/program/program-python/2026-python/weeks/week-07/solutions/1114405014/10071/main.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), expected_output.strip())

    def test_sample2(self):
        """N=2, S={2, 3} -> output 20 (a*b*c = d*e*f formula)"""
        input_data = "2\n2\n3\n"
        expected_output = "20"

        result = subprocess.run(
            ["python3", "/mnt/d/Edwin/program/program-python/2026-python/weeks/week-07/solutions/1114405014/10071/main.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), expected_output.strip())

    def test_sample3(self):
        """N=2, S={-1, 1} -> output 32 (a*b*c = d*e*f formula)"""
        input_data = "2\n-1\n1\n"
        expected_output = "32"

        result = subprocess.run(
            ["python3", "/mnt/d/Edwin/program/program-python/2026-python/weeks/week-07/solutions/1114405014/10071/main.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), expected_output.strip())

    def test_sample4(self):
        """N=3, S={5, 7, 10} -> output 93 (a*b*c = d*e*f formula)"""
        input_data = "3\n5\n7\n10\n"
        expected_output = "93"

        result = subprocess.run(
            ["python3", "/mnt/d/Edwin/program/program-python/2026-python/weeks/week-07/solutions/1114405014/10071/main.py"],
            input=input_data,
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main()
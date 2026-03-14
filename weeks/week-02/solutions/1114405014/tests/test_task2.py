import unittest

from task2_student_ranking import solve


class TestTask2StudentRanking(unittest.TestCase):
    def test_sample_case(self):
        input_text = "\n".join([
            "6 3",
            "amy 88 20",
            "bob 88 19",
            "zoe 92 21",
            "ian 88 19",
            "leo 75 20",
            "eva 92 20",
        ])
        expected = "\n".join([
            "eva 92 20",
            "zoe 92 21",
            "bob 88 19",
        ])
        self.assertEqual(solve(input_text), expected)

    def test_tie_break_by_age_then_name(self):
        input_text = "\n".join([
            "5 5",
            "zoe 90 20",
            "amy 90 19",
            "bob 90 19",
            "ian 90 21",
            "eva 90 19",
        ])
        expected = "\n".join([
            "amy 90 19",
            "bob 90 19",
            "eva 90 19",
            "zoe 90 20",
            "ian 90 21",
        ])
        self.assertEqual(solve(input_text), expected)

    def test_k_smaller_than_n(self):
        input_text = "\n".join([
            "4 2",
            "amy 70 20",
            "bob 95 21",
            "chris 85 19",
            "dora 95 20",
        ])
        expected = "\n".join([
            "dora 95 20",
            "bob 95 21",
        ])
        self.assertEqual(solve(input_text), expected)

    def test_k_zero(self):
        input_text = "\n".join([
            "3 0",
            "amy 80 20",
            "bob 90 21",
            "zoe 85 19",
        ])
        expected = ""
        self.assertEqual(solve(input_text), expected)

    def test_single_student(self):
        input_text = "\n".join([
            "1 1",
            "amy 88 20",
        ])
        expected = "amy 88 20"
        self.assertEqual(solve(input_text), expected)


if __name__ == "__main__":
    unittest.main()
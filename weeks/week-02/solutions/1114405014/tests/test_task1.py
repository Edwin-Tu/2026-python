import unittest

from task1_sequence_clean import solve


class TestTask1SequenceClean(unittest.TestCase):
    def test_normal_case(self):
        input_line = "5 3 5 2 9 2 8 3 1"
        expected = "\n".join([
            "dedupe: 5 3 2 9 8 1",
            "asc: 1 2 2 3 3 5 5 8 9",
            "desc: 9 8 5 5 3 3 2 2 1",
            "evens: 2 2 8"
        ])
        self.assertEqual(solve(input_line), expected)

    def test_empty_input(self):
        input_line = ""
        expected = "\n".join([
            "dedupe:",
            "asc:",
            "desc:",
            "evens:"
        ])
        self.assertEqual(solve(input_line), expected)

    def test_all_duplicates(self):
        input_line = "4 4 4 4"
        expected = "\n".join([
            "dedupe: 4",
            "asc: 4 4 4 4",
            "desc: 4 4 4 4",
            "evens: 4 4 4 4"
        ])
        self.assertEqual(solve(input_line), expected)

    def test_all_odds(self):
        input_line = "9 7 5 3 1 9 7"
        expected = "\n".join([
            "dedupe: 9 7 5 3 1",
            "asc: 1 3 5 7 7 9 9",
            "desc: 9 9 7 7 5 3 1",
            "evens:"
        ])
        self.assertEqual(solve(input_line), expected)

    def test_negative_numbers_and_zero(self):
        input_line = "0 -2 -2 3 4 -1 0"
        expected = "\n".join([
            "dedupe: 0 -2 3 4 -1",
            "asc: -2 -2 -1 0 0 3 4",
            "desc: 4 3 0 0 -1 -2 -2",
            "evens: 0 -2 -2 4 0"
        ])
        self.assertEqual(solve(input_line), expected)


if __name__ == "__main__":
    unittest.main()
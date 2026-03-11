import unittest


class TestTextRotation(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(rotate_text([]), [])

    def test_single_line(self):
        lines = ["ABC"]
        expected = ["C", "B", "A"]
        self.assertEqual(rotate_text(lines), expected)

    def test_two_lines_example(self):
        lines = ["HELLO", "WORLD"]
        expected = ["OW", "LR", "LD", "EL", "HO"]
        self.assertEqual(rotate_text(lines), expected)

    def test_single_character_lines(self):
        lines = ["A", "B", "C"]
        expected = ["C", "B", "A"]
        self.assertEqual(rotate_text(lines), expected)

    def test_uneven_lines(self):
        lines = ["AB", "CDE", "F"]
        expected = ["CF", "BE", "AD"]
        self.assertEqual(rotate_text(lines), expected)

    def test_with_spaces(self):
        lines = ["A B", "CD "]
        expected = ["CD", "A ", "B "]
        self.assertEqual(rotate_text(lines), expected)

    def test_special_characters(self):
        lines = ["A!1", "B@2"]
        expected = ["BA", "!@", "12"]
        self.assertEqual(rotate_text(lines), expected)

    def test_mixed_case(self):
        lines = ["AbC", "dEf"]
        expected = ["dA", "Eb", "Cf"]
        self.assertEqual(rotate_text(lines), expected)

    def test_max_dimensions(self):
        lines = ["A" * 100 for _ in range(100)]
        result = rotate_text(lines)

        self.assertEqual(len(result), 100)
        for line in result:
            self.assertEqual(len(line), 100)

        self.assertEqual(result[0], "A" * 100)


def rotate_text(lines):
    if not lines:
        return []

    max_length = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_length) for line in lines]

    result = []
    for col in range(max_length):
        row_chars = []
        for row in range(len(padded_lines)):
            row_chars.append(padded_lines[row][col])
        rotated_line = ''.join(row_chars[::-1]).rstrip()
        if rotated_line:
            result.append(rotated_line)

    return result


if __name__ == '__main__':
    unittest.main()
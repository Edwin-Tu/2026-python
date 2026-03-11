import unittest


class TestQuoteConverter(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(convert_quotes(""), "")

    def test_no_quotes(self):
        text = "Hello world without quotes"
        self.assertEqual(convert_quotes(text), text)

    def test_single_pair_quotes(self):
        text = '"Hello"'
        expected = '``Hello\'\''
        self.assertEqual(convert_quotes(text), expected)

    def test_multiple_pairs_quotes(self):
        text = '"First" and "Second"'
        expected = '``First\'\' and ``Second\'\''
        self.assertEqual(convert_quotes(text), expected)

    def test_complex_text_with_quotes(self):
        text = '"To be or not to be," quoth the bard, "that is the question."'
        expected = '``To be or not to be,\'\' quoth the bard, ``that is the question.\'\'' 
        self.assertEqual(convert_quotes(text), expected)

    def test_quotes_with_special_characters(self):
        text = '"Line 1\n" and "Line 2\t"'
        expected = '``Line 1\n\'\' and ``Line 2\t\'\''
        self.assertEqual(convert_quotes(text), expected)

    def test_quotes_in_quotes_not_nested(self):
        text = '"Outer" and "Inner" text'
        expected = '``Outer\'\' and ``Inner\'\' text'
        self.assertEqual(convert_quotes(text), expected)

    def test_even_number_quotes_guaranteed(self):
        text = '"One" "Two" "Three" "Four"'
        expected = '``One\'\' ``Two\'\' ``Three\'\' ``Four\'\''
        self.assertEqual(convert_quotes(text), expected)

    def test_process_lines(self):
        lines = [
            '"First line"',
            'Second line "with quotes"',
            'Third line'
        ]
        expected = [
            '``First line\'\'',
            'Second line ``with quotes\'\'',
            'Third line'
        ]
        result = [convert_quotes(line) for line in lines]
        self.assertEqual(result, expected)

    def test_backtick_and_apostrophe_preserved(self):
        text = "`Not a quote' and \"real quote\""
        expected = "`Not a quote' and ``real quote\'\'"
        self.assertEqual(convert_quotes(text), expected)


def convert_quotes(text):
    result = []
    quote_count = 0

    for char in text:
        if char == '"':
            if quote_count % 2 == 0:
                result.append('``')
            else:
                result.append('\'\'')
            quote_count += 1
        else:
            result.append(char)

    return ''.join(result)


if __name__ == '__main__':
    unittest.main()
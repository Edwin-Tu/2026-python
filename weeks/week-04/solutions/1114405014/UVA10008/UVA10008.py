import unittest
from UVA10008 import count_letters, format_output, solve


class TestUVA10008(unittest.TestCase):

    def test_count_letters_case_insensitive(self):
        """
        測試：大小寫是否被視為相同
        aA → A 出現 2 次
        """
        lines = ["aA bB cC"]
        expected = {
            "A": 2,
            "B": 2,
            "C": 2,
        }
        self.assertEqual(count_letters(lines), expected)

    def test_count_letters_ignores_non_letters(self):
        """
        測試：是否忽略非英文字母（數字、符號、空白）
        """
        lines = ["Hello, World! 123"]
        expected = {
            "H": 1,
            "E": 1,
            "L": 3,
            "O": 2,
            "W": 1,
            "R": 1,
            "D": 1,
        }
        self.assertEqual(count_letters(lines), expected)

    def test_count_letters_accumulates_multiple_lines(self):
        """
        測試：多行輸入是否會累加計算
        """
        lines = ["ABC", "aabbcc", "zzz"]
        expected = {
            "A": 3,
            "B": 3,
            "C": 3,
            "Z": 3,
        }
        self.assertEqual(count_letters(lines), expected)

    def test_format_output_sorted_by_frequency_desc_then_letter_asc(self):
        """
        測試：排序規則
        1. 先依出現次數由大到小
        2. 次數相同依字母順序排序
        """
        counter = {
            "B": 2,
            "A": 2,
            "C": 3,
        }
        expected = "C 3\nA 2\nB 2"
        self.assertEqual(format_output(counter), expected)

    def test_format_output_excludes_zero_count_letters(self):
        """
        測試：沒有出現的字母不應該被輸出
        """
        counter = {
            "A": 1,
            "C": 2,
        }
        output = format_output(counter)
        self.assertEqual(output, "C 2\nA 1")
        self.assertNotIn("B", output)  # B 不應該出現

    def test_solve_full_input_output(self):
        """
        測試：完整輸入輸出（整合測試）
        - 第一行為行數
        - 後面多行文字
        - 最後輸出排序結果
        """
        input_data = """3
This is a test.
Count me 123!
A a a b B
"""
        expected = """A 4
T 4
S 3
B 2
C 2
E 2
I 2
M 2
N 2
O 2
U 2
H 1"""
        self.assertEqual(solve(input_data).strip(), expected)


if __name__ == "__main__":
    unittest.main()
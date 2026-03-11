import unittest

# 測試驅動開發 (TDD) 策略：
# 1. 紅燈階段：先寫測試，讓測試失敗
# 2. 綠燈階段：實現功能，讓測試通過
# 3. 重構階段：優化代碼，保持測試通過

class TestQuoteConverter(unittest.TestCase):
    """
    測試 TeX 引號轉換功能
    根據題目 UVA 272，將普通雙引號轉換為有方向性雙引號
    """

    def test_empty_string(self):
        """測試空字串"""
        self.assertEqual(convert_quotes(""), "")

    def test_no_quotes(self):
        """測試沒有引號的文字"""
        text = "Hello world without quotes"
        self.assertEqual(convert_quotes(text), text)

    def test_single_pair_quotes(self):
        """測試單對引號"""
        text = '"Hello"'
        expected = '``Hello\'\''
        self.assertEqual(convert_quotes(text), expected)

    def test_multiple_pairs_quotes(self):
        """測試多對引號"""
        text = '"First" and "Second"'
        expected = '``First\'\' and ``Second\'\''
        self.assertEqual(convert_quotes(text), expected)

    def test_complex_text_with_quotes(self):
        """測試複雜文字包含引號"""
        text = '"To be or not to be," quoth the bard, "that is the question."'
        expected = '``To be or not to be,\'\' quoth the bard, ``that is the question.\'\''
        self.assertEqual(convert_quotes(text), expected)

    def test_quotes_with_special_characters(self):
        """測試引號與特殊字元"""
        text = '"Line 1\n" and "Line 2\t"'
        expected = '``Line 1\n\'\' and ``Line 2\t\'\''
        self.assertEqual(convert_quotes(text), expected)

    def test_quotes_in_quotes_not_nested(self):
        """測試題目保證不會有巢狀引號"""
        text = '"Outer" and "Inner" text'
        expected = '``Outer\'\' and ``Inner\'\' text'
        self.assertEqual(convert_quotes(text), expected)

    def test_even_number_quotes_guaranteed(self):
        """測試題目保證偶數個引號"""
        text = '"One" "Two" "Three" "Four"'
        expected = '``One\'\' ``Two\'\' ``Three\'\' ``Four\'\''
        self.assertEqual(convert_quotes(text), expected)

    def test_process_lines(self):
        """測試處理多行文字"""
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
        """測試 ` 和 ' 字元不被改變"""
        text = "`Not a quote' and \"real quote\""
        expected = "`Not a quote' and ``real quote\'\'"
        self.assertEqual(convert_quotes(text), expected)

# 以下是實現函數（在 TDD 中，這部分應該在測試通過後添加）
# 但為了完整性，先提供基本實現

def convert_quotes(text):
    """
    將普通雙引號轉換為 TeX 格式的有方向性雙引號
    第一個引號用 `` 代替，第二個用 '' 代替，交替進行
    """
    result = []
    quote_count = 0

    for char in text:
        if char == '"':
            if quote_count % 2 == 0:
                result.append('``')  # 第一個引號用 ``
            else:
                result.append('\'\'')  # 第二個引號用 ''
            quote_count += 1
        else:
            result.append(char)

    return ''.join(result)

if __name__ == '__main__':
    unittest.main()

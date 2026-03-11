import unittest

# 測試驅動開發 (TDD) 策略：
# 1. 紅燈階段：先寫測試，讓測試失敗
# 2. 綠燈階段：實現功能，讓測試通過
# 3. 重構階段：優化代碼，保持測試通過

class TestTextRotation(unittest.TestCase):
    """
    測試文字旋轉功能
    根據題目 UVA 490，將文字行順時針旋轉90度
    """

    def test_empty_input(self):
        """測試空輸入"""
        self.assertEqual(rotate_text([]), [])

    def test_single_line(self):
        """測試單行文字"""
        lines = ["ABC"]
        expected = ["C", "B", "A"]
        self.assertEqual(rotate_text(lines), expected)

    def test_two_lines_example(self):
        """測試題目範例：HELLO 和 WORLD"""
        lines = ["HELLO", "WORLD"]
        expected = ["OW", "LR", "LD", "EL", "HO"]
        self.assertEqual(rotate_text(lines), expected)

    def test_single_character_lines(self):
        """測試每行只有一個字元"""
        lines = ["A", "B", "C"]
        expected = ["C", "B", "A"]
        self.assertEqual(rotate_text(lines), expected)

    def test_uneven_lines(self):
        """測試長度不一的行"""
        lines = ["AB", "CDE", "F"]
        expected = ["CF", "BE", "AD"]
        self.assertEqual(rotate_text(lines), expected)

    def test_with_spaces(self):
        """測試包含空格的文字"""
        lines = ["A B", "CD "]
        expected = ["CD", "A ", "B "]
        self.assertEqual(rotate_text(lines), expected)

    def test_special_characters(self):
        """測試特殊字元"""
        lines = ["A!1", "B@2"]
        expected = ["BA", "!@", "12"]
        self.assertEqual(rotate_text(lines), expected)

    def test_mixed_case(self):
        """測試大小寫混合"""
        lines = ["AbC", "dEf"]
        expected = ["dA", "Eb", "Cf"]
        self.assertEqual(rotate_text(lines), expected)

    def test_max_dimensions(self):
        """測試最大尺寸：100行，每行100字元"""
        # 創建測試數據
        lines = ["A" * 100 for _ in range(100)]
        result = rotate_text(lines)

        # 驗證結果維度：應該有100行，每行100字元
        self.assertEqual(len(result), 100)
        for line in result:
            self.assertEqual(len(line), 100)

        # 驗證第一行應該都是最後一行的字元
        self.assertEqual(result[0], "A" * 100)

# 以下是實現函數（在 TDD 中，這部分應該在測試通過後添加）
# 但為了完整性，先提供基本實現

def rotate_text(lines):
    """
    將文字行順時針旋轉90度
    最後一行變成最左列，第一行變成最右列
    """
    if not lines:
        return []

    # 找到最長行的長度，用於填充
    max_length = max(len(line) for line in lines)

    # 將所有行填充到相同長度
    padded_lines = [line.ljust(max_length) for line in lines]

    # 創建旋轉後的結果
    result = []
    for col in range(max_length):
        # 從第一行開始，向下收集每一列的字元（順時針旋轉）
        row_chars = []
        for row in range(len(padded_lines)):
            row_chars.append(padded_lines[row][col])
        # 移除尾部空格並反轉順序
        rotated_line = ''.join(row_chars[::-1]).rstrip()
        if rotated_line:  # 只添加非空行
            result.append(rotated_line)

    return result

if __name__ == '__main__':
    unittest.main()

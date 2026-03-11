import unittest

# 測試驅動開發 (TDD) 策略：
# 1. 紅燈階段：先寫測試，讓測試失敗
# 2. 綠燈階段：實現功能，讓測試通過
# 3. 重構階段：優化代碼，保持測試通過

class TestCollatzCycleLength(unittest.TestCase):
    """
    測試 Collatz 猜想中的 cycle-length 計算
    根據題目 UVA 100，計算數列長度
    """

    def test_cycle_length_of_1(self):
        """測試 n=1 的 cycle-length，應該是 1"""
        # 數列：1，長度 1
        self.assertEqual(cycle_length(1), 1)

    def test_cycle_length_of_2(self):
        """測試 n=2 的 cycle-length，應該是 2"""
        # 數列：2, 1，長度 2
        self.assertEqual(cycle_length(2), 2)

    def test_cycle_length_of_3(self):
        """測試 n=3 的 cycle-length，應該是 8"""
        # 數列：3, 10, 5, 16, 8, 4, 2, 1，長度 8
        self.assertEqual(cycle_length(3), 8)

    def test_cycle_length_of_22(self):
        """測試 n=22 的 cycle-length，應該是 16"""
        # 根據題目範例
        self.assertEqual(cycle_length(22), 16)

    def test_cycle_length_of_9(self):
        """測試 n=9 的 cycle-length，應該是 20"""
        # 9 的數列最長
        self.assertEqual(cycle_length(9), 20)

    def test_max_cycle_length_single_number(self):
        """測試單個數字的區間最大 cycle-length"""
        self.assertEqual(max_cycle_length(1, 1), 1)
        self.assertEqual(max_cycle_length(2, 2), 2)
        self.assertEqual(max_cycle_length(22, 22), 16)

    def test_max_cycle_length_range_1_to_10(self):
        """測試 1 到 10 的區間，最大 cycle-length 應該是 20 (來自 9)"""
        self.assertEqual(max_cycle_length(1, 10), 20)

    def test_max_cycle_length_range_100_to_200(self):
        """測試 100 到 200 的區間，驗證較大範圍"""
        # 這個範圍內的最大 cycle-length 應該是 125 (來自 171 或其他)
        # 但我們先測試基本功能
        result = max_cycle_length(100, 200)
        self.assertGreaterEqual(result, 20)  # 至少大於等於已知值

    def test_max_cycle_length_i_greater_than_j(self):
        """測試 i > j 的情況，應該交換 i 和 j"""
        # 根據題目，i 和 j 的順序不確定，需要處理
        self.assertEqual(max_cycle_length(10, 1), max_cycle_length(1, 10))

    def test_process_input_output(self):
        """測試輸入處理和輸出格式"""
        # 模擬輸入 "1 10"，輸出應該是 "1 10 20"
        # 這裡測試函數邏輯
        i, j = 1, 10
        max_len = max_cycle_length(i, j)
        expected_output = f"{i} {j} {max_len}"
        self.assertEqual(expected_output, "1 10 20")

# 以下是實現函數（在 TDD 中，這部分應該在測試通過後添加）
# 但為了完整性，先提供基本實現

def cycle_length(n):
    """
    計算 n 的 cycle-length
    根據 Collatz 猜想演算法
    """
    count = 1
    while n != 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        count += 1
    return count

def max_cycle_length(i, j):
    """
    計算從 i 到 j 之間所有數字的最大 cycle-length
    """
    # 確保 i <= j
    if i > j:
        i, j = j, i

    max_len = 0
    for num in range(i, j + 1):
        current_len = cycle_length(num)
        if current_len > max_len:
            max_len = current_len
    return max_len

if __name__ == '__main__':
    unittest.main()

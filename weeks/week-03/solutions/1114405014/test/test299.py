import unittest

# 測試驅動開發 (TDD) 策略：
# 1. 紅燈階段：先寫測試，讓測試失敗
# 2. 綠燈階段：實現功能，讓測試通過
# 3. 重構階段：優化代碼，保持測試通過

class TestTrainSwapping(unittest.TestCase):
    """
    測試火車車廂排序問題
    根據題目 UVA 299，計算最少交換相鄰車廂的次數
    """

    def test_already_sorted(self):
        """測試已經排序好的車廂"""
        # 車廂已經是 1,2,3,... 順序，不需要交換
        self.assertEqual(count_swaps([1, 2, 3]), 0)
        self.assertEqual(count_swaps([1]), 0)

    def test_reverse_sorted(self):
        """測試完全反向排序的車廂"""
        # 3,2,1 需要交換 3 次 (氣泡排序的交換次數)
        self.assertEqual(count_swaps([3, 2, 1]), 3)
        # 4,3,2,1 需要交換 6 次
        self.assertEqual(count_swaps([4, 3, 2, 1]), 6)

    def test_single_swap_needed(self):
        """測試只需要一次交換的情況"""
        # 1,3,2 -> 交換一次得到 1,2,3
        self.assertEqual(count_swaps([1, 3, 2]), 1)
        # 2,1,3 -> 交換一次得到 1,2,3
        self.assertEqual(count_swaps([2, 1, 3]), 1)

    def test_multiple_swaps_needed(self):
        """測試需要多次交換的情況"""
        # 2,3,1 -> 需要 2 次交換
        self.assertEqual(count_swaps([2, 3, 1]), 2)
        # 3,1,2 -> 需要 2 次交換
        self.assertEqual(count_swaps([3, 1, 2]), 2)

    def test_complex_case(self):
        """測試複雜的排列情況"""
        # 測試一個更複雜的例子
        self.assertEqual(count_swaps([4, 2, 3, 1]), 5)

    def test_empty_train(self):
        """測試空火車（長度為0）"""
        self.assertEqual(count_swaps([]), 0)

    def test_two_cars(self):
        """測試只有兩個車廂的情況"""
        self.assertEqual(count_swaps([1, 2]), 0)  # 已排序
        self.assertEqual(count_swaps([2, 1]), 1)  # 需要交換

    def test_sample_input(self):
        """測試題目可能的樣本輸入"""
        # 根據題目描述的場景
        self.assertEqual(count_swaps([1, 3, 2]), 1)
        self.assertEqual(count_swaps([3, 2, 1]), 3)

    def test_max_length(self):
        """測試最大長度 L=50 的情況"""
        # 創建一個反向排序的 50 個車廂
        reverse_50 = list(range(50, 0, -1))
        # 逆序對數量 = n*(n-1)/2 = 50*49/2 = 1225
        self.assertEqual(count_swaps(reverse_50), 1225)

# 以下是實現函數（在 TDD 中，這部分應該在測試通過後添加）
# 但為了完整性，先提供基本實現

def count_swaps(train):
    """
    計算將火車車廂排序到 1,2,3,... 順序所需的最少相鄰交換次數
    使用氣泡排序的交換次數計算，等於逆序對的數量
    """
    if not train:
        return 0

    # 複製列表避免修改原列表
    cars = train[:]
    swaps = 0

    # 使用氣泡排序計算交換次數
    n = len(cars)
    for i in range(n):
        for j in range(0, n-i-1):
            if cars[j] > cars[j+1]:
                # 交換相鄰元素
                cars[j], cars[j+1] = cars[j+1], cars[j]
                swaps += 1

    return swaps

if __name__ == '__main__':
    unittest.main()

# 8 容器操作與推導式範例
# 本範例展示 Python 中常用的容器操作技巧，包括清單推導式、字典推導式與生成器表達式

# 建立一個包含正負數字的清單
nums = [1, -2, 3, -4]

# 清單推導式（List Comprehension）
# 語法：[表達式 for 項目 in 可疊代物件 if 條件]
# 用途：從 nums 中篩選所有正數，建立新的清單
# 結果：[1, 3]
positives = [n for n in nums if n > 0]

# 建立一組元組配對，每個元組包含字母與數字
pairs = [('a', 1), ('b', 2)]

# 字典推導式（Dictionary Comprehension）
# 語法：{鍵: 值 for 項目 in 可疊代物件}
# 用途：將 pairs 轉換為字典結構，方便透過鍵快速查詢對應的值
# 結果：{'a': 1, 'b': 2}
lookup = {k: v for k, v in pairs}

# 生成器表達式（Generator Expression）
# 語法：(表達式 for 項目 in 可疊代物件)
# 用途：計算 nums 中所有數字的平方和
# 特色：使用小括號，不會立即產生完整清單，節省記憶體，適合大量資料處理
# 計算過程：1² + (-2)² + 3² + (-4)² = 1 + 4 + 9 + 16 = 30
squares_sum = sum(n * n for n in nums)

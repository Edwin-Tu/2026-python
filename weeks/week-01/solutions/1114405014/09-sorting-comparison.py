# 9 比較、排序與 key 函式範例
# 本範例展示 Python 中的比較運算、排序機制以及 key 函式的使用方式

# 比較運算（tuple 逐一比較）
# 建立兩個元組進行比較
a = (1, 2)
b = (1, 3)

# 元組比較規則：從第一個元素開始逐一比較，直到找到不相等的元素
# 此處 a[0] == b[0] == 1，相等所以繼續比較下一個元素
# a[1] == 2 < b[1] == 3，因此 a < b 結果為 True
result = a < b

# key 排序
# 建立一個包含多個字典的清單，每個字典有 uid 欄位
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]

# sorted() 函式搭配 key 參數
# key 參數指定一個函式，用於從每個元素中提取比較用的關鍵值
# 此處使用 lambda 匿名函式，指定以 'uid' 的值作為排序依據
# 結果：{'uid': 1}、{'uid': 2}、{'uid': 3}（依 uid 由小到大排列）
rows_sorted = sorted(rows, key=lambda r: r['uid'])

# min/max 搭配 key
# min() 與 max() 函式同樣支援 key 參數
# 此處找出 rows 中 uid 值最小的字典
# 結果：{'uid': 1}
smallest = min(rows, key=lambda r: r['uid'])

# U6. defaultdict 為何比手動初始化乾淨（1.6）

# 從 collections 模組匯入 defaultdict
# defaultdict 可以在 key 不存在時，自動建立預設值
from collections import defaultdict

# 原始資料：每個元素都是 (key, value)
pairs = [('a', 1), ('a', 2), ('b', 3)]

# ----------------------------
# 手動版：一直判斷 key 是否存在
# ----------------------------

# 建立普通字典
d = {}

# 逐筆處理 pairs
for k, v in pairs:
    # 如果 key 還沒出現過，就先建立一個空串列
    if k not in d:
        d[k] = []
    
    # 再把 value 加進對應的串列
    d[k].append(v)

# 印出手動版結果
print("手動初始化的結果：", d)


# ----------------------------
# defaultdict 版：省掉初始化分支
# ----------------------------

# 建立 defaultdict(list)
# 當新 key 第一次出現時，會自動建立空串列 []
d2 = defaultdict(list)

# 逐筆處理 pairs
for k, v in pairs:
    # 不需要先判斷 key 是否存在
    # 因為 d2[k] 如果不存在，會自動變成 []
    d2[k].append(v)

# 印出 defaultdict 結果
print("defaultdict 的結果：", d2)

# 如果想看起來像普通 dict，也可以轉型後再印
print("轉成一般 dict 後：", dict(d2))
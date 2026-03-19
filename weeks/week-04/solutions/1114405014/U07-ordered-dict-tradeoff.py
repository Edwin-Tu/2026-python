# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）

# 從 collections 模組匯入 OrderedDict
# OrderedDict 是「有順序的字典」
from collections import OrderedDict

# 建立一個 OrderedDict
d = OrderedDict()

# 依序加入資料
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3

# 印出整個 OrderedDict
print("OrderedDict 內容：", d)

# 逐項印出 key 和 value，觀察順序
print("依插入順序輸出：")
for key, value in d.items():
    print(key, value)
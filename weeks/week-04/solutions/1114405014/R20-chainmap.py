# R20. ChainMap 合併映射（1.20）

# 從 collections 模組匯入 ChainMap
# ChainMap 可以把多個字典「串起來」當成一個字典來使用
from collections import ChainMap

# 建立第一個字典
a = {'x': 1, 'z': 3}

# 建立第二個字典
b = {'y': 2, 'z': 4}

# 使用 ChainMap 將 a 和 b 合併
# 注意：不是建立新字典複製資料，而是把多個字典串接起來查看
c = ChainMap(a, b)

# 印出原始字典
print("字典 a：", a)
print("字典 b：", b)

# 印出 ChainMap 物件
print("ChainMap c：", c)

# 取出鍵 'x'
# 因為 'x' 在 a 中存在，所以會得到 a 裡的值 1
print("c['x'] =", c['x'])

# 取出鍵 'y'
# 因為 'y' 不在 a 中，但在 b 中存在，所以會得到 b 裡的值 2
print("c['y'] =", c['y'])

# 取出鍵 'z'
# 因為 a 和 b 都有 'z'
# ChainMap 會優先找前面的字典，所以會先取到 a 的 z，也就是 3
print("c['z'] =", c['z'])  # 取到 a 的 z

# 額外示範：查看 ChainMap 中所有映射來源
print("ChainMap 內部的 maps：", c.maps)
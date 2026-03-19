# U8. 字典最值為何常用 zip(values, keys)（1.8）

# 建立一個價格字典
# key 是商品名稱，value 是價格
prices = {'A': 2.0, 'B': 1.0}

# 直接對字典使用 min()
# 預設只會比較 key，也就是字母大小
result1 = min(prices)

# 印出結果
print("min(prices) 的結果：", result1)

# 只對 values() 使用 min()
# 可以找到最小價格，但不知道是哪一個 key 對應到這個價格
result2 = min(prices.values())

# 印出結果
print("min(prices.values()) 的結果：", result2)

# 使用 zip(prices.values(), prices.keys())
# 會把 value 和 key 配對成 tuple：
# (2.0, 'A'), (1.0, 'B')
# 這樣 min() 會先比較 tuple 的第一個元素，也就是 value
# 因此可以同時得到「最小 value」和「對應的 key」
result3 = min(zip(prices.values(), prices.keys()))

# 印出結果
print("min(zip(prices.values(), prices.keys())) 的結果：", result3)
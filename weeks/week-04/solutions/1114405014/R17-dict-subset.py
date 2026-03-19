# R17. 字典子集（1.17）

# 建立一個股價字典
# key 是股票代號，value 是股價
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55
}

# 使用字典推導式，篩選出股價大於 200 的項目
# 會建立一個新的字典 p1
p1 = {k: v for k, v in prices.items() if v > 200}

# 印出原始字典
print("原始股價字典：", prices)

# 印出股價大於 200 的子字典
print("股價大於 200 的項目：", p1)

# 建立一個集合，表示科技股名稱
tech_names = {'AAPL', 'IBM'}

# 使用字典推導式，篩選出 key 在 tech_names 集合中的項目
# 會建立一個新的字典 p2
p2 = {k: v for k, v in prices.items() if k in tech_names}

# 印出科技股名稱集合
print("科技股名稱集合：", tech_names)

# 印出符合科技股名稱的子字典
print("屬於科技股的項目：", p2)
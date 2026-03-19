# R19. 轉換+聚合：生成器表達式（1.19）

# 建立一個數字串列
nums = [1, 2, 3]

# 使用生成器表達式計算每個數字的平方，再用 sum() 加總
# 1*1 + 2*2 + 3*3 = 1 + 4 + 9 = 14
result1 = sum(x * x for x in nums)

# 印出平方和結果
print("平方和：", result1)


# 建立一個 tuple，內容包含字串、整數、浮點數
s = ('ACME', 50, 123.45)

# 使用生成器表達式先將每個元素轉成字串
# 再用逗號把它們串接起來
result2 = ','.join(str(x) for x in s)

# 印出串接結果
print("串接後的字串：", result2)


# 建立一個投資組合串列
# 每個元素都是字典，包含公司名稱與持有股數
portfolio = [
    {'name': 'AOL', 'shares': 20},
    {'name': 'YHOO', 'shares': 75}
]

# 使用生成器表達式取出每個字典中的 shares
# 再找出最小的股數
result3 = min(s['shares'] for s in portfolio)

# 印出最小股數
print("最小股數：", result3)

# 直接在整個字典資料中找 shares 最小的那一筆資料
# key=lambda s: s['shares'] 表示比較時依 shares 欄位判斷
result4 = min(portfolio, key=lambda s: s['shares'])

# 印出 shares 最小的整筆資料
print("股數最少的資料：", result4)
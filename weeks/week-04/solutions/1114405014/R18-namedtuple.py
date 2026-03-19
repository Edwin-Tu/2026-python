# R18. namedtuple（1.18）

# 從 collections 模組匯入 namedtuple
# namedtuple 可以建立「有名稱欄位」的 tuple
from collections import namedtuple

# 建立 Subscriber 類別
# 欄位有 addr（地址）與 joined（加入日期）
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

# 建立一筆 Subscriber 資料
sub = Subscriber('jonesy@example.com', '2012-10-19')

# 印出整個 sub
print("Subscriber 資料：", sub)

# 取出 addr 欄位並印出
print("訂閱者信箱：", sub.addr)

# 取出 joined 欄位並印出
print("加入日期：", sub.joined)

# 建立 Stock 類別
# 欄位有 name（股票名稱）、shares（股數）、price（價格）
Stock = namedtuple('Stock', ['name', 'shares', 'price'])

# 建立一筆股票資料
s = Stock('ACME', 100, 123.45)

# 印出原本的股票資料
print("原本的 Stock 資料：", s)

# 使用 _replace() 建立一個新的 namedtuple
# 將 shares 從 100 改成 75
# 注意：namedtuple 本身不可直接修改，所以 _replace() 會回傳新物件
s = s._replace(shares=75)

# 印出修改後的股票資料
print("修改後的 Stock 資料：", s)

# 分別印出各欄位內容
print("股票名稱：", s.name)
print("股數：", s.shares)
print("價格：", s.price)
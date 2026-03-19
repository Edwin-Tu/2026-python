# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）

# 建立一個 tuple
# 內容只有姓名和 email，沒有電話
record = ('Dave', 'dave@example.com')

# 使用星號解包
# name 會接到第一個元素
# email 會接到第二個元素
# *phones 會接收「剩下所有元素」
# 即使沒有剩餘元素，phones 仍然會是一個空的 list
name, email, *phones = record

# 印出原始資料
print("record 的內容：", record)

# 印出解包後的結果
print("name =", name)
print("email =", email)
print("phones =", phones)

# 額外印出 phones 的資料型態
print("phones 的型態是：", type(phones))
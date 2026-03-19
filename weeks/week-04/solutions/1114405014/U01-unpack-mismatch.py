# U1. 解包失敗的原因：變數數量 ≠ 元素數量（1.1）

# 建立一個 tuple，裡面有 2 個元素
p = (4, 5)

# 先印出原始 tuple
print("p 的內容：", p)

# 正確示範：
# 因為 p 裡面有 2 個元素，所以要用 2 個變數來接
x, y = p

# 印出正確解包後的結果
print("正確解包後：")
print("x =", x)
print("y =", y)

# 錯誤示範：
# p 只有 2 個元素，但右邊卻想用 3 個變數來接
# 這樣會造成 ValueError
try:
    x, y, z = p
except ValueError as e:
    # 印出錯誤訊息
    print("發生錯誤：", e)
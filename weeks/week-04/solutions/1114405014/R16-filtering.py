# R16. 過濾：推導式 / generator / filter / compress（1.16）

# 原始串列
mylist = [1, 4, -5, 10]

# 使用串列推導式過濾出大於 0 的數字
# 結果會直接產生一個新的串列
positive_list = [n for n in mylist if n > 0]

# 印出串列推導式的結果
print("串列推導式結果：", positive_list)

# 使用生成器表達式過濾出大於 0 的數字
# 不會一次把所有資料都建立好，而是要用的時候才一個一個取出
pos = (n for n in mylist if n > 0)

# 將生成器轉成串列後輸出，方便觀察內容
print("生成器轉成串列後的結果：", list(pos))

# 含有數字字串、符號、無效資料的串列
values = ['1', '2', '-3', '-', 'N/A']

# 定義一個函式，判斷字串是否可以轉成整數
def is_int(val):
    try:
        # 嘗試把字串轉成整數
        int(val)
        return True
    except ValueError:
        # 如果轉換失敗，表示它不是整數格式
        return False

# 使用 filter 搭配 is_int 函式
# 只保留可以成功轉成整數的元素
int_values = list(filter(is_int, values))

# 印出過濾後的結果
print("filter 過濾後的整數字串：", int_values)

# 匯入 compress：可依照布林條件篩選對應位置的元素
from itertools import compress

# 地址資料
addresses = ['a1', 'a2', 'a3']

# 對應的數量資料
counts = [0, 3, 10]

# 建立布林條件串列
# 判斷每個 counts 元素是否大於 5
# 結果會是 [False, False, True]
more5 = [n > 5 for n in counts]

# 先印出布林條件，方便觀察
print("是否大於 5 的判斷結果：", more5)

# 使用 compress 根據 more5 的 True / False 來過濾 addresses
# 只有對應到 True 的元素會被保留下來
result = list(compress(addresses, more5))

# 印出 compress 的結果
print("compress 篩選後的地址：", result)
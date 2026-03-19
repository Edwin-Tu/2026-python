# 匯入 textwrap 模組：用來處理長字串換行排版
import textwrap

# 建立一個前後含有空白與換行符號的字串
s = "  hello world \n"

# strip()：移除字串左右兩側的空白與換行
print(repr(s.strip()))

# lstrip()：只移除字串左側的空白
print(repr(s.lstrip()))

# strip("-=")：移除字串左右兩側的 - 或 =
# 注意：只會移除頭尾，不會移除中間
print("-----hello=====".strip("-="))

# 建立一般文字
text = "Hello World"

# ljust(20)：靠左對齊，總長度補到 20
print(text.ljust(20))

# rjust(20)：靠右對齊，總長度補到 20
print(text.rjust(20))

# center(20, "*")：置中對齊，總長度補到 20，空位用 * 補
print(text.center(20, "*"))

# format(text, "^20")：使用 format 做置中對齊，總長度 20
# ^ 代表置中
print(format(text, "^20"))

# format(1.2345, ">10.2f")：
# > 代表靠右對齊
# 10 代表總寬度 10
# .2f 代表保留小數點後 2 位
print(format(1.2345, ">10.2f"))

# 建立字串清單
parts = ["Is", "Chicago", "Not", "Chicago?"]

# 用空白把串列中的元素連接起來
print(" ".join(parts))

# 用逗號把串列中的元素連接起來
print(",".join(parts))

# 建立包含不同型態資料的清單
data = ["ACME", 50, 91.1]

# join() 只能串接字串，所以要先把每個元素轉成 str
print(",".join(str(d) for d in data))

# 建立變數
name, n = "Guido", 37

# 使用格式化字串模板
s = "{name} has {n} messages."

# 用 format() 帶入指定變數
print(s.format(name=name, n=n))

# format_map(vars())：vars() 會取得目前變數名稱與值的字典
# 可直接把目前作用域中的變數帶入
print(s.format_map(vars()))

# f-string：更直觀的字串格式化寫法
print(f"{name} has {n} messages.")

# 建立長字串
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)

# textwrap.fill(long_s, 40)：
# 將長字串自動換行，每行寬度最多 40 個字元
print(textwrap.fill(long_s, 40))

# initial_indent="    "：
# 第一行前面加上 4 個空白縮排
print(textwrap.fill(long_s, 40, initial_indent="    "))
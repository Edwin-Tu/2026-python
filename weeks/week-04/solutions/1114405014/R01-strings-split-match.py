# 匯入 re 模組：用來做正規表示式處理
import re

# 匯入 fnmatch、fnmatchcase：用來做萬用字元樣式比對
from fnmatch import fnmatch, fnmatchcase

# 原始字串，內含空白、分號、逗號等不同分隔符號
line = "asdf fjdk; afed, fjek,asdf, foo"

# 使用 re.split() 搭配正規表示式來切割字串
# [;,\s] 表示遇到分號、逗號或空白都可以切開
# \s* 表示分隔符號後面如果有 0 個以上空白，也一起忽略
print(re.split(r"[;,\s]\s*", line))

# 使用另一種寫法來切割字串
# (?:,|;|\s) 表示「逗號 或 分號 或 空白」
# ?: 代表這是一個非捕獲群組，只做分組，不保留結果
# 功能與上面類似，也是把不同分隔符號都當成切割依據
print(re.split(r"(?:,|;|\s)\s*", line))

# 建立一個檔名字串
filename = "spam.txt"

# 判斷檔名是否以 .txt 結尾
print(filename.endswith(".txt"))

# 判斷檔名是否以 file: 開頭
print(filename.startswith("file:"))

# 建立一組檔名清單
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]

# 使用串列推導式篩選出副檔名是 .c 或 .h 的檔案
# endswith() 可以一次接受 tuple，表示符合其中任一結尾即可
print([name for name in filenames if name.endswith((".c", ".h"))])

# fnmatch() 用萬用字元樣式比對字串
# *.txt 表示任意名稱，但副檔名必須是 .txt
print(fnmatch("foo.txt", "*.txt"))

# Dat[0-9]* 表示：
# Dat 開頭，後面接一個數字，再接任意字元
print(fnmatch("Dat45.csv", "Dat[0-9]*"))

# fnmatchcase() 與 fnmatch() 類似，但會區分大小寫
# 這裡 foo.txt 不符合 *.TXT，因為 txt 和 TXT 大小寫不同
print(fnmatchcase("foo.txt", "*.TXT"))

# 建立地址清單
addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]

# 使用 fnmatchcase() 篩選出以 " ST" 結尾的地址
# * ST 表示前面可以是任意字元，但最後必須是空白加 ST
print([a for a in addresses if fnmatchcase(a, "* ST")])
# 匯入 re 模組：用來做正規表示式處理
import re

# 建立位元組資料（bytes）
# 前面加 b 表示這不是一般字串，而是 bytes
data = b"Hello World"

# 切片操作：取出索引 0 到 4 的內容
# 結果仍然是 bytes
print(data[0:5])

# 判斷 data 是否以 b"Hello" 開頭
# bytes 也可以使用 startswith()
print(data.startswith(b"Hello"))

# 依照空白切開 bytes
# 回傳值會是由 bytes 組成的 list
print(data.split())

# 將 bytes 中的 b"Hello" 替換成 b"Hello Cruel"
# 注意：替換時前後都要用 bytes 格式
print(data.replace(b"Hello", b"Hello Cruel"))

# 建立另一組 bytes 資料
raw = b"FOO:BAR,SPAM"

# 使用正規表示式分割 bytes
# rb"[:,]" 表示 bytes 版本的 raw string
# [:,] 表示遇到冒號或逗號就切開
print(re.split(rb"[:,]", raw))

# 建立一般字串
a = "Hello"

# 建立 bytes
b = b"Hello"

# 一般字串取索引時，回傳的是字元
print(a[0])

# bytes 取索引時，回傳的是整數（ASCII 編碼值）
# 例如 b'H' 的值是 72
print(b[0])

# 先用 format() 建立格式化字串
# {:10s} 表示字串欄位寬度為 10
# {:10d} 表示整數欄位寬度為 10
# 之後再用 encode("ascii") 轉成 bytes
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")

# 印出轉成 bytes 後的結果
print(formatted)
# R04. 十六進位與 Base64 編碼解碼（6.9–6.10）
# 主題：binascii / base64 / bytes.hex() / bytes.fromhex()
# 這兩種編碼方式都是將二進位資料轉換為可列印（printable）的字元
# 注意：編碼 ≠ 加密，兩者都不提供安全性

# 匯入 binascii 模組，提供二進位與 ASCII 之間的轉換
import binascii
# 匯入 base64 模組，提供 Base64 編碼解碼
import base64

# ── 6.9 十六進位（Hex）────────────────────────────────────────────────
# 二進位資料，b 前綴表示 bytes 型別
# \xe4\xb8\x96\xe7\x95\x8c 是「世界」兩個字的 UTF-8 編碼
data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"   # "Hello, 世界"

# 方法一：binascii.b2a_hex() 將 bytes 轉為 hex 字串
# b2a = binary to ASCII，回傳值型別是 bytes（內容為十六進位字元）
hex_str = binascii.b2a_hex(data)
# 輸出為 b'48656c6c6f2c20e4b896e7958c'
# 每個位元組轉為兩個十六進位字元（0-9, a-f）
print("b2a_hex：", hex_str)

# 方法二：bytes.hex() 是 Python 3.5+ 的內建方法
# 更直觀、不需要 import binascii
hex_str2 = data.hex()
print(".hex()：", hex_str2)

# 反向操作：binascii.a2b_hex() 將 hex 字串轉回 bytes
# a2b = ASCII to binary
restored = binascii.a2b_hex(hex_str)
print("a2b_hex：", restored)

# 另一種方式：bytes.fromhex() 類別方法，Python 3.5+
restored2 = bytes.fromhex(hex_str2)
print("fromhex：", restored2)

# assert 確認還原後的資料與原始資料一致
# 如果不相等會拋出 AssertionError
assert restored == data     # 確認一致

# ── 6.10 Base64 ───────────────────────────────────────────────────────
# Base64 將二進位資料編碼為 64 個可列印字元（A-Z, a-z, 0-9, +, /）
# 編碼後長度約為原來的 4/3 倍
msg = b"Python Cookbook"

# 標準 Base64 編碼
encoded = base64.b64encode(msg)
# 輸出為 b'UHl0aG9uIENvb2tib29r'
# 每 3 個位元組編碼為 4 個 Base64 字元
print("\nb64encode：", encoded)

# Base64 解碼，還原為原始 bytes
decoded = base64.b64decode(encoded)
print("b64decode：", decoded)                 # b'Python Cookbook'

# URL-safe Base64：將標準 Base64 中的 + 換成 -，/ 換成 _
# 適合用在 URL 或檔案名稱中，不須跳脫字元
url_encoded = base64.urlsafe_b64encode(msg)
print("urlsafe：  ", url_encoded)

# ── 應用場景比較 ──────────────────────────────────────────────────────
# Hex（十六進位）：
#   - 可讀性高，人類可直接閱讀
#   - 長度為原始資料的 2 倍（1 byte → 2 hex chars）
#   - 常見用途：MD5/SHA 雜湊值、MAC 位址、顏色碼
# Base64：
#   - 長度約為原始資料的 1.33 倍
#   - 常見用途：Email 附件（MIME）、HTTP Basic 認證、JWT Token
# 兩者都只是「表示方式」，不是加密！
# 如果需要安全性，請使用 hashlib（雜湊）或 cryptography（加密）

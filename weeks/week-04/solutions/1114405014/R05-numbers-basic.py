# 從 decimal 模組匯入 Decimal 與 localcontext
# Decimal：提供高精度的十進位運算
# localcontext：可暫時設定 Decimal 的運算環境
from decimal import Decimal, localcontext

# 匯入 math 模組
import math

# round(1.27, 1)：四捨五入到小數點後 1 位
print(round(1.27, 1)) 

# round(1.25361, 3)：四捨五入到小數點後 3 位
print(round(1.25361, 3))

# round(0.5)：對整數位進行四捨五入
# Python 採用「銀行家捨入法」，0.5 會捨入到最接近的偶數
print(round(0.5)) 

# round(2.5)：同樣使用銀行家捨入法，所以會變成 2
print(round(2.5)) 

# 建立一個整數
a = 1627731

# round(a, -2)：四捨五入到百位
# -2 表示從個位往左數兩位，也就是百位
print(round(a, -2))

# 浮點數相加，可能出現精度誤差
print(4.2 + 2.1) 

# 使用 Decimal 進行精確十進位計算
da, db = Decimal("4.2"), Decimal("2.1")
print(da + db)

# localcontext()：建立一個暫時的 Decimal 運算環境
with localcontext() as ctx:
    # 設定精度為 3 位有效數字
    ctx.prec = 3
    
    # 以 Decimal 進行除法，結果會依目前精度限制
    print(Decimal("1.3") / Decimal("1.7")) 

# math.fsum()：高精度加總浮點數
# 可減少一般 sum() 因浮點數誤差造成的問題
print(math.fsum([1.23e18, 1, -1.23e18]))  

# 建立浮點數
x = 1234.56789

# format(x, "0.2f")：固定顯示小數點後 2 位
print(format(x, "0.2f")) 

# format(x, ">10.1f")：
# > 代表靠右對齊
# 10 代表總寬度為 10
# .1f 代表小數點後 1 位
print(format(x, ">10.1f")) 

# format(x, ",")：加入千分位逗號
print(format(x, ",")) 

# format(x, "0,.2f")：加入千分位逗號，並保留 2 位小數
print(format(x, "0,.2f")) 

# format(x, "e")：以科學記號格式輸出
print(format(x, "e"))

# 建立整數
n = 1234

# bin()：轉成二進位字串（含 0b 前綴）
# oct()：轉成八進位字串（含 0o 前綴）
# hex()：轉成十六進位字串（含 0x 前綴）
print(bin(n), oct(n), hex(n))

# format(n, "b")：轉成純二進位字串，不含 0b
# format(n, "x")：轉成純十六進位字串，不含 0x
print(format(n, "b"), format(n, "x"))

# int("4d2", 16)：把十六進位字串轉成十進位整數
# int("2322", 8)：把八進位字串轉成十進位整數
print(int("4d2", 16), int("2322", 8))
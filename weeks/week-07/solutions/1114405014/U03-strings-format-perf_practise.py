# U03. 字串格式化效能與陷阱（2.14–2.20）
# join vs + / format_map 缺失鍵 / bytes 索引差異

import timeit

# ── join 效能優於 + （2.14）──────────────────────────
# 說明：字串是不可變物件，使用 + 串接會產生新字串物件
# 效能分析：
# - 使用 + 串接：每次串接都會建立新字串物件，時間複雜度 O(n²)
# - 使用 join()：一次分配記憶體，時間複雜度 O(n)
# 原因：Python 的 + 運算子會複製左邊字串再加上右邊字串
# 每次迴圈迭代都會：(1) 配置新記憶體 (2) 複製舊內容 (3) 附加新內容
parts = [f"item{i}" for i in range(1000)]


def bad_concat():
    s = ""
    for p in parts:
        s += p  # 每次建立新字串，O(n²)
    return s


def good_join():
    return "".join(parts)  # 一次分配，O(n)


t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"+串接: {t1:.3f}s  join: {t2:.3f}s")
# 結論：join() 明顯更快，尤其在大量字串串接時


# ── format_map 處理缺失鍵（2.15）─────────────────────
# 說明：str.format_map() 與 str.format() 的差異
# - format()：拋出 KeyError 當鍵不存在
# - format_map()：調用 dict 的 __getitem__，可自定義行為
class SafeSub(dict):
    def __missing__(self, key: str) -> str:
        # 當鍵不存在時，回傳保留原始佔位符的格式
        return "{" + key + "}"  # 缺失時保留佔位符


name = "Guido"
s = "{name} has {n} messages."
# vars() 回傳 current local variables 的 dict
# name 存在 → "Guido"，n 不存在 → 回傳 "{n}"
print(s.format_map(SafeSub(vars())))  # 'Guido has {n} messages.'（n 不存在也不報錯）


# ── bytes 索引回傳整數（2.20）────────────────────────
# 說明：str 與 bytes 的索引行為不同
# - str[index] 回傳字元（type: str）
# - bytes[index] 回傳整數（type: int，等同 ord(字元)）
a = "Hello"
b = b"Hello"
print(a[0])  # 'H'（字元）
print(b[0])  # 72（整數 = ord('H')）
# 這是因為 bytes 是位元組序列，索引即該位元組的數值

# bytes 不能直接 format，需先格式化再 encode
# 流程：先產生格式化的 str，再 encode 為 bytes
print("{:10s} {:5d}".format("ACME", 100).encode("ascii"))
# b'ACME            100'
# 說明：{:10s} 左對齊 10 字元，{:5d} 右對齊 5 位數
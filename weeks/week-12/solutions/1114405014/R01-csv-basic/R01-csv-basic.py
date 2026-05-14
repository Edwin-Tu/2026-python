# R01. CSV 基礎讀寫（6.1）
# 主題：csv.reader / csv.writer / csv.DictReader / csv.DictWriter
# CSV（Comma-Separated Values）是最常見的資料交換格式之一

# 匯入 csv 模組，Python 內建，不需額外安裝
import csv
# io.StringIO 讓字串可以模擬檔案物件，方便測試而不需實際讀寫硬碟
import io

# ── 範例資料（模擬 CSV 字串）────────────────────────────────────────
# 用三引號字串模擬一個 CSV 檔案的內容
# 第一列是標頭列（header），定義各欄位名稱
# 逗號是預設的分隔符號（delimiter）
raw = """Symbol,Price,Date,Time,Change,Volume
AA,39.48,6/11/2007,9:36am,-0.18,181800
AIG,71.38,6/11/2007,9:36am,-0.15,195500
AXP,62.58,6/11/2007,9:36am,-0.46,935000
"""

# ── 6.1 csv.reader：逐列讀取，每列是 list ───────────────────────────
# csv.reader 以列為單位讀取 CSV，每一列回傳一個 list
print("=== csv.reader ===")
# 用 StringIO 將字串包裝成檔案物件，避免真的開檔案
f = io.StringIO(raw)
# 建立 reader 物件，可迭代（iterable）
reader = csv.reader(f)
# next() 從迭代器中取得下一列，這裡取得第一列（標頭列）
headers = next(reader)          # 第一列當標頭
print("標頭：", headers)
# 繼續迭代剩餘的資料列，每一列都是字串的 list
for row in reader:
    # row 是一個 list，順序對應標頭順序
    # 例如 ['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '181800']
    print(row)

# ── 6.1 csv.DictReader：每列自動對應成 dict ──────────────────────────
# csv.DictReader 會自動將第一列視為鍵（key），後續每列轉為 dict
print("\n=== csv.DictReader ===")
# 重新建立 StringIO 物件（因為前一個 reader 已經迭代完了）
f = io.StringIO(raw)
# DictReader 以第一列欄位名稱為 key，每一列變成 OrderedDict
for row in csv.DictReader(f):
    # row 是 dict，可用欄位名稱取值，程式碼更可讀
    # 例如 row['Symbol'] 就是 'AA'
    # :5s 是格式化：字串靠左對齊佔 5 字元；:>6s 是右對齊佔 6 字元
    print(f"{row['Symbol']:5s}  價格={row['Price']:>6s}  漲跌={row['Change']}")

# ── 6.1 csv.writer：寫出 CSV ─────────────────────────────────────────
# csv.writer 將 list 寫成 CSV 格式
print("\n=== csv.writer ===")
# 建立 StringIO 物件接收寫入結果
output = io.StringIO()
# 建立 writer 物件
writer = csv.writer(output)
# writerow() 寫入單列，接受一個可迭代物件（如 list）
# 自動在欄位間插入逗號，必要時加上引號
writer.writerow(["Symbol", "Price", "Change"])
writer.writerow(["AA", 39.48, -0.18])
writer.writerow(["AIG", 71.38, -0.15])
# getvalue() 取得 StringIO 中所有寫入的內容
print(output.getvalue())

# ── 6.1 csv.DictWriter：以 dict 寫出 CSV ─────────────────────────────
# csv.DictWriter 接受 dict，根據指定的欄位順序寫出
print("=== csv.DictWriter ===")
output = io.StringIO()
# fieldnames 是一個 list，決定 dict 中哪些鍵要寫出以及順序
fieldnames = ["Symbol", "Price", "Change"]
writer = csv.DictWriter(output, fieldnames=fieldnames)
# writeheader() 會根據 fieldnames 自動寫出標頭列
writer.writeheader()
# writerow() 接受 dict，只取出 fieldnames 中的鍵來寫
writer.writerow({"Symbol": "AA",  "Price": 39.48, "Change": -0.18})
writer.writerow({"Symbol": "AIG", "Price": 71.38, "Change": -0.15})
print(output.getvalue())

# ── 常用參數 ─────────────────────────────────────────────────────────
# delimiter='\t'   → 使用 Tab 作為分隔符號，即 TSV 格式
# quotechar='"'    → 當欄位內包含分隔符號時，用引號包圍
# quoting=csv.QUOTE_ALL → 強制所有欄位都加上引號
# quoting=csv.QUOTE_NONNUMERIC → 非數字欄位才加引號

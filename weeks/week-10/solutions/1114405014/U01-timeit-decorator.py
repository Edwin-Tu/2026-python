# U01. 計時裝飾器實作與資料格式速度比較（6.1 / 6.2 / 6.3）
# 從「重複的計時程式碼」出發，引入裝飾器，再做格式實驗
#
# 本程式分為四個部分：
# 1. 問題展示：手動計時導致程式碼重複
# 2. 裝飾器基礎：將計時邏輯封裝成可重複使用的裝飾器
# 3. functools.wraps：保留被裝飾函式的 metadata（__name__, __doc__ 等）
# 4. 實戰測試：比較 CSV、JSON、XML 三種資料格式的解析速度

import csv
import json
import time
import io
import xml.etree.ElementTree as ET
import functools

# ═══════════════════════════════════════════════════════════
# 部分一：問題展示 — 手動計時導致程式碼重複
# ═══════════════════════════════════════════════════════════

# 定義三個讀取不同格式的函式（功能相同，格式不同）
def read_csv_raw(data: str) -> list:
    """讀取 CSV 格式字串，回傳字典列表"""
    return list(csv.DictReader(io.StringIO(data)))

def read_json_raw(data: str) -> list:
    """讀取 JSON 格式字串，回傳列表"""
    return json.loads(data)

def read_xml_raw(data: str) -> list:
    """讀取 XML 格式字串，回傳屬性字典列表"""
    root = ET.fromstring(data)
    return [r.attrib for r in root.findall("row")]

# 沒有裝飾器的問題：每次都要複製貼上相同的計時程式碼
# 缺點：
#   1. 程式碼重複（Don't Repeat Yourself 原則被違反）
#   2. 容易忘記移除計時程式碼
#   3. 每加一個函式就要多寫三行計時程式碼
#
# 以下是沒有裝飾器時的寫法（已註解）：
# start = time.perf_counter()
# result = read_csv_raw(data)
# print(f"read_csv_raw 耗時 {time.perf_counter() - start:.6f}s")
#
# start = time.perf_counter()
# result = read_json_raw(data)
# print(f"read_json_raw 耗時 {time.perf_counter() - start:.6f}s")
# ... 每加一個函式就多寫三行，且容易忘記移除

# ═══════════════════════════════════════════════════════════
# 部分二：裝飾器基礎 — 將計時邏輯封裝，一次定義到處復用
# ═══════════════════════════════════════════════════════════

def timeit(func):
    """
    基礎版計時裝飾器
    在函式呼叫前後計時，並印出耗時
    參數：func — 被裝飾的函式
    回傳：wrapper 函式
    """
    def wrapper(*args, **kwargs):
        # time.perf_counter() 提供最高精度的計時（包含睡眠時間）
        start = time.perf_counter()

        # 呼叫原始函式，並保存結果
        result = func(*args, **kwargs)

        # 計算並印出耗時
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")

        # 回傳原函式的執行結果（確保功能不變）
        return result
    return wrapper

# 問題展示：單純的裝飾器會覆蓋原函式的 metadata
def demo():
    """這是 demo 的說明文字"""
    pass

# 手動應用裝飾器（等同於 @timeit 語法）
wrapped = timeit(demo)
print("未加 wraps 前：", wrapped.__name__)   # 輸出：wrapper（錯誤！）
# 問題：wrapper 蓋掉了原函式的 __name__ 和 __doc__

# ═══════════════════════════════════════════════════════════
# 部分三：functools.wraps — 保留原函式的 metadata
# ═══════════════════════════════════════════════════════════

def timeit(func):
    """
    改進版計時裝飾器，使用 functools.wraps 保留原函式資訊
    """
    @functools.wraps(func)  # 關鍵：將原函式的 metadata 複製到 wrapper
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__:<20s} {elapsed:.6f}s")
        return result
    return wrapper

# 再次測試：現在 wrapper 會保留原函式的 __name__ 和 __doc__
wrapped = timeit(demo)
print("加 wraps 後：  ", wrapped.__name__)   # 輸出：demo（正確！）
print()

# ═══════════════════════════════════════════════════════════
# 部分四：實戰測試 — 相同資料，CSV vs JSON vs XML 速度比較
# ═══════════════════════════════════════════════════════════

# ── 步驟 1：產生測試資料（1000 筆學生記錄）─────────────────
N = 1000  # 測試資料筆數

# CSV 格式：使用 csv.DictWriter 產生標準 CSV 字串
csv_buf = io.StringIO()
writer = csv.DictWriter(csv_buf, fieldnames=["id", "name", "score"])
writer.writeheader()  # 寫入標頭列
for i in range(N):
    writer.writerow({
        "id": i,
        "name": f"Student{i:04d}",  # 格式化為 4 位數，如 Student0000
        "score": 60 + i % 40         # 分數範圍：60~99
    })
CSV_DATA = csv_buf.getvalue()  # 取得 CSV 格式字串

# JSON 格式：使用 json.dumps 將列表轉為 JSON 字串
JSON_DATA = json.dumps([
    {"id": i, "name": f"Student{i:04d}", "score": 60 + i % 40}
    for i in range(N)
])

# XML 格式：手動組裝 XML 字串（使用 f-string）
xml_rows = "".join(
    f'<row id="{i}" name="Student{i:04d}" score="{60 + i % 40}"/>'
    for i in range(N)
)
XML_DATA = f"<data>{xml_rows}</data>"  # 包裝在 <data> 根元素中

# ── 步驟 2：帶回傳耗時的計時包裝 ─────────────────────────
# 這個版本不直接印出，而是回傳 (結果, 耗時) 元組，方便統計

def timeit_silent(func):
    """
    靜默版計時裝飾器：不印出結果，而是回傳 (結果, 耗時)
    適合用於自動化測試和統計
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        return result, time.perf_counter() - start
    return wrapper

# 建立包裝後的函式（預先包裝好，避免重複裝飾的開銷）
_csv  = timeit_silent(read_csv_raw)
_json = timeit_silent(read_json_raw)
_xml  = timeit_silent(read_xml_raw)

# ── 步驟 3：執行比較（重複多次取平均，排除冷啟動影響）─────

RUNS = 5  # 每種格式執行的次數
times = {"CSV": 0.0, "JSON": 0.0, "XML": 0.0}

# 重複執行並累計時間
for _ in range(RUNS):
    _, t = _csv(CSV_DATA);   times["CSV"]  += t  # CSV 解析
    _, t = _json(JSON_DATA); times["JSON"] += t  # JSON 解析
    _, t = _xml(XML_DATA);   times["XML"]  += t  # XML 解析

# 輸出結果表格
print(f"=== 讀取 {N} 筆資料，重複 {RUNS} 次平均 ===\n")
print(f"{'格式':<6} {'平均耗時':>12}  {'相對 JSON':>10}")

# 以 JSON 為基準（baseline），計算各格式的相對速度
base = times["JSON"] / RUNS

for fmt, total in times.items():
    avg = total / RUNS  # 計算平均耗時
    print(f"  {fmt:<6} {avg:.6f}s   {avg/base:>8.2f}x")

# ═══════════════════════════════════════════════════════════
# 觀察重點與結論
# ═══════════════════════════════════════════════════════════
# 1. JSON 通常最快：因為 Python 的 json 模組底層是 C 實作，解析速度快
# 2. XML 通常最慢：需要完整的 XML 解析器，文字解析開銷大，屬性需字串轉換
# 3. CSV 介於中間：格式簡單，但每個欄位都是字串，需要自行轉型（如 int, float）
#
# 裝飾器帶來的好處：
# ✅ 計時邏輯只寫一次，不汙染原函式（關注點分離）
# ✅ 要移除計時只需拿掉 @timeit 裝飾器，函式本身不需修改
# ✅ functools.wraps 確保 debug、help()、日誌等能看到正確的函式名稱與說明
# ✅ 裝飾器可以堆疊使用（如 @timeit @cache），增加功能而不改原程式碼

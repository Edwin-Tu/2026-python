# R02. JSON 基礎讀寫（6.2）
# 主題：json.loads / json.dumps / json.load / json.dump
# JSON（JavaScript Object Notation）是輕量級資料交換格式
# Python 的 json 模組可以將 Python 物件與 JSON 字串互相轉換

# 匯入 json 模組，Python 內建，不需額外安裝
import json

# ── 字串 ↔ Python 物件 ───────────────────────────────────────────────
# Python 的 dict/list 等內建型別可以直接轉換為 JSON
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

# 序列化（Serialization）：Python 物件 → JSON 字串
# dumps = dump string，回傳字串而非寫入檔案
s = json.dumps(data)
# type(s) 會是 <class 'str'>
# 預設不縮排，輸出為緊湊的一行：{"name": "Alice", "age": 30, "scores": [95, 87, 92]}
print(type(s), s)

# 美化輸出（pretty print）
# indent=4 表示每層縮排 4 個空格
# sort_keys=True 表示按照鍵的字母順序排序
s_pretty = json.dumps(data, indent=4, sort_keys=True)
print(s_pretty)

# 反序列化（Deserialization）：JSON 字串 → Python 物件
# loads = load string，從字串解析回 Python 物件
obj = json.loads(s)
# obj 的 type 會是 <class 'dict'>，obj["name"] 就是 "Alice"
print(type(obj), obj["name"])

# ── 檔案 I/O ─────────────────────────────────────────────────────────
# 將 Python 物件序列化後直接寫入檔案，使用 json.dump()（沒有 s）
# 開啟檔案寫入模式，指定 UTF-8 編碼以支援中文
with open("/tmp/data.json", "w", encoding="utf-8") as f:
    # dump 直接將資料寫入檔案物件，不需先轉成字串
    # ensure_ascii=False 讓非 ASCII 字元（如中文）直接輸出，不跳脫
    json.dump(data, f, indent=2, ensure_ascii=False)

# 從檔案讀入 JSON 並解析為 Python 物件，使用 json.load()（沒有 s）
with open("/tmp/data.json", "r", encoding="utf-8") as f:
    # load 直接從檔案物件讀取並解析
    loaded = json.load(f)
# loaded 是 dict，內容與原始 data 相同
print(loaded)

# ── 型別對應 ──────────────────────────────────────────────────────────
# Python 與 JSON 之間的型別對應關係：
# Python dict   → JSON object  {}
# Python list   → JSON array   []
# Python str    → JSON string  ""
# Python int    → JSON number（整數）
# Python float  → JSON number（浮點數）
# Python True   → JSON true
# Python False  → JSON false
# Python None   → JSON null
# Python tuple  → JSON array（轉換時 tuple 會變成 list）

# 展示型別對應：list 中有整數、布林、None、字串
print(json.dumps([1, True, None, "hello"]))
# 輸出：[1, true, null, "hello"]

# ── 中文不跳脫 ───────────────────────────────────────────────────────
# 預設 ensure_ascii=True 時，非 ASCII 字元會以 \uXXXX 跳脫
# 設定 ensure_ascii=False 則保留原始字元，人類可讀
record = {"城市": "澎湖", "人口": 100000}
# ensure_ascii=False：直接輸出中文字元
# {"城市": "澎湖", "人口": 100000}
print(json.dumps(record, ensure_ascii=False))
# ensure_ascii=True（預設）：中文字元被跳脫
# {"城市": "\u6f8e\u6e56", "人口": 100000}
print(json.dumps(record, ensure_ascii=True))

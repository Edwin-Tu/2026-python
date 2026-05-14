# R05. 資料統計與累加（6.13）
# 主題：Counter / defaultdict / namedtuple 整合應用
# collections 模組提供許多好用的資料結構，讓資料處理更簡潔

# 從 collections 一次匯入三個常用工具
from collections import Counter, defaultdict, namedtuple

# ── Counter：計數器 ──────────────────────────────────────────────────
# Counter 是 dict 的子類別，專門用來計算可雜湊物件的出現次數
# 輸入一個可迭代物件，自動統計每個元素出現的次數
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# 建立 Counter 物件，傳入 list 即可自動統計
cnt = Counter(words)
# Counter 會顯示每個元素及其次數
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print("Counter：", cnt)
# most_common(n) 回傳出現次數最高的前 n 個元素
# 回傳值是一個 list，每個元素是 (元素, 次數) 的 tuple
print("最多出現：", cnt.most_common(2))      # [('apple', 3), ('banana', 2)]

# Counter 支援加法運算，合併兩個 Counter 的計數
# 對應的元素次數會相加
extra = Counter(["banana", "cherry"])
print("合併：", cnt + extra)   # apple: 3, banana: 3, cherry: 2

# ── defaultdict：有預設值的 dict ────────────────────────────────────
# defaultdict 是 dict 的子類別，當存取不存在的鍵時會自動建立預設值
# 避免每次都要檢查鍵是否存在（KeyError）

# 應用一：按類別分組（預設值為 list）
# 將學生按照科系分組
records = [
    ("系資", "Alice"),
    ("電子", "Bob"),
    ("系資", "Carol"),
    ("電子", "David"),
    ("系資", "Eve"),
]

# defaultdict(list) 表示當鍵不存在時，自動建立一個空的 list
# 這樣直接呼叫 .append() 就不會產生 KeyError
by_dept = defaultdict(list)
for dept, name in records:
    # 如果 dept 不存在，defaultdict 會自動建立 dept: []
    # 然後再執行 append，完全不需要檢查鍵是否存在
    by_dept[dept].append(name)

print("\ndefaultdict：")
for dept, members in by_dept.items():
    print(f"  {dept}: {members}")

# 應用二：自動計數（預設值為 int）
# defaultdict(int) 表示預設值為 0（int() 回傳 0）
score_sum = defaultdict(int)
scores = [("Alice", 90), ("Bob", 80), ("Alice", 85), ("Bob", 70)]
for name, score in scores:
    # 第一次遇到 Alice 時，預設值為 0，然後加上 90
    # 第二次遇到 Alice 時，值已經是 90，再加上 85 變成 175
    score_sum[name] += score
# 如果使用一般 dict，需要先檢查鍵是否存在再初始化
print("\n各人總分：", dict(score_sum))

# ── namedtuple：具名結構，更可讀 ────────────────────────────────────
# namedtuple 建立一個輕量級的「不可變資料容器」
# 類似 tuple，但可以透過屬性名稱（而非索引）存取資料
# 語法：namedtuple(類別名稱, [欄位名稱1, 欄位名稱2, ...])
Stock = namedtuple("Stock", ["symbol", "price", "change"])
# 建立一個 Stock 實例，使用關鍵字參數提升可讀性
s = Stock("AA", 39.48, -0.18)
# 可以像物件屬性一樣存取，比 s[0], s[1], s[2] 更直觀
print(f"\n{s.symbol}: ${s.price}  漲跌 {s.change}")
# namedtuple 也支援索引存取（因為本質上還是 tuple）
print(f"透過索引：{s[0]}, {s[1]}, {s[2]}")

# ── 綜合應用：從 list of dict 做統計 ─────────────────────────────────
# 實際工作中常遇到這種結構：從 API 或資料庫取得的資料
data = [
    {"dept": "系資", "score": 85},
    {"dept": "電子", "score": 78},
    {"dept": "系資", "score": 92},
    {"dept": "電子", "score": 88},
]

# 使用 defaultdict(list) 按照科系分組收集分數
dept_scores = defaultdict(list)
for row in data:
    # row["dept"] 是科系名稱（如 "系資"）
    # row["score"] 是分數
    dept_scores[row["dept"]].append(row["score"])

# 計算每個科系的平均分數
print("\n各系平均：")
for dept, scores in dept_scores.items():
    avg = sum(scores) / len(scores)
    # :.1f 表示格式化為小數點後一位
    print(f"  {dept}: {avg:.1f}")

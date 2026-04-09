# U01. 字串分割與匹配的陷阱（2.1–2.11）
# 捕獲分組保留分隔符 / startswith 必須傳 tuple / strip 只處理頭尾

import re

# ── 捕獲分組保留分隔符（2.1）─────────────────────────
# 說明：re.split() 使用捕獲分組時，分隔符會被包含在結果陣列中
# 語法：re.split(r"(分組)", 字串) - 用括號包住的正規表達式會被捕獲
# 用途：當需要知道分割時使用什麼分隔符時，可保留分隔符供後續重建使用
line = "asdf fjdk; afed, fjek,asdf, foo"
# 正則表達式說明：
# (;|,|\s) - 捕獲分組：匹配分號、逗號或空白字元
# \s* - 匹配零個或多個空白字元（分隔符後方的空格）
fields = re.split(r"(;|,|\s)\s*", line)
# 結果：['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
# 偶數索引 (0,2,4...) 是實際值，奇數索引 (1,3,5...) 是分隔符
values = fields[::2]  # 取出所有偶數索引 = 實際值陣列
# 處理最後一個分隔符：原本的最後一個分隔符後面沒有元素，需補上空的
delimiters = fields[1::2] + [""]  # 合併一個空字串確保長度一致
# 使用 zip 交叉配對：values[0]+delimiters[0], values[1]+delimiters[1]...
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print(rebuilt)  # 'asdf fjdk;afed,fjek,asdf,foo'
# 說明：原本的 " fjdk; " 變成 "fjdk;" - 注意空格被移除了

# ── startswith 必須傳 tuple（2.2）────────────────────
# 說明：str.startswith() 和 str.endswith() 方法
# 參數必須是 tuple 或 frozenset，不能是 list 或其他可迭代物件
# 這是 Python 的設計決定，原因可能是：
# 1. 語意明確：tuple 表示「一系列固定的選項」，list 表示「可變集合」
# 2. 避免歧義：list 可能會被誤認為單一元素（當作單一字串）
# 3. 效能：tuple 是不可變的，可被 hash 且優化
url = "http://www.python.org"
choices = ["http:", "ftp:"]
try:
    # 嘗試傳入 list，會引發 TypeError
    url.startswith(choices)  # type: ignore[arg-type]
except TypeError as e:
    print(f"TypeError: {e}")  # 'str.startswith' does not support a list
# 正確做法：將 list 轉換為 tuple
print(url.startswith(tuple(choices)))  # True（轉成 tuple 才行）

# ── strip 只處理頭尾，不處理中間（2.11）──────────────
# 說明：str.strip() 只移除字串開頭和結尾的空白字元
# 中間的空白不會被移除，這是常見的誤解
s = "  hello     world  "
print(repr(s.strip()))  # 'hello     world'（中間多餘空白還在）
# 如果需要移除所有空白：使用 replace（但會移除詞間的空白）
print(repr(s.replace(" ", "")))  # 'helloworld'（過頭，連詞間空白也消）
# 正確做法：用正規表達式將連續空白替換為單一空格
print(repr(re.sub(r"\s+", " ", s.strip())))  # 'hello world'（正確）
# 正則表達式說明：\s+ 匹配一個或多個空白字元（包括空格、tab、換行）
# re.sub() 將匹配到的內容替換為單一空格

# 生成器逐行清理（高效，不預載入記憶體）
# 說明：使用生成器表達式 (generator expression) 而非列表
# 優點：逐行處理，不會一次性將所有行載入記憶體，適合處理大檔案
lines = ["  apple  \n", "  banana  \n"]
for line in (l.strip() for l in lines):
    print(line)
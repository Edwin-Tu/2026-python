# 匯入 re 模組：用來做正規表示式處理
import re

# 原始文字，裡面包含兩個日期
text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# 建立日期的正規表示式物件
# (\d+) 表示一個或多個數字
# 用括號包起來代表「分組」
# 這裡分成 月 / 日 / 年 三組
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# findall() 會找出所有符合格式的日期
# 回傳值會是由 tuple 組成的 list
# 每個 tuple 內分別是 month, day, year
print(datepat.findall(text))

# match() 只會從字串開頭開始比對
# 這裡 "11/27/2012" 一開始就是日期，所以能成功比對
m = datepat.match("11/27/2012")

# 確保比對成功
assert m is not None

# group(0) 代表完整符合的字串
# groups() 代表各個括號分組抓到的內容
print(m.group(0), m.groups())

# finditer() 會逐一回傳每個符合結果的 Match 物件
for m in datepat.finditer(text):
    # 取出三個分組：月、日、年
    month, day, year = m.groups()
    
    # 重新組成 年-月-日 的格式
    print(f"{year}-{month}-{day}")

# 使用 re.sub() 直接進行字串替換
# \1, \2, \3 分別代表第 1、2、3 個分組
# 原本是 月/日/年，改成 年-月-日
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))

# 使用具名分組的方式來替換
# (?P<month>...) 表示將這組命名為 month
# 這樣在替換時可以用名稱來引用，閱讀性更高
print(
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
)

# re.subn() 與 sub() 類似
# 差別在於它會回傳：
# 1. 替換後的新字串
# 2. 替換發生的次數
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)

# 印出替換次數
print(f"替換了 {n} 次")

# 建立一段大小寫混合的文字
s = "UPPER PYTHON, lower python, Mixed Python"

# re.findall() 搭配 IGNORECASE 旗標
# 表示搜尋時忽略大小寫
# 所以 python、PYTHON、Python 都會被找出來
print(re.findall("python", s, flags=re.IGNORECASE))

# 建立含有雙引號內容的文字
text2 = 'Computer says "no." Phone says "yes."'

# 使用貪婪模式 (.*)
# 會盡可能匹配最長字串
# 因此可能從第一個引號一路抓到最後一個引號
print(re.compile(r'"(.*)"').findall(text2))

# 使用非貪婪模式 (.*?)
# 會盡可能匹配最短字串
# 因此可分別抓出每組引號內的內容
print(re.compile(r'"(.*?)"').findall(text2))

# 建立多行註解文字
code = "/* this is a\nmultiline comment */"

# 使用 DOTALL 模式
# 讓 . 也可以匹配換行字元
# 這樣就能抓到跨行的註解內容
print(re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code))
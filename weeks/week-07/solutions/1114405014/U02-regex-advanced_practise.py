# U02. 正則表達式進階技巧（2.4–2.6）
# 預編譯效能 / sub 回呼函數 / 大小寫一致替換

import re
import timeit
from calendar import month_abbr

# ── 預編譯效能（2.4）──────────────────────────────────
# 說明：正則表達式預先用 re.compile() 編譯，可提升重複使用時的效能
# 原理：編譯後的正則表達式會被快取，重複匹配時無需重新解析正則語法
# 適用場景：當同一個正則表達式需要匹配多次時（如迴圈、大量文字處理）
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
# 正則表達式說明：
# (\d+) - 捕獲一或多個數字，分為三個群組：月、日、年
# / - 固定的分隔符斜線


def using_module():
    # 直接使用 re.findall()，每次呼叫都會解析正則表達式
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)


def using_compiled():
    # 使用預先編譯的 pattern，減少解析開銷
    return datepat.findall(text)


# 測試效能：執行 50,000 次
t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(using_compiled, number=50_000)
print(f"直接呼叫: {t1:.3f}s  預編譯: {t2:.3f}s")
# 結論：預編譯通常更快，尤其在大數據量時更明顯


# ── sub 回呼函數（2.5）────────────────────────────────
# 說明：re.sub() 的 replacement 參數可以是函數（回呼函數）
# 用途：根據匹配內容動態生成替換文字，實現複雜的替換邏輯
def change_date(m: re.Match) -> str:
    # re.Match 物件包含完整匹配資訊：
    # m.group(0) 或 m.group() - 整個匹配（"11/27/2012"）
    # m.group(1) - 第一個捕獲群組（月：11）
    # m.group(2) - 第二個捕獲群組（日：27）
    # m.group(3) - 第三個群組（年：2012）
    mon_name = month_abbr[int(m.group(1))]
    # month_abbr 是 calendar 模組的月份縮寫列表
    # index 1-12 對應 Jan-Dec，將數字轉為英文縮寫
    return f"{m.group(2)} {mon_name} {m.group(3)}"


# 使用回呼函數替換所有匹配
print(datepat.sub(change_date, text))
# 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'


# ── 保持大小寫一致的替換（2.6）───────────────────────
# 說明：在進行不区分大小写的替換時，保持原文字的大小寫形式
# 應用場景：如全文搜尋並替換時，希望根據原文大小寫調整替換文字
def matchcase(word: str):
    # 回呼工廠：返回一個回呼函數，可攜帶額外參數（word）
    def replace(m: re.Match) -> str:
        t = m.group()  # 取得匹配到的原始文字
        if t.isupper():
            # 全部大寫 → 全部大寫
            return word.upper()
        if t.islower():
            # 全部小寫 → 全部小寫
            return word.lower()
        if t[0].isupper():
            # 首字母大寫 → 首字母大寫（title case）
            return word.capitalize()
        return word  # 預設：維持原樣

    return replace


# 測試案例
s = "UPPER PYTHON, lower python, Mixed Python"
# flags=re.IGNORECASE - 不区分大小写匹配
# matchcase("snake") - 根據原文字大小寫，動態調整 "snake" 的大小寫
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
# 'UPPER SNAKE, lower snake, Mixed Snake'
# 說明：原本的 "PYTHON" 變成 "SNAKE"，"python" 變成 "snake"，"Python" 變成 "Snake"
# U05. 日期時間的陷阱（3.12–3.15）
# timedelta 不支援月份 / strptime 效能問題

import timeit
import calendar
from datetime import datetime, timedelta

# ── timedelta 不支援月份（3.12）──────────────────────
# 說明：timedelta 類別只支援天（小時、分、秒）的運算
# 不支援「月」或「年」等時間單位，因為它們的天數不固定
# 直接使用 months 參數會引發 TypeError
dt = datetime(2012, 9, 23)
try:
    dt + timedelta(months=1)  # type: ignore[call-arg]
except TypeError as e:
    print(f"TypeError: {e}")  # 'months' is an invalid keyword argument


# 正確做法：用 calendar 取得目標月份天數，並將日期 clamp 到該月最後一天
# 說明：當原日期是月底（如1月31日）加一個月時，
# 目標月份可能沒有31天，需要將日期調整到該月最後一天
def add_one_month(dt: datetime) -> datetime:
    # 計算目標的年與月
    year = dt.year
    month = dt.month + 1
    if month == 13:  # 跨年
        year += 1
        month = 1

    # calendar.monthrange(year, month) 回傳 ( weekday, days )
    # days 是該月的總天數
    _, days_in_target_month = calendar.monthrange(year, month)
    # 將原日期限制在目標月份的天數範圍內
    # 例如：1月31日 + 1月 → 2月只有29天（閏年）→ 調整為29日
    day = min(dt.day, days_in_target_month)

    return dt.replace(year=year, month=month, day=day)


print(add_one_month(datetime(2012, 1, 31)))  # 2012-02-29（閏年二月有29天）
print(add_one_month(datetime(2012, 9, 23)))  # 2012-10-23（正常月份，直接加一個月）


# ── strptime 效能問題（3.15）─────────────────────────
# 說明：datetime.strptime() 每次呼叫都會解析格式字串
# 在大量日期處理時會成為效能瓶頸，應考慮手動解析
# 建立測試資料：12個月 x 28天 = 336 個日期字串
dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]


def use_strptime(s: str) -> datetime:
    # strptime：需要解析格式字串 "%Y-%m-%d"，每次都有開銷
    return datetime.strptime(s, "%Y-%m-%d")


def use_manual(s: str) -> datetime:
    # 手動解析：直接分割字串並轉換為整數，效能較好
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))


# 驗證兩者結果相同
assert use_strptime("2012-09-20") == use_manual("2012-09-20")

# 效能測試：各執行 100 次
t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=100)
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)
print(f"strptime: {t1:.3f}s  手動解析: {t2:.3f}s（快 {t1 / t2:.1f} 倍）")
# 結論：手動解析通常快 2-3 倍，但在需要嚴格格式驗證時仍應使用 strptime
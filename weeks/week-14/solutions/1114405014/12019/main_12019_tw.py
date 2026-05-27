# 各月份對應的 Doomsday 參考日期（2012 年）
DOOMSDAY = {
    1: 10, 2: 21, 3: 7, 4: 4, 5: 9, 6: 6,
    7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12
}

# 星期對照表（0 = Monday, 6 = Sunday）
WEEKDAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def solve():
    """
    使用 Doom's Day 演算法計算 2012 年任意日期的星期。
    2012 年的 Doomsday 為星期三（索引 2）。
    """
    t = int(input().strip())
    for _ in range(t):
        m, d = map(int, input().split())
        # 取得該月份的 Doomsday 參考日期
        doomsday = DOOMSDAY[m]
        # 計算與參考日期的天數差
        diff = d - doomsday
        # 2012 doomsday = Wednesday (index 2)
        weekday_idx = (2 + diff) % 7
        print(WEEKDAY[weekday_idx])


if __name__ == "__main__":
    solve()

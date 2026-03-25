# 判斷是否為週末（星期五或星期六）
def is_weekend(day):
    # 題目規定第1天是星期天
    # day % 7 == 6 → 星期五
    # day % 7 == 0 → 星期六
    return day % 7 == 6 or day % 7 == 0


# 計算罷工天數
def count_hartals(n, parties):
    hartal_days = set()  # 用集合避免重複計算

    # 對每個政黨
    for h in parties:
        # 每隔 h 天罷工一次
        for day in range(h, n + 1, h):
            if not is_weekend(day):  # 如果不是週末才算
                hartal_days.add(day)

    return len(hartal_days)


# 主程式
def solve():
    t = int(input())  # 測試資料數

    for _ in range(t):
        n = int(input())  # 總天數
        p = int(input())  # 政黨數量

        parties = []
        for _ in range(p):
            parties.append(int(input()))  # 每個政黨的罷工週期

        result = count_hartals(n, parties)
        print(result)


if __name__ == "__main__":
    solve()
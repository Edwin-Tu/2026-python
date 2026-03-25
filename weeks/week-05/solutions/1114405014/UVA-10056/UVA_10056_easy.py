# 計算第 i 個人最終贏的機率
def win_probability(n, p, i):
    # 如果成功機率是 0，永遠不會贏
    if p == 0:
        return 0.0

    # 第一輪就贏的機率
    first_win = (1 - p) ** (i - 1) * p

    # 一整輪（n人都失敗）的機率
    all_fail = (1 - p) ** n

    # 無限輪累積（等比級數）
    return first_win / (1 - all_fail)


# 主程式
def solve():
    t = int(input())  # 測試資料數

    for _ in range(t):
        n = int(input())      # 玩家數
        p = float(input())    # 每次成功機率
        i = int(input())      # 第幾位玩家

        result = win_probability(n, p, i)

        # 輸出小數點後4位
        print(f"{result:.4f}")


if __name__ == "__main__":
    solve()
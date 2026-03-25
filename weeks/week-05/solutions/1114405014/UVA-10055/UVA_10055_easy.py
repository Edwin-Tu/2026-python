# 主程式
def solve():
    n, q = map(int, input().split())

    # 0 = 遞增，1 = 遞減（初始全部為遞增）
    states = [0] * n

    for _ in range(q):
        data = list(map(int, input().split()))

        # 操作 1：翻轉某個函數
        if data[0] == 1:
            i = data[1] - 1  # 轉成 0-based index
            states[i] = 1 - states[i]  # 0 ↔ 1

        # 操作 2：查詢區間
        else:
            l = data[1] - 1
            r = data[2] - 1

            # 計算區間內「遞減」的數量
            count = sum(states[l:r+1])

            # 奇數 → 遞減(1)，偶數 → 遞增(0)
            print(count % 2)


if __name__ == "__main__":
    solve()
# 讀取測試資料筆數
t = int(input())

for _ in range(t):
    # 讀取總和 S 與差值 D
    s, d = map(int, input().split())

    # 若 S < D 或 S+D 為奇數，代表無法組成合法整數
    if s < d or (s + d) % 2 != 0:
        print("impossible")
    else:
        # 計算較大與較小分數
        high = (s + d) // 2
        low = (s - d) // 2

        print(high, low)

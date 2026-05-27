def solve():
    # 讀取測試資料組數 T
    t = int(input().strip())
    # 依序處理每一組測試資料
    for case in range(1, t + 1):
        # 讀取矩陣維度行（格式 "N = n"），跳過空白行
        line = input().strip()
        while line == '':
            line = input().strip()
        n = int(line.split('=')[1].strip())
        # 讀取 n x n 方陣
        M = [list(map(int, input().split())) for _ in range(n)]
        symmetric = True
        # 檢查中心對稱性與非負條件
        for i in range(n):
            for j in range(n):
                # 條件 1：元素不可為負
                # 條件 2：M[i][j] 必須等於 M[n-1-i][n-1-j]（中心對稱）
                if M[i][j] < 0 or M[i][j] != M[n - 1 - i][n - 1 - j]:
                    symmetric = False
                    break
            if not symmetric:
                break
        # 輸出結果
        if symmetric:
            print(f"Test #{case}: Symmetric.")
        else:
            print(f"Test #{case}: Non-symmetric.")


if __name__ == "__main__":
    solve()

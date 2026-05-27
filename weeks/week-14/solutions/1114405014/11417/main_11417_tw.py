import math


def solve():
    """
    計算 G = Σ_{i=1}^{N-1} Σ_{j=i+1}^{N} gcd(i, j)
    當輸入為 0 時結束。
    """
    while True:
        line = input().strip()
        n = int(line)
        if n == 0:
            # 遇到 0 結束程式
            break
        total = 0
        # 雙層迴圈窮舉所有 i < j 的數對
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                # 累加最大公因數
                total += math.gcd(i, j)
        print(total)


if __name__ == "__main__":
    solve()

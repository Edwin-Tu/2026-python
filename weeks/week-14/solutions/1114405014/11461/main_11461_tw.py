import math


def solve():
    """
    計算閉區間 [a, b] 內完全平方數的個數。
    當 a = b = 0 時結束輸入。
    """
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            # 終止條件
            break
        # 完全平方數個數 = floor(sqrt(b)) - floor(sqrt(a-1))
        # 使用 math.isqrt 避免浮點數誤差
        count = int(math.isqrt(b)) - int(math.isqrt(a - 1))
        print(count)


if __name__ == "__main__":
    solve()

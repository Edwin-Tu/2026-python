import math


def solve():
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        count = int(math.isqrt(b)) - int(math.isqrt(a - 1))
        print(count)


if __name__ == "__main__":
    solve()

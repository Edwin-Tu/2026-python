def win_probability(n, p, i):
    if p == 0:
        return 0.0
    first = (1 - p) ** (i - 1) * p
    fail = (1 - p) ** n
    return first / (1 - fail)


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = float(input())
        i = int(input())
        print(f"{win_probability(n, p, i):.4f}")


if __name__ == "__main__":
    solve()
def is_weekend(day):
    return day % 7 == 6 or day % 7 == 0


def count_hartals(n, parties):
    days = set()
    for h in parties:
        for day in range(h, n + 1, h):
            if not is_weekend(day):
                days.add(day)
    return len(days)


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = int(input())
        parties = [int(input()) for _ in range(p)]
        print(count_hartals(n, parties))


if __name__ == "__main__":
    solve()
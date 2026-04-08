import sys
from collections import Counter


def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    S = list(map(int, data[1:]))

    abc_counts = Counter()
    for a in S:
        for b in S:
            for c in S:
                abc_counts[a * b * c] += 1

    count = 0
    for d in S:
        for e in S:
            for f in S:
                target = d * e * f
                count += abc_counts[target]

    print(count)


if __name__ == "__main__":
    solve()
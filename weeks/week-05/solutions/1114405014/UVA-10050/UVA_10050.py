def is_weekend(day: int) -> bool:
    """
    題目規定第 1 天是星期天
    因此：
    day % 7 == 6 -> 星期五
    day % 7 == 0 -> 星期六
    """
    return day % 7 == 6 or day % 7 == 0


def count_hartals(n: int, parties: list[int]) -> int:
    hartal_days = set()

    for h in parties:
        for day in range(h, n + 1, h):
            if not is_weekend(day):
                hartal_days.add(day)

    return len(hartal_days)


def solve(data: str) -> str:
    tokens = data.split()
    t = int(tokens[0])
    index = 1
    results = []

    for _ in range(t):
        n = int(tokens[index])
        index += 1

        p = int(tokens[index])
        index += 1

        parties = []
        for _ in range(p):
            parties.append(int(tokens[index]))
            index += 1

        results.append(str(count_hartals(n, parties)))

    return "\n".join(results) + "\n"


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()), end="")
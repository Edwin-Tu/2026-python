def win_probability(n: int, p: float, i: int) -> float:
    """
    回傳第 i 位玩家最終獲勝的機率
    """
    if p == 0.0:
        return 0.0

    first_round = ((1 - p) ** (i - 1)) * p
    cycle_fail = (1 - p) ** n

    return first_round / (1 - cycle_fail)


def solve(data: str) -> str:
    tokens = data.split()
    t = int(tokens[0])
    index = 1
    results = []

    for _ in range(t):
        n = int(tokens[index])
        index += 1

        p = float(tokens[index])
        index += 1

        i = int(tokens[index])
        index += 1

        results.append(f"{win_probability(n, p, i):.4f}")

    return "\n".join(results) + "\n"


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()), end="")
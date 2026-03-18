def diff(a: int, b: int) -> int:
    return abs(a - b)


def solve(input_data: str) -> str:
    lines = input_data.splitlines()
    results = []

    for line in lines:
        line = line.strip()

        if not line:
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        a, b = map(int, parts)
        results.append(str(diff(a, b)))
    return "\n".join(results)


def main() -> None:
    import sys
    input_data = sys.stdin.read()
    print(solve(input_data))


if __name__ == "__main__":
    main()
from typing import List


def is_jolly(nums: List[int]) -> bool:
    n = len(nums)

    if n == 1:
        return True

    differences = set()

    for i in range(1, n):
        diff = abs(nums[i] - nums[i - 1])

        if diff < 1 or diff >= n:
            return False

        differences.add(diff)

    return len(differences) == n - 1


def solve(input_data: str) -> str:
    results = []

    for line in input_data.splitlines():
        line = line.strip()
        if not line:
            continue

        parts = list(map(int, line.split()))
        n = parts[0]
        nums = parts[1:1 + n]

        if is_jolly(nums):
            results.append("Jolly")
        else:
            results.append("Not jolly")

    return "\n".join(results)


def main() -> None:
    import sys
    input_data = sys.stdin.read()
    print(solve(input_data))


if __name__ == "__main__":
    main()
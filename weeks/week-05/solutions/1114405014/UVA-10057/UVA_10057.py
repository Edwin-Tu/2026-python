def analyze_password(nums: list[int]) -> tuple[int, int, int]:
    sorted_nums = sorted(nums)
    n = len(sorted_nums)

    left_median = sorted_nums[(n - 1) // 2]
    right_median = sorted_nums[n // 2]

    best_a = left_median
    count_in_range = sum(1 for num in sorted_nums if left_median <= num <= right_median)
    number_of_best_a = right_median - left_median + 1

    return best_a, count_in_range, number_of_best_a


def solve(data: str) -> str:
    tokens = data.split()
    index = 0
    results = []

    while index < len(tokens):
        n = int(tokens[index])
        index += 1

        nums = list(map(int, tokens[index:index + n]))
        index += n

        best_a, count_in_range, number_of_best_a = analyze_password(nums)
        results.append(f"{best_a} {count_in_range} {number_of_best_a}")

    return "\n".join(results) + "\n"


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()), end="")
def count_carries(a: str, b: str) -> int:
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    count = 0

    while i >= 0 or j >= 0:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        total = digit_a + digit_b + carry

        if total >= 10:
            carry = 1
            count += 1
        else:
            carry = 0

        i -= 1
        j -= 1

    return count


def format_result(carries: int) -> str:
    if carries == 0:
        return "No carry operation."
    elif carries == 1:
        return "1 carry operation."
    else:
        return f"{carries} carry operations."


def solve(input_data: str) -> str:
    lines = input_data.strip().splitlines()
    results = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        a, b = line.split()

        if a == "0" and b == "0":
            break

        carries = count_carries(a, b)
        results.append(format_result(carries))

    return "\n".join(results)


def main() -> None:
    import sys
    input_data = sys.stdin.read()
    print(solve(input_data))


if __name__ == "__main__":
    main()
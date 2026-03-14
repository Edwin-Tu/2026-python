from typing import List
import sys


def parse_numbers(input_text: str) -> List[int]:
    input_text = input_text.strip()
    if not input_text:
        return []
    return [int(token) for token in input_text.split()]


def dedupe_preserve_order(numbers: List[int]) -> List[int]:
    seen = []
    result = []

    for num in numbers:
        if num not in seen:
            seen.append(num)
            result.append(num)

    return result


def get_even_numbers(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num % 2 == 0]


def format_line(label: str, numbers: List[int]) -> str:
    if not numbers:
        return f"{label}:"
    return f"{label}: {' '.join(str(num) for num in numbers)}"


def solve(input_text: str) -> str:
    numbers = parse_numbers(input_text)

    deduped = dedupe_preserve_order(numbers)
    asc_sorted = sorted(numbers)
    desc_sorted = sorted(numbers, reverse=True)
    evens = get_even_numbers(numbers)

    output_lines = [
        format_line("dedupe", deduped),
        format_line("asc", asc_sorted),
        format_line("desc", desc_sorted),
        format_line("evens", evens),
    ]
    return "\n".join(output_lines)


def main() -> None:
    input_text = sys.stdin.read()
    print(solve(input_text))


if __name__ == "__main__":
    main()
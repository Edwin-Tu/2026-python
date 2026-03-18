from typing import List, Tuple


Weighing = Tuple[List[int], List[int], str]


def is_possible_fake(coin: int, is_heavier: bool, weighings: List[Weighing]) -> bool:
    for left, right, result in weighings:
        left_weight = 0
        right_weight = 0

        for c in left:
            if c == coin:
                left_weight += 2 if is_heavier else 0
            else:
                left_weight += 1

        for c in right:
            if c == coin:
                right_weight += 2 if is_heavier else 0
            else:
                right_weight += 1

        if result == "=":
            if left_weight != right_weight:
                return False
        elif result == "<":
            if not (left_weight < right_weight):
                return False
        elif result == ">":
            if not (left_weight > right_weight):
                return False
        else:
            return False

    return True


def find_fake_coin(n: int, weighings: List[Weighing]) -> int:
    candidates = []

    for coin in range(1, n + 1):
        can_be_heavier = is_possible_fake(coin, True, weighings)
        can_be_lighter = is_possible_fake(coin, False, weighings)

        if can_be_heavier or can_be_lighter:
            candidates.append(coin)

    if len(candidates) == 1:
        return candidates[0]
    return 0


def solve(input_data: str) -> str:
    lines = [line.strip() for line in input_data.splitlines()]
    index = 0

    while index < len(lines) and lines[index] == "":
        index += 1

    t = int(lines[index])
    index += 1

    answers = []

    for _ in range(t):
        while index < len(lines) and lines[index] == "":
            index += 1

        n, k = map(int, lines[index].split())
        index += 1

        weighings = []

        for _ in range(k):
            parts = list(map(int, lines[index].split()))
            index += 1

            p = parts[0]
            left = parts[1:1 + p]
            right = parts[1 + p:1 + 2 * p]

            result = lines[index]
            index += 1

            weighings.append((left, right, result))

        answers.append(str(find_fake_coin(n, weighings)))

    return "\n\n".join(answers)


def main() -> None:
    import sys
    input_data = sys.stdin.read()
    print(solve(input_data))


if __name__ == "__main__":
    main()
from typing import List, Tuple
import sys


Student = Tuple[str, int, int]


def parse_students(input_text: str) -> Tuple[int, int, List[Student]]:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return 0, 0, []

    n, k = map(int, lines[0].split())
    students: List[Student] = []

    for line in lines[1:1 + n]:
        name, score, age = line.split()
        students.append((name, int(score), int(age)))

    return n, k, students


def rank_students(students: List[Student]) -> List[Student]:
    return sorted(students, key=lambda student: (-student[1], student[2], student[0]))


def format_students(students: List[Student]) -> str:
    return "\n".join(f"{name} {score} {age}" for name, score, age in students)


def solve(input_text: str) -> str:
    _, k, students = parse_students(input_text)
    ranked = rank_students(students)
    selected = ranked[:k]
    return format_students(selected)


def main() -> None:
    input_text = sys.stdin.read()
    print(solve(input_text), end="")


if __name__ == "__main__":
    main()
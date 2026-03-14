from collections import Counter, defaultdict
from typing import Dict, List, Tuple
import sys


LogRecord = Tuple[str, str]


def parse_logs(input_text: str) -> List[LogRecord]:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return []

    m = int(lines[0])
    logs: List[LogRecord] = []

    for line in lines[1:1 + m]:
        user, action = line.split()
        logs.append((user, action))

    return logs


def count_user_events(logs: List[LogRecord]) -> Dict[str, int]:
    user_counts: Dict[str, int] = defaultdict(int)
    for user, _ in logs:
        user_counts[user] += 1
    return dict(user_counts)


def count_actions(logs: List[LogRecord]) -> Counter:
    action_counts: Counter = Counter()
    for _, action in logs:
        action_counts[action] += 1
    return action_counts


def sort_user_counts(user_counts: Dict[str, int]) -> List[Tuple[str, int]]:
    return sorted(user_counts.items(), key=lambda item: (-item[1], item[0]))


def get_top_action(action_counts: Counter) -> Tuple[str, int]:
    if not action_counts:
        return "None", 0

    action, count = sorted(action_counts.items(), key=lambda item: (-item[1], item[0]))[0]
    return action, count


def solve(input_text: str) -> str:
    logs = parse_logs(input_text)

    user_counts = count_user_events(logs)
    action_counts = count_actions(logs)

    sorted_users = sort_user_counts(user_counts)
    top_action, top_count = get_top_action(action_counts)

    output_lines = [f"{user} {count}" for user, count in sorted_users]
    output_lines.append(f"top_action: {top_action} {top_count}")

    return "\n".join(output_lines)


def main() -> None:
    input_text = sys.stdin.read()
    print(solve(input_text), end="")


if __name__ == "__main__":
    main()
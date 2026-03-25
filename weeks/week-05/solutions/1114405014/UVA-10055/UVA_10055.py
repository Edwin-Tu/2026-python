def flip_function(states: list[int], index: int) -> None:
    """
    將第 index 個函數的增減性反轉
    index 使用 1-based
    0 = increasing
    1 = decreasing
    """
    states[index - 1] ^= 1


def query_monotonicity(states: list[int], left: int, right: int) -> int:
    """
    查詢區間 [left, right] 複合函數的增減性
    若 decreasing 的個數為奇數 -> 回傳 1
    若 decreasing 的個數為偶數 -> 回傳 0
    """
    decreasing_count = sum(states[left - 1:right])
    return decreasing_count % 2


def solve(data: str) -> str:
    tokens = data.split()
    if not tokens:
        return ""

    n = int(tokens[0])
    q = int(tokens[1])
    index = 2

    # 一開始所有函數皆為 increasing
    states = [0] * n
    results = []

    for _ in range(q):
        op = int(tokens[index])
        index += 1

        if op == 1:
            i = int(tokens[index])
            index += 1
            flip_function(states, i)
        else:
            left = int(tokens[index])
            right = int(tokens[index + 1])
            index += 2
            results.append(str(query_monotonicity(states, left, right)))

    return "\n".join(results) + "\n"


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()), end="")
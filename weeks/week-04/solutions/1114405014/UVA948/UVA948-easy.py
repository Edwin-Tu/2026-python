from typing import List, Tuple

# 每次秤重的資料格式：
# (左盤硬幣列表, 右盤硬幣列表, 結果)
Weighing = Tuple[List[int], List[int], str]


def is_possible_fake(coin: int, is_heavier: bool, weighings: List[Weighing]) -> bool:
    """
    判斷某一枚硬幣是否可能是假幣

    參數：
    coin        → 要檢查的硬幣編號
    is_heavier  → True = 假設它比較重，False = 假設它比較輕
    weighings   → 所有秤重紀錄

    回傳：
    True  → 這個假設成立
    False → 不符合秤重結果
    """

    for left, right, result in weighings:
        # 計算左右盤重量
        left_weight = 0
        right_weight = 0

        # 計算左盤重量
        for c in left:
            if c == coin:
                # 如果是這枚假幣
                if is_heavier:
                    left_weight += 2  # 比較重
                else:
                    left_weight += 0  # 比較輕
            else:
                left_weight += 1  # 正常硬幣

        # 計算右盤重量
        for c in right:
            if c == coin:
                if is_heavier:
                    right_weight += 2
                else:
                    right_weight += 0
            else:
                right_weight += 1

        # 根據秤重結果判斷是否符合
        if result == "=":
            if left_weight != right_weight:
                return False

        elif result == "<":
            # 左邊比較輕
            if left_weight >= right_weight:
                return False

        elif result == ">":
            # 左邊比較重
            if left_weight <= right_weight:
                return False

    # 所有秤重都符合
    return True


def find_fake_coin(n: int, weighings: List[Weighing]) -> int:
    """
    找出唯一可能的假幣

    回傳：
    - 若只有一枚符合 → 回傳該編號
    - 否則 → 回傳 0
    """

    candidates = []  # 存所有可能是假幣的編號

    for coin in range(1, n + 1):

        # 檢查兩種可能：
        # 1. 比較重
        # 2. 比較輕
        if is_possible_fake(coin, True, weighings) or \
           is_possible_fake(coin, False, weighings):
            candidates.append(coin)

    # 只剩一個 → 找到了
    if len(candidates) == 1:
        return candidates[0]

    # 否則無法確定
    return 0


def solve(input_data: str) -> str:
    """
    主流程：解析輸入 → 計算答案 → 輸出結果
    """

    # 先把每行整理好
    lines = [line.strip() for line in input_data.splitlines()]
    index = 0

    # 跳過開頭空行
    while index < len(lines) and lines[index] == "":
        index += 1

    t = int(lines[index])  # 測試資料數量
    index += 1

    answers = []

    for _ in range(t):

        # 跳過空行
        while index < len(lines) and lines[index] == "":
            index += 1

        # 讀 N（硬幣數）和 K（秤重次數）
        n, k = map(int, lines[index].split())
        index += 1

        weighings = []

        # 讀取每次秤重
        for _ in range(k):
            parts = list(map(int, lines[index].split()))
            index += 1

            p = parts[0]  # 每邊放幾個硬幣
            left = parts[1:1 + p]
            right = parts[1 + p:1 + 2 * p]

            result = lines[index]  # 秤重結果
            index += 1

            weighings.append((left, right, result))

        # 計算答案
        answer = find_fake_coin(n, weighings)
        answers.append(str(answer))

    # 每組測資之間要空一行
    return "\n\n".join(answers)


def main() -> None:
    import sys
    input_data = sys.stdin.read()
    print(solve(input_data))


if __name__ == "__main__":
    main()
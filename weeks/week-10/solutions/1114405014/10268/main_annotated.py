#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UVA 10268 / UVA 10934 - Dropping water balloons

題目描述：
    有 k 個水球，建築物有 n 層樓。
    水球在某層樓會破（也可能不會破）。
    求在最糟糕情況下，找出臨界樓層所需的最少測試次數。

解題思路：
    1. 使用動態規劃解決經典的水球問題
    2. dp[t][e] = 使用 e 個水球、t 次測試能測試的最大樓層數
    3. 轉移：dp[t][e] = dp[t-1][e-1] + dp[t-1][e] + 1
        - dp[t-1][e-1]: 水球破了，向下一步
        - dp[t-1][e]: 水球沒壞，向上一步
        - +1: 當前這層

演算法：
    - DP，時間複雜度 O(k * 答案)
    - 如果需要的次數 > 63，輸出特殊訊息
"""

from typing import Union

def min_trials(k: int, n: int) -> Union[int, str]:
    """
    計算最少測試次數

    參數：
        k: 水球數量
        n: 樓層數

    回傳：
        最少次數（整數）或 "More than 63 trials needed."
    """
    # 處理邊界情況
    if k <= 0 or n <= 0:
        return 0

    # 只有一顆水球，只能線性搜尋
    if k == 1:
        if n > 63:
            return "More than 63 trials needed."
        return n

    # 超過 63 次就輸出特殊訊息
    # 因為需要超過 63 trials 代表需要的次數 > 63
    max_trials = 63

    # dp[t] = 使用 t 次測試能測試的最大樓層數
    dp = [0] * (k + 1)

    t = 0
    while t <= k and t <= max_trials:
        # 更新 dp[t]（t 次測試，t 個水球）
        # 注意：我們需要找最小的 t 使得 dp[t] >= n
        new_dp = [0] * (k + 1)

        for e in range(1, min(t, k) + 1):
            new_dp[e] = dp[e] + dp[e - 1] + 1

            if new_dp[e] >= n:
                if t > max_trials:
                    return "More than 63 trials needed."
                return t

        dp = new_dp
        t += 1

    # 如果还没找到，检查是否超过63
    if t > max_trials:
        return "More than 63 trials needed."
    return t


def solve():
    """主解答函數"""
    import sys

    input_data = sys.stdin.read().strip().splitlines()

    output = []

    for line in input_data:
        parts = line.split()
        if len(parts) < 2:
            continue

        k = int(parts[0])
        n = int(parts[1])

        if k == 0:
            break

        result = min_trials(k, n)
        output.append(str(result))

    # 輸出結果
    for line in output:
        print(line)


if __name__ == "__main__":
    solve()
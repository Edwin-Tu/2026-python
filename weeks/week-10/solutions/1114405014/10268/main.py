#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UVA 10268 / UVA 10934 - Dropping water balloons
"""
from typing import Union

def min_trials(k: int, n: int) -> Union[int, str]:
    """计算所需的最少试验次数"""
    if k <= 0 or n <= 0:
        return 0

    if k == 1:
        return "More than 63 trials needed." if n > 63 else n

    dp = [0] * (k + 1)

    for t in range(1, 64):
        new_dp = [0] * (k + 1)
        for e in range(1, min(t, k) + 1):
            new_dp[e] = dp[e] + dp[e - 1] + 1
            if new_dp[e] >= n:
                return t
        dp = new_dp

    return "More than 63 trials needed."


def solve() -> None:
    """主求解函数"""
    import sys

    data = sys.stdin.read().splitlines()
    output = []

    for line in data:
        parts = line.split()
        if len(parts) < 2:
            continue

        k, n = map(int, parts)

        if k == 0:
            break

        output.append(str(min_trials(k, n)))

    sys.stdout.write('\n'.join(output))


if __name__ == "__main__":
    solve()
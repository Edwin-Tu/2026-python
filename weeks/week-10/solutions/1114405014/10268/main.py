#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UVA 10268 / UVA 10934 - Dropping water balloons
"""

from typing import Union

def min_trials(k: int, n: int) -> Union[int, str]:
    if k <= 0 or n <= 0:
        return 0

    if k == 1:
        if n > 63:
            return "More than 63 trials needed."
        return n

    max_trials = 63

    dp = [0] * (k + 1)

    t = 0
    while t <= k and t <= max_trials:
        new_dp = [0] * (k + 1)

        for e in range(1, min(t, k) + 1):
            new_dp[e] = dp[e] + dp[e - 1] + 1

            if new_dp[e] >= n:
                if t > max_trials:
                    return "More than 63 trials needed."
                return t

        dp = new_dp
        t += 1

    if t > max_trials:
        return "More than 63 trials needed."
    return t


def solve():
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

    for line in output:
        print(line)


if __name__ == "__main__":
    solve()
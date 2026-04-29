#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
"""
UVA 10252 / ZeroJudge a245 - 王老師愛兩條線
"""
from typing import List, Tuple

def find_min_distance_and_count(points: List[Tuple[int, int]]) -> Tuple[int, int]:
    """寻找最小曼哈顿距离和及其方案数"""
    if not points:
        return (0, 0)

    n = len(points)
    xs = sorted(p[0] for p in points)
    ys = sorted(p[1] for p in points)

    if n % 2 == 1:
        x_med = xs[n // 2]
        y_med = ys[n // 2]
        min_dist = sum(abs(p[0] - x_med) + abs(p[1] - y_med) for p in points)
        x_count = xs.count(x_med)
        y_count = ys.count(y_med)
        return (min_dist, x_count * y_count)

    x_low, x_high = xs[n // 2 - 1], xs[n // 2]
    y_low, y_high = ys[n // 2 - 1], ys[n // 2]

    min_dist = float('inf')
    for x in range(x_low, x_high + 1):
        for y in range(y_low, y_high + 1):
            dist = sum(abs(p[0] - x) + abs(p[1] - y) for p in points)
            min_dist = min(min_dist, dist)

    count = sum(1 for x in range(x_low, x_high + 1)
                   for y in range(y_low, y_high + 1)
                   if sum(abs(p[0] - x) + abs(p[1] - y) for p in points) == min_dist)

    return (min_dist, count)


def solve() -> None:
    """主求解函数"""
    import sys

    data = sys.stdin.read().splitlines()
    if not data:
        return

    t = int(data[0])
    idx = 1
    output = []

    for _ in range(t):
        while idx < len(data) and not data[idx].strip():
            idx += 1

        n = int(data[idx])
        idx += 1

        points = []
        for _ in range(n):
            x, y = map(int, data[idx].split())
            idx += 1
            points.append((x, y))

        min_dist, count = find_min_distance_and_count(points)
        output.append(f"{min_dist} {count}")

    sys.stdout.write('\n'.join(output))


if __name__ == "__main__":
    solve()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UVA 10252 / ZeroJudge a245 - 王老師愛兩條線
"""

from typing import List, Tuple

def find_min_distance_and_count(points: List[Tuple[int, int]]) -> Tuple[int, int]:
    if not points:
        return (0, 0)

    n = len(points)

    xs = sorted([p[0] for p in points])
    ys = sorted([p[1] for p in points])

    mid_x_idx = n // 2
    mid_y_idx = n // 2

    if n % 2 == 1:
        x_median = xs[mid_x_idx]
        y_median = ys[mid_y_idx]

        x_count = xs.count(x_median)
        y_count = ys.count(y_median)

        min_dist = sum(abs(p[0] - x_median) + abs(p[1] - y_median) for p in points)

        return (min_dist, x_count * y_count)
    else:
        x_low = xs[mid_x_idx - 1]
        x_high = xs[mid_x_idx]

        y_low = ys[mid_y_idx - 1]
        y_high = ys[mid_y_idx]

        candidates = []
        for x in range(x_low, x_high + 1):
            for y in range(y_low, y_high + 1):
                dist = sum(abs(p[0] - x) + abs(p[1] - y) for p in points)
                candidates.append(dist)

        min_dist = min(candidates)

        count = sum(1 for d in candidates if d == min_dist)

        return (min_dist, count)


def solve():
    import sys

    input_data = sys.stdin.read().strip().splitlines()

    if not input_data:
        return

    t = int(input_data[0])
    line_idx = 1

    output = []

    for case in range(t):
        while line_idx < len(input_data) and not input_data[line_idx].strip():
            line_idx += 1

        n = int(input_data[line_idx])
        line_idx += 1

        points = []
        for _ in range(n):
            x, y = map(int, input_data[line_idx].split())
            line_idx += 1
            points.append((x, y))

        min_dist, count = find_min_distance_and_count(points)
        output.append(f"{min_dist} {count}")

    for line in output:
        print(line)


if __name__ == "__main__":
    solve()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UVA 10252 / ZeroJudge a245 - 王老師愛兩條線

題目描述：
    給定 N 個點，找出到所有點的曼哈頓距離和最小的整數點 P。
    輸出最小的距離和以及產生此距離和的整數點數量。

解題思路：
    1. 曼哈頓距離：|x1-x2| + |y1-y2|
    2. x 和 y 座標可以分開考慮
    3. 最小距離的 x 座標為所有 x 座標的中位數（可有多個）
    4. 最小距離的 y 座標為所有 y 座標的中位數（可有多個）
    5. 總方法數 = x 中位數方法數 * y 中位數方法數

演算法：
    - 分別找出 x 和 y 座標的中位數及其出现次數
    - 計算最小曼哈頓距離和
    - 計算方法數
"""

from typing import List, Tuple

def find_min_distance_and_count(points: List[Tuple[int, int]]) -> Tuple[int, int]:
    """
    找出最小曼哈頓距離和與方法數

    參數：
        points: 點的列表，每個點為 (x, y)

    回傳：
        (最小距離和, 方法數)
    """
    if not points:
        return (0, 0)

    n = len(points)

    # 分離 x 和 y 座標
    xs = sorted([p[0] for p in points])
    ys = sorted([p[1] for p in points])

    # 找出中位數的位置
    mid_x_idx = n // 2
    mid_y_idx = n // 2

    # 如果 n 為奇數，只有唯一中位數
    if n % 2 == 1:
        # 奇數個點
        x_median = xs[mid_x_idx]
        y_median = ys[mid_y_idx]

        # 計算方法數
        x_count = xs.count(x_median)
        y_count = ys.count(y_median)

        # 計算最小距離
        min_dist = sum(abs(p[0] - x_median) + abs(p[1] - y_median) for p in points)

        return (min_dist, x_count * y_count)
    else:
        # 偶數個點，中位數可以是某個範圍
        # x 中位數可以是 xs[mid_x_idx-1] 到 xs[mid_x_idx] 之間的任意整數
        x_low = xs[mid_x_idx - 1]
        x_high = xs[mid_x_idx]

        y_low = ys[mid_y_idx - 1]
        y_high = ys[mid_y_idx]

        # 計算每個候選點的距離
        candidates = []
        for x in range(x_low, x_high + 1):
            for y in range(y_low, y_high + 1):
                dist = sum(abs(p[0] - x) + abs(p[1] - y) for p in points)
                candidates.append(dist)

        min_dist = min(candidates)

        # 計算方法數
        count = sum(1 for d in candidates if d == min_dist)

        return (min_dist, count)


def solve():
    """主解答函數"""
    import sys

    input_data = sys.stdin.read().strip().splitlines()

    if not input_data:
        return

    t = int(input_data[0])
    line_idx = 1

    output = []

    for case in range(t):
        # 跳過可能的空行
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

    # 輸出結果
    for line in output:
        print(line)


if __name__ == "__main__":
    solve()
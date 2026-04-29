#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UVA 10235 / ZeroJudge a228 - 就少一個插座用很不方便

題目描述：
    在 N*M 的網格上放置蛇，每隻蛇形成一個環狀。
    有插座的格子不能被佔據，其餘格子必須被蛇佔據。
    計算所有可能的放置方法數（MOD 1000000007）。

解題思路：
    1. 這是一個狀態壓縮 DP 問題
    2. 將網格中的空格（無插座）編號
    3. 使用 DP 枚舉所有可能的環狀覆蓋

演算法：
    - 狀態壓縮 DP
    - 使用 bitmask 表示已覆蓋的格子
    - 轉移：選擇一個未覆蓋的格子，嘗試與相鄰格子形成環
"""

MOD = 1000000007

def count_socket_arrangements(grid):
    """
    計算在網格中放置蛇的方法數

    參數：
        grid: 二維列表，1 表示空格，0 表示插座

    回傳：
        放置方法數（已取 MOD）
    """
    n = len(grid)
    m = len(grid[0])

    # 收集所有空格位置
    empty_cells = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                empty_cells.append((i, j))

    # 使用 DP，狀態為已覆蓋的格子集合
    dp = [0] * (1 << len(empty_cells))
    dp[0] = 1

    # 將每個空格位置對應到索引
    cell_to_idx = {cell: idx for idx, cell in enumerate(empty_cells)}

    for mask in range(1 << len(empty_cells)):
        if dp[mask] == 0:
            continue

        # 找到第一個未被覆蓋的格子
        first_unset = -1
        for i in range(len(empty_cells)):
            if not (mask & (1 << i)):
                first_unset = i
                break

        if first_unset == -1:
            continue

        x1, y1 = empty_cells[first_unset]

        # 嘗試四個方向的相鄰格子形成環
        for direction in range(4):
            x2 = x1
            y2 = y1

            if direction == 0:
                x2 += 1  # 向下
            elif direction == 1:
                x2 -= 1  # 向上
            elif direction == 2:
                y2 += 1  # 向右
            else:
                y2 -= 1  # 向左

            # 檢查相鄰格子是否為空格
            if 0 <= x2 < n and 0 <= y2 < m and grid[x2][y2] == 1:
                idx2 = cell_to_idx[(x2, y2)]

                # 形成環：選擇這兩個格子
                new_mask = mask | (1 << first_unset) | (1 << idx2)
                dp[new_mask] = (dp[new_mask] + dp[mask]) % MOD

    # 統計所有狀態（所有格子都被覆蓋的情況）
    result = sum(dp) % MOD

    return result


def solve():
    """主解答函數"""
    import sys

    input_data = sys.stdin.read().strip().split('\n')

    if not input_data:
        return

    t = int(input_data[0])
    output = []
    line_idx = 1

    for case in range(1, t + 1):
        # 讀取 N 和 M
        parts = input_data[line_idx].split()
        line_idx += 1
        n, m = int(parts[0]), int(parts[1])

        # 讀取網格
        grid = []
        for _ in range(n):
            row = list(map(int, input_data[line_idx].split()))
            line_idx += 1
            grid.append(row)

        # 計算結果
        result = count_socket_arrangements(grid)
        output.append(f"Case {case}: {result}")

    # 輸出結果
    for line in output:
        print(line)


if __name__ == "__main__":
    solve()

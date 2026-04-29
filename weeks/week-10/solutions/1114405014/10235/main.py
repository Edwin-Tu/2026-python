#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UVA 10235 / ZeroJudge a228 - 就少一個插座用很不方便
"""
from typing import List

MOD = 1000000007

def count_socket_arrangements(grid: List[List[int]]) -> int:
    """统计插座排列方式数量"""
    n = len(grid)
    m = len(grid[0])

    empty_cells = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]
    cell_count = len(empty_cells)

    if cell_count == 0:
        return 1

    cell_to_idx = {cell: idx for idx, cell in enumerate(empty_cells)}
    dp = [0] * (1 << cell_count)
    dp[0] = 1

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for mask in range(1 << cell_count):
        if dp[mask] == 0:
            continue

        first_unset = next((i for i in range(cell_count) if not (mask & (1 << i))), None)
        if first_unset is None:
            continue

        x1, y1 = empty_cells[first_unset]

        for dx, dy in directions:
            x2, y2 = x1 + dx, y1 + dy
            if 0 <= x2 < n and 0 <= y2 < m and grid[x2][y2] == 1:
                idx2 = cell_to_idx.get((x2, y2))
                if idx2 is not None and not (mask & (1 << idx2)):
                    new_mask = mask | (1 << first_unset) | (1 << idx2)
                    dp[new_mask] = (dp[new_mask] + dp[mask]) % MOD

    return sum(dp) % MOD


def solve() -> None:
    """主求解函数"""
    import sys

    data = sys.stdin.read().splitlines()
    if not data:
        return

    t = int(data[0])
    output = []
    idx = 1

    for case in range(1, t + 1):
        n, m = map(int, data[idx].split())
        idx += 1

        grid = [list(map(int, data[idx + i].split())) for i in range(n)]
        idx += n

        result = count_socket_arrangements(grid)
        output.append(f"Case {case}: {result}")

    sys.stdout.write('\n'.join(output))


if __name__ == "__main__":
    solve()
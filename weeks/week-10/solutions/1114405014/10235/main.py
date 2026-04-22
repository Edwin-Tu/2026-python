#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UVA 10235 / ZeroJudge a228 - 就少一個插座用很不方便
"""

MOD = 1000000007

def count_socket_arrangements(grid):
    n = len(grid)
    m = len(grid[0])

    empty_cells = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                empty_cells.append((i, j))

    dp = [0] * (1 << len(empty_cells))
    dp[0] = 1

    cell_to_idx = {cell: idx for idx, cell in enumerate(empty_cells)}

    for mask in range(1 << len(empty_cells)):
        if dp[mask] == 0:
            continue

        first_unset = -1
        for i in range(len(empty_cells)):
            if not (mask & (1 << i)):
                first_unset = i
                break

        if first_unset == -1:
            continue

        x1, y1 = empty_cells[first_unset]

        for direction in range(4):
            x2 = x1
            y2 = y1

            if direction == 0:
                x2 += 1
            elif direction == 1:
                x2 -= 1
            elif direction == 2:
                y2 += 1
            else:
                y2 -= 1

            if 0 <= x2 < n and 0 <= y2 < m and grid[x2][y2] == 1:
                idx2 = cell_to_idx[(x2, y2)]

                new_mask = mask | (1 << first_unset) | (1 << idx2)
                dp[new_mask] = (dp[new_mask] + dp[mask]) % MOD

    result = sum(dp) % MOD
    return result


def solve():
    import sys

    input_data = sys.stdin.read().strip().split('\n')

    if not input_data:
        return

    t = int(input_data[0])
    output = []
    line_idx = 1

    for case in range(1, t + 1):
        parts = input_data[line_idx].split()
        line_idx += 1
        n, m = int(parts[0]), int(parts[1])

        grid = []
        for _ in range(n):
            row = list(map(int, input_data[line_idx].split()))
            line_idx += 1
            grid.append(row)

        result = count_socket_arrangements(grid)
        output.append(f"Case {case}: {result}")

    for line in output:
        print(line)


if __name__ == "__main__":
    solve()
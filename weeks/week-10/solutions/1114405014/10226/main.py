#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from typing import List, Set

def generate_permutations(n: int, forbidden: List[Set[int]]) -> List[str]:
    """生成所有有效的排列"""
    current: List[int] = []
    result: List[str] = []

    def backtrack():
        pos = len(current)
        if pos == n:
            result.append(''.join(chr(ord('A') + x) for x in current))
            return

        for person in range(n):
            if person in current:
                continue
            if pos in forbidden[person]:
                continue
            current.append(person)
            backtrack()
            current.pop()

    backtrack()
    result.sort()
    return result


def output_diff(prev: str, curr: str) -> str:
    """计算两个字符串的差异部分"""
    for i, (c1, c2) in enumerate(zip(prev, curr)):
        if c1 != c2:
            return curr[i:]
    return curr[len(prev):]


def solve() -> str:
    """主求解函数"""
    data = sys.stdin.read().splitlines()
    output_lines: List[str] = []
    idx = 0

    while idx < len(data):
        line = data[idx].strip()
        idx += 1

        if not line:
            continue

        n = int(line)
        forbidden: List[Set[int]] = [set() for _ in range(n)]

        for person in range(n):
            if idx >= len(data):
                break
            parts = data[idx].strip().split()
            idx += 1

            for p in parts:
                pos = int(p)
                if pos == 0:
                    break
                forbidden[person].add(pos - 1)

        permutations = generate_permutations(n, forbidden)

        prev = ""
        for perm in permutations:
            diff = output_diff(prev, perm)
            if diff:
                output_lines.append(diff)
            prev = perm

        if idx < len(data) and data[idx:]:
            output_lines.append("")

    while output_lines and output_lines[-1] == "":
        output_lines.pop()

    return '\n'.join(output_lines)


if __name__ == "__main__":
    print(solve(), end='')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from typing import List, Dict, Set

def generate_permutations(n: int, forbidden: Dict[int, List[int]]) -> List[str]:
    forbidden_sets: List[Set[int]] = [set(f) for f in forbidden]
    current: List[int] = []
    used: List[bool] = [False] * n
    result: List[str] = []

    def backtrack():
        if len(current) == n:
            result.append(''.join(chr(ord('A') + x) for x in current))
            return

        for person in range(n):
            if person in current:
                continue
            pos = len(current)
            if pos in forbidden_sets[person]:
                continue
            current.append(person)
            backtrack()
            current.pop()

    backtrack()
    result.sort()
    return result


def output_diff(prev: str, curr: str) -> str:
    i = 0
    while i < len(prev) and i < len(curr) and prev[i] == curr[i]:
        i += 1
    return curr[i:]


def solve() -> str:
    data = sys.stdin.read().strip().splitlines()
    output_lines: List[str] = []
    idx = 0

    while idx < len(data):
        if not data[idx].strip():
            idx += 1
            continue

        n_line = data[idx].strip()
        idx += 1

        if not n_line:
            continue

        n = int(n_line)
        forbidden: Dict[int, List[int]] = {i: [] for i in range(n)}

        for person in range(n):
            while idx < len(data) and not data[idx].strip():
                idx += 1
            if idx >= len(data):
                break

            parts = data[idx].strip().split()
            idx += 1

            positions: List[int] = []
            for p in parts:
                pos = int(p)
                if pos == 0:
                    break
                positions.append(pos - 1)

            forbidden[person] = positions

        permutations = generate_permutations(n, forbidden)

        prev = ""
        for perm in permutations:
            diff = output_diff(prev, perm)
            if diff:
                output_lines.append(diff)
            prev = perm

        if idx < len(data):
            output_lines.append("")

    while output_lines and output_lines[-1] == "":
        output_lines.pop()

    return '\n'.join(output_lines)


if __name__ == "__main__":
    result = solve()
    print(result, end='')

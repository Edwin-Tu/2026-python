#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UVA 10242 / ZeroJudge a235 - APIO2009 抢掠计划
"""
from collections import deque
from typing import List, Tuple

INF = float('-inf')

def find_max_robbery(n: int, edges: List[Tuple[int, int]], values: List[int], s: int, pubs: List[int]) -> int:
    """使用SPFA算法寻找最大抢劫价值"""
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)

    dist = [INF] * (n + 1)
    dist[s] = values[s - 1]
    in_queue = [False] * (n + 1)
    queue = deque([s])
    in_queue[s] = True
    count = [0] * (n + 1)

    while queue:
        u = queue.popleft()
        in_queue[u] = False

        for v in graph[u]:
            new_dist = dist[u] + values[v - 1]
            if dist[v] < new_dist:
                dist[v] = new_dist
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
                    count[v] += 1
                    if count[v] > n:
                        return -1

    return max((dist[pub] for pub in pubs), default=INF)


def solve() -> None:
    """主求解函数"""
    import sys

    data = sys.stdin.read().splitlines()
    if not data:
        return

    n, m = map(int, data[0].split())
    edges = [tuple(map(int, data[i].split())) for i in range(1, m + 1)]
    values = [int(data[i]) for i in range(m + 1, m + n + 1)]

    s, p = map(int, data[m + n + 1].split())
    pubs = list(map(int, data[m + n + 2].split())) if p > 0 else []

    result = find_max_robbery(n, edges, values, s, pubs)
    print(result)


if __name__ == "__main__":
    solve()
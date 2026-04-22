#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UVA 10242 / ZeroJudge a235 - APIO2009 抢掠计划
"""

import collections

def find_max_robbery(n, edges, values, s, pubs):
    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]

    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)

    dist = [-10**18] * (n + 1)
    dist[s] = values[s - 1]
    in_queue = [False] * (n + 1)
    queue = collections.deque([s])
    in_queue[s] = True
    count = [0] * (n + 1)

    while queue:
        u = queue.popleft()
        in_queue[u] = False

        for v in graph[u]:
            if dist[v] < dist[u] + values[v - 1]:
                dist[v] = dist[u] + values[v - 1]
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
                    count[v] += 1
                    if count[v] > n:
                        return -1

    result = -10**18
    for pub in pubs:
        if dist[pub] > result:
            result = dist[pub]

    return result


def solve():
    import sys

    input_data = sys.stdin.read().strip().splitlines()

    if not input_data:
        return

    n, m = map(int, input_data[0].split())
    edges = []

    for i in range(1, m + 1):
        u, v = map(int, input_data[i].split())
        edges.append((u, v))

    values = []
    for i in range(m + 1, m + n + 1):
        values.append(int(input_data[i]))

    s_p_line = input_data[m + n + 1].split()
    s = int(s_p_line[0])
    p = int(s_p_line[1])

    pubs = []
    if p > 0:
        pubs = list(map(int, input_data[m + n + 2].split()))

    result = find_max_robbery(n, edges, values, s, pubs)

    print(result)


if __name__ == "__main__":
    solve()
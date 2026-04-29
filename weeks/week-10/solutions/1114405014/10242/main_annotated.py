#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UVA 10242 / ZeroJudge a235 - APIO2009 抢掠计划

題目描述：
    在 Siruseri 城中，每個路口有 ATM 提款機。
    搶劫者從市中心出發，沿著單向道路行駛，搶劫途經的 ATM。
    每台 ATM 只能被搶一次，最終要在酒吧結束。
    求最多能搶到的金額。

解題思路：
    1. 這是帶有負權重的最短路徑問題的變體
    2. 使用 SPFA 或 Bellman-Ford 演算法
    3. 酒吧節點作為終點，求最大路徑和

演算法：
    - 將問題轉換為最大路徑問題
    - 使用 SPFA（改良式 Bellman-Ford）
    - 如果存在正環，則可以無限搶劫
"""

def find_max_robbery(n, edges, values, s, pubs):
    """
    計算最大搶劫金額

    參數：
        n: 節點數量
        edges: 邊列表，每條邊為 (起點, 終點)
        values: 每個節點的 ATM 金額
        s: 起點（市中心）
        pubs: 酒吧節點列表

    回傳：
        最大搶劫金額
    """
    import collections

    # 建立鄰接表（正向和反向）
    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]

    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)

    # 使用 SPFA 計算從起點到每個節點的最大路徑
    # 初始化：距離為負無限，起點為自身的 ATM 金額
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
            # 嘗試更新到 v 的路徑
            if dist[v] < dist[u] + values[v - 1]:
                dist[v] = dist[u] + values[v - 1]
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
                    count[v] += 1
                    # 如果某節點被更新超過 n 次，存在正環
                    if count[v] > n:
                        return -1

    # 找出酒吧節點中的最大金額
    result = -10**18
    for pub in pubs:
        if dist[pub] > result:
            result = dist[pub]

    return result


def solve():
    """主解答函數"""
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
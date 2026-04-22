#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UVA 10226 / ZeroJudge a219 - 限制排列

題目描述：
    給定 N 個人 (編號 A, B, ...)，每個人可能不想站在某些位置。
    請輸出所有可能的排列（依照字典順序），但僅輸出與上次排列不同的部分。

解題思路：
    1. 使用 DFS 生成所有符合條件的排列
    2. 使用回溯法 (Backtracking) 進行剪枝
    3. 對於連續的排列，只輸出不同的部分

演算法：
    - 使用深度優先搜尋 (DFS) 枚舉所有排列
    - 使用集合記錄每個人不願意站的位置
    - 對每個排列，與前一個排列比較，只輸出差異部分
"""

import sys
from typing import List, Dict, Set

def generate_permutations(n: int, forbidden: Dict[int, List[int]]) -> List[str]:
    """
    生成所有符合條件的排列

    參數：
        n: 人的數量 (1 <= n <= 15)
        forbidden: 字典，key 為人的編號 (0 到 n-1)，value 為該人不願意站的位置列表

    回傳：
        所有有效排列的字串列表
    """
    # 將禁止位置轉換為集合以加快查詢速度
    forbidden_sets: List[Set[int]] = [set(f) for f in forbidden]

    # 記錄當前排列
    current: List[int] = []
    # 記錄每個位置是否已被佔用
    used: List[bool] = [False] * n
    # 儲存所有結果
    result: List[str] = []

    def backtrack():
        """使用回溯法生成所有排列"""
        # 如果已經選夠 n 個人，將排列轉換為字串並儲存
        if len(current) == n:
            # 將數字編號轉換為字母 (0 -> 'A', 1 -> 'B', ...)
            result.append(''.join(chr(ord('A') + x) for x in current))
            return

        # 嘗試將每個人放入下一個位置
        for person in range(n):
            # 檢查這個人是否已被選過
            if person in current:
                continue

            # 檢查這個人是否不願意站在這個位置
            pos = len(current)
            if pos in forbidden_sets[person]:
                continue

            # 選這個人
            current.append(person)
            # 遞迴處理下一個位置
            backtrack()
            # 撤銷選擇（回溯）
            current.pop()

    # 開始生成排列
    backtrack()

    # 依照字典順序排序輸出
    result.sort()

    return result


def output_diff(prev: str, curr: str) -> str:
    """
    輸出兩個排列之間不同的部分

    參數：
        prev: 前一個排列
        curr: 目前的排列

    回傳：
        從第一個不同字元開始的所有字元
    """
    # 找出第一個不同的位置
    i = 0
    while i < len(prev) and i < len(curr) and prev[i] == curr[i]:
        i += 1

    # 從該位置開始輸出所有字元
    return curr[i:]


def solve() -> str:
    """
    主解答函數

    回傳：
        輸出的字串
    """
    # 讀取所有輸入
    data = sys.stdin.read().strip().splitlines()

    # 用於儲存輸出結果
    output_lines: List[str] = []

    # 索引指標
    idx = 0

    while idx < len(data):
        # 跳過空行
        if not data[idx].strip():
            idx += 1
            continue

        # 讀取 N
        n_line = data[idx].strip()
        idx += 1

        if not n_line:
            continue

        n = int(n_line)

        # 讀取每個人的禁止位置
        forbidden: Dict[int, List[int]] = {i: [] for i in range(n)}

        for person in range(n):
            # 處理可能存在的空行
            while idx < len(data) and not data[idx].strip():
                idx += 1

            if idx >= len(data):
                break

            # 讀取該人的禁止位置
            parts = data[idx].strip().split()
            idx += 1

            # 解析每個位置直到遇到 0
            positions: List[int] = []
            for p in parts:
                pos = int(p)
                if pos == 0:
                    break
                positions.append(pos - 1)  # 轉換為 0 索引

            forbidden[person] = positions

        # 產生所有排列
        permutations = generate_permutations(n, forbidden)

        # 輸出結果
        prev = ""
        for perm in permutations:
            diff = output_diff(prev, perm)
            if diff:
                output_lines.append(diff)
            prev = perm

        # 每筆測資後輸出空行（除了最後一筆）
        if idx < len(data):
            output_lines.append("")

    # 移除最後多餘的空行
    while output_lines and output_lines[-1] == "":
        output_lines.pop()

    return '\n'.join(output_lines)


if __name__ == "__main__":
    # 測試範例輸入
    test_input = """3
0
0
0
3
1 0
3 0
0
"""

    # 執行解答並輸出結果
    result = solve()
    print(result, end='')

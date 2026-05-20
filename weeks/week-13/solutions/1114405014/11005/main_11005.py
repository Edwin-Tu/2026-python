# 題目：UVA 11005 - Cheapest Base
# 給定 36 個字元 (0-9, A-Z) 的印刷成本，
# 對於每個查詢數字 N (十進位)，找出 2~36 進位中，
# 印刷成本最低的進位制（一個或多個）。

import sys

cost_table = []


def cheapest_base(costs, n):
    """
    計算數字 n 在 2~36 進位中，哪個進位的印刷成本最低。
    :param costs: list[int] 長度 36，依序為 '0'~'9', 'A'~'Z' 的單位成本
    :param n: int 要查詢的十進位數字 (0 ≤ N ≤ 2,000,000,000)
    :return: list[int] 成本最低的進位制列表（升序排列）
    """
    # 待實作 TDD — Phase 2 Green
    raise NotImplementedError("Implement this function")


def main():
    """
    主程式：讀取標準輸入，解析測資，呼叫 cheapest_base 並輸出結果。
    輸入格式：
        - 第一行：測試資料組數 T
        - 每組測試：
          - 前 4 行各 9 個整數，共 36 個（0~9, A~Z 成本）
          - 一行：查詢數量 Q
          - Q 行：每行一個十進位數字 N
    輸出格式：
        Case X:
        Cheapest base(s) for number Y: b1 b2 ...
        （組間空一行）
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])                # 測試資料組數
    idx = 1
    for case_no in range(1, t + 1):
        # 讀取 36 個字元成本
        costs = list(map(int, data[idx:idx + 36]))
        idx += 36
        q = int(data[idx]); idx += 1   # 查詢數量
        print(f"Case {case_no}:")
        for _ in range(q):
            n = int(data[idx]); idx += 1
            bases = cheapest_base(costs, n)
            # 輸出格式：Cheapest base(s) for number Y: b1 b2 ...
            print(f"Cheapest base(s) for number {n}:", *bases)
        if case_no < t:
            print()   # 組間空行


if __name__ == "__main__":
    main()

# 題目：UVA 11150 - Frog Crossing Bridge (獨木橋上的青蛙)
# 河上有一座長度 L 的獨木橋，青蛙從 0 出發跳到 L（含跳過即算成功）。
# 每次可跳 S~T 的任意整數距離，橋上有 M 個石子（討厭踩到）。
# 目標：計算最少需要踩到的石子數。
#
# 限制：L 可達 10^9，但 M ≤ 100，S,T ≤ 10，
#       需使用路徑壓縮 (path compression) 後再做 DP。

import sys


def min_stones(L, S, T, stones):
    """
    計算青蛙過河最少需要踩到的石子數。
    :param L: int 橋樑長度 (1 ≤ L ≤ 10^9)
    :param S: int 最小跳躍距離 (1 ≤ S ≤ T ≤ 10)
    :param T: int 最大跳躍距離
    :param stones: list[int] 石子位置列表，已排序、不重複、不含 0 與 L
    :return: int 最少踩到的石子數
    """
    # 待實作 TDD — Phase 2 Green
    # 提示：當 T - S >= 0 或石子間距過大時，需要壓縮距離
    raise NotImplementedError("Implement this function")


def main():
    """
    主程式：讀取標準輸入，解析測資，呼叫 min_stones 並輸出結果。
    輸入格式：
        - 第一行：L
        - 第二行：S T M（M 為石子數量）
        - 第三行：M 個整數，石子位置
    輸出格式：
        - 一個整數，最少踩到的石子數
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    # 可能含多組測資
    while idx < len(data):
        L = int(data[idx]); idx += 1
        if idx >= len(data):
            break
        S = int(data[idx]); T = int(data[idx + 1]); M = int(data[idx + 2])
        idx += 3
        stones = []
        for _ in range(M):
            stones.append(int(data[idx])); idx += 1
        print(min_stones(L, S, T, stones))


if __name__ == "__main__":
    main()

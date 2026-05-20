# 題目：UVA 11321 - 茵可的陷阱 (Trap Placement)
# N×M 的柏油路，起點在左邊，茵可家在右邊。
# 茵可要放置陷阱（不可放在已放置的點），但不能讓道路封死。
# （封死 = 不存在任何從左邊界到右邊界的路徑）
# 判斷每個陷阱能否放置。
#
# 注意：x 軸為縱軸（列），y 軸為橫軸（行），左下角為 (0,0)。

import sys


def can_place_trap(N, M, traps):
    """
    依序判斷每個陷阱能否放置而不封死道路。
    :param N: int 網格列數（x 軸方向）
    :param M: int 網格行數（y 軸方向）
    :param traps: list[tuple[int,int]] 依序要放置的陷阱座標 (x, y)
    :return: list[str] 每個陷阱的結果：
             - "<(_ _)>"  可放置
             - ">_<"      不可放置（會封死道路）
    """
    # 待實作 TDD — Phase 2 Green
    # 提示：使用 BFS/DFS 檢查放置後是否仍有左到右路徑，
    #       或使用並查集 (DSU) 檢查是否形成上下連通阻斷。
    raise NotImplementedError("Implement this function")


def main():
    """
    主程式：讀取標準輸入，解析陷阱座標，呼叫 can_place_trap 並輸出結果。
    輸入格式：
        - 第一行：N M T（T 為陷阱數量）
        - 接下來 T 行：每行 x y 表示陷阱座標
    輸出格式：
        - 每個陷阱輸出一行：可放置為 "<(_ _)>"，不可為 ">_<"
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    # 可能含多組測資
    while idx < len(data):
        N = int(data[idx]); M = int(data[idx + 1]); T = int(data[idx + 2])
        idx += 3
        traps = []
        for _ in range(T):
            x = int(data[idx]); y = int(data[idx + 1])
            idx += 2
            traps.append((x, y))
        results = can_place_trap(N, M, traps)
        for r in results:
            print(r)


if __name__ == "__main__":
    main()

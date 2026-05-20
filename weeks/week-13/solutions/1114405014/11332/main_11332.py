# 題目：UVA 11332 - Mirror Visibility (鏡子可見度)
# 某 M 在原點 (0,0)，四周有許多鏡子（線段）。
# 每個鏡子由兩個端點 (sx,sy) ~ (ex,ey) 定義。
# 判斷從原點能否看到每個鏡子的「至少一小段區域」。
# （不考慮反射，鏡子之間不會相交，也不通過原點）

import sys


def visible_mirrors(mirrors):
    """
    判斷從原點 (0,0) 可以看到哪些鏡子。
    :param mirrors: list[tuple[int,int,int,int]]
                    每個元素為 (sx, sy, ex, ey) 表示線段端點
    :return: list[int] 每個鏡子 0 (不可見) / 1 (可見)
    """
    # 待實作 TDD — Phase 2 Green
    # 提示：對每個鏡子，判斷從原點出發的射線能否到達鏡子上的任意一點
    #       而不被其他鏡子遮擋。需考慮線段相交判斷與方向夾角。
    raise NotImplementedError("Implement this function")


def main():
    """
    主程式：讀取標準輸入，解析鏡子線段，呼叫 visible_mirrors 並輸出結果。
    輸入格式：
        - 多組測資，每組第一行為 n（鏡子數量）
        - 接下來 n 行，每行 4 個整數 sx sy ex ey
    輸出格式：
        - 每組一行，n 個 0/1 整數，以空格分隔
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    while idx < len(data):
        n = int(data[idx]); idx += 1
        mirrors = []
        for _ in range(n):
            sx = int(data[idx]); sy = int(data[idx + 1])
            ex = int(data[idx + 2]); ey = int(data[idx + 3])
            idx += 4
            mirrors.append((sx, sy, ex, ey))
        result = visible_mirrors(mirrors)
        # 輸出格式：0 1 0 1 ...（以空格分隔）
        print(" ".join(str(v) for v in result))


if __name__ == "__main__":
    main()

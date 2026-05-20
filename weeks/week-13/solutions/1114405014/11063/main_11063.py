# 題目：UVA 11063 - RGB to XYZ
# 將 n×n 影像的 RGB 像素轉換為 XYZ 色空間，
# 並計算影像平均亮度 Y。
#
# 轉換公式：
#   X = 0.5149 * R + 0.3244 * G + 0.1607 * B
#   Y = 0.2654 * R + 0.6704 * G + 0.0642 * B
#   Z = 0.0248 * R + 0.1248 * G + 0.8504 * B

import sys


def rgb_to_xyz(pixels):
    """
    將 RGB 像素列表轉換為 XYZ 色空間。
    :param pixels: list[tuple[int,int,int]] 每個元素為 (R, G, B)，值域 0~255
    :return: tuple (xyz_list, avg_y)
             - xyz_list: list[tuple[float,float,float]] 每個像素的 (X, Y, Z)，四捨五入至小數第 4 位
             - avg_y: float 所有像素 Y 的平均值，四捨五入至小數第 4 位
    """
    # 待實作 TDD — Phase 2 Green
    raise NotImplementedError("Implement this function")


def main():
    """
    主程式：讀取標準輸入，解析像素資料，呼叫 rgb_to_xyz 並輸出結果。
    輸入格式：
        - 第一行：n (影像寬高，0 < n ≤ 256)
        - 接下來 n 行，每行 n 個像素，每個像素為 "R G B"
    輸出格式：
        - 每個像素一行："X Y Z"（小數點後 4 位）
        - 最後一行："The average of Y is 平均亮度"（小數點後 4 位）
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    case_no = 1
    # 支援多組測試資料（題目未明確說多組，但預留 while 迴圈）
    while idx < len(data):
        n = int(data[idx]); idx += 1                     # 影像寬高
        pixels = []
        for _ in range(n * n):
            r = int(data[idx]); g = int(data[idx + 1]); b = int(data[idx + 2])
            idx += 3
            pixels.append((r, g, b))
        print(f"Case {case_no}:")
        case_no += 1
        xyz_list, avg_y = rgb_to_xyz(pixels)
        for x, y, z in xyz_list:
            # 輸出至小數點後 4 位
            print(f"{x:.4f} {y:.4f} {z:.4f}")
        print(f"The average of Y is {avg_y:.4f}")


if __name__ == "__main__":
    main()

import sys

def can_expand(grid, m, n, r, c, size):
    # 取得中心點的字元，正方形內所有字元都必須與它相同
    ch = grid[r][c]
    top = r - size
    bottom = r + size
    left = c - size
    right = c + size

    # 若正方形超出邊界，代表不能再擴大
    if top < 0 or bottom >= m or left < 0 or right >= n:
        return False

    # 檢查目前正方形範圍內的每一格是否都相同
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if grid[i][j] != ch:
                return False
    return True

def solve():
    # 使用 splitlines 保留每一列字元網格
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    t = int(lines[0])
    idx = 1
    out = []

    for _ in range(t):
        # m 行、n 列、q 筆查詢
        m, n, q = map(int, lines[idx].split())
        idx += 1

        # 讀取字元網格
        grid = lines[idx:idx + m]
        idx += m

        # 題目要求每組測資先輸出 m n q
        out.append(f"{m} {n} {q}")

        for _ in range(q):
            r, c = map(int, lines[idx].split())
            idx += 1

            # radius 代表目前可以向外擴張幾圈
            radius = 0
            while can_expand(grid, m, n, r, c, radius + 1):
                radius += 1

            # 邊長 = 半徑 * 2 + 1
            out.append(str(radius * 2 + 1))

    print("\n".join(out))

if __name__ == "__main__":
    solve()

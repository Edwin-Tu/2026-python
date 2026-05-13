import sys

def can_expand(grid, m, n, r, c, size):
    ch = grid[r][c]
    top = r - size
    bottom = r + size
    left = c - size
    right = c + size
    if top < 0 or bottom >= m or left < 0 or right >= n:
        return False
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if grid[i][j] != ch:
                return False
    return True

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0])
    idx = 1
    out = []
    for _ in range(t):
        m, n, q = map(int, lines[idx].split())
        idx += 1
        grid = lines[idx:idx + m]
        idx += m
        out.append(f"{m} {n} {q}")
        for _ in range(q):
            r, c = map(int, lines[idx].split())
            idx += 1
            radius = 0
            while can_expand(grid, m, n, r, c, radius + 1):
                radius += 1
            out.append(str(radius * 2 + 1))
    print("\n".join(out))

if __name__ == "__main__":
    solve()

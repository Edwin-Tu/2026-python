t = int(input())

for _ in range(t):
    m, n, q = map(int, input().split())

    grid = [input().strip() for _ in range(m)]

    print(m, n, q)

    for _ in range(q):
        r, c = map(int, input().split())

        ch = grid[r][c]
        size = 1
        step = 1

        while True:
            top = r - step
            bottom = r + step
            left = c - step
            right = c + step

            if top < 0 or bottom >= m or left < 0 or right >= n:
                break

            ok = True

            for i in range(top, bottom + 1):
                for j in range(left, right + 1):
                    if grid[i][j] != ch:
                        ok = False
                        break
                if not ok:
                    break

            if not ok:
                break

            size += 2
            step += 1

        print(size)

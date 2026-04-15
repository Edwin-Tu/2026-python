def count_mines(grid, row, col, n, m):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '*':
            count += 1
    return count


def process_grid(grid, n, m):
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            if grid[i][j] == '*':
                row.append('*')
            else:
                row.append(count_mines(grid, i, j, n, m))
        result.append(row)
    return result


def solve():
    import sys
    lines = sys.stdin.read().strip().splitlines()
    idx = 0
    field_num = 1
    outputs = []
    
    while idx < len(lines):
        parts = lines[idx].split()
        idx += 1
        if len(parts) < 2:
            continue
        n, m = int(parts[0]), int(parts[1])
        if n == 0 and m == 0:
            break
        
        grid = []
        for _ in range(n):
            grid.append(list(lines[idx].strip()))
            idx += 1
        
        outputs.append(f"Field #{field_num}:")
        result = process_grid(grid, n, m)
        for row in result:
            outputs.append(''.join(str(cell) for cell in row))
        outputs.append('')
        field_num += 1
    
    sys.stdout.write('\n'.join(outputs))


if __name__ == "__main__":
    solve()
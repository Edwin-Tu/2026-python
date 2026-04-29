import unittest
from main_10235 import solve, count_socket_arrangements

class TestUVA10235(unittest.TestCase):
    def test_basic_count(self):
        """測試基本計數"""
        grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        result = count_socket_arrangements(grid)
        self.assertEqual(result, 3)

    def test_small_grid(self):
        """測試小網格"""
        grid = [[1, 1], [1, 1]]
        result = count_socket_arrangements(grid)
        self.assertEqual(result, 2)

    def test_all_sockets(self):
        """測試全部都是插座"""
        grid = [[0, 0], [0, 0]]
        result = count_socket_arrangements(grid)
        self.assertEqual(result, 1)

    def test_no_sockets_single_empty(self):
        """測試只有一個空格"""
        grid = [[1]]
        result = count_socket_arrangements(grid)
        self.assertEqual(result, 1)

    def test_solve_output_format(self):
        """測試輸出格式"""
        import io
        import sys
        input_data = "3\n6 3\n1 1 1\n1 0 1\n1 1 1\n1 1 1\n1 0 1\n1 1 1\n2 4\n1 1 1 1\n1 1 1 1\n1 1\n0\n"
        expected = "Case 1: 3\nCase 2: 2\nCase 3: 1\n"
        sys.stdin = io.StringIO(input_data)
        sys.stdout = io.StringIO()
        solve()
        self.assertEqual(sys.stdout.getvalue(), expected)

MOD = 1000000007

def solve():
    import sys
    input_data = sys.stdin.read().strip().split('\n')
    t = int(input_data[0])
    output = []
    line_idx = 1
    
    for case in range(1, t + 1):
        parts = input_data[line_idx].split()
        line_idx += 1
        n, m = int(parts[0]), int(parts[1])
        
        grid = []
        for _ in range(n):
            row = list(map(int, input_data[line_idx].split()))
            line_idx += 1
            grid.append(row)
        
        result = count_socket_arrangements(grid)
        output.append(f"Case {case}: {result}")
    
    sys.stdout = sys.__stdout__
    for line in output:
        print(line)

def count_socket_arrangements(grid):
    n = len(grid)
    m = len(grid[0])
    total_cells = n * m
    
    empty_cells = []
    socket_cells = []
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                empty_cells.append((i, j))
            else:
                socket_cells.append((i, j))
    
    dp = [0] * (1 << len(empty_cells))
    dp[0] = 1
    
    for mask in range(1 << len(empty_cells)):
        if dp[mask] == 0:
            continue
        
        first_unset = -1
        for i in range(len(empty_cells)):
            if not (mask & (1 << i)):
                first_unset = i
                break
        
        if first_unset == -1:
            continue
        
        x1, y1 = empty_cells[first_unset]
        
        for direction in range(4):
            x2 = x1
            y2 = y1
            valid = True
            
            if direction == 0:
                x2 += 1
            elif direction == 1:
                x2 -= 1
            elif direction == 2:
                y2 += 1
            else:
                y2 -= 1
            
            if 0 <= x2 < n and 0 <= y2 < m and grid[x2][y2] == 1:
                idx2 = empty_cells.index((x2, y2))
                new_mask = mask | (1 << first_unset) | (1 << idx2)
                dp[new_mask] = (dp[new_mask] + dp[mask]) % MOD
    
    result = 0
    for mask in range(1 << len(empty_cells)):
        result = (result + dp[mask]) % MOD
    
    return result

if __name__ == '__main__':
    solve()
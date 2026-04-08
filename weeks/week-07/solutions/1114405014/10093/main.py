import sys


def generate_valid_masks(M):
    masks = []
    for mask in range(1 << M):
        last = -3
        valid = True
        for j in range(M):
            if mask & (1 << j):
                if j - last < 3:
                    valid = False
                    break
                last = j
        if valid:
            masks.append(mask)
    return masks


def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    N = int(data[0])
    M = int(data[1])
    grid = []
    for i in range(N):
        grid.append(data[2 + i].strip())
    
    row_masks = []
    for i in range(N):
        mask = 0
        for j in range(M):
            if grid[i][j] == 'P':
                mask |= (1 << j)
        row_masks.append(mask)
    
    valid_masks = generate_valid_masks(M)
    
    if N == 0:
        print(0)
        return
    
    if N == 1:
        max_count = 0
        for m in valid_masks:
            if m & ~row_masks[0]:
                continue
            cnt = bin(m).count('1')
            max_count = max(max_count, cnt)
        print(max_count)
        return
    
    dp = [{} for _ in range(N)]
    
    for mask in valid_masks:
        if mask & ~row_masks[0]:
            continue
        cnt = bin(mask).count('1')
        dp[0][mask] = cnt
    
    for r in range(1, N):
        for mask2 in valid_masks:
            if mask2 & ~row_masks[r]:
                continue
            cnt2 = bin(mask2).count('1')
            
            for mask1, val1 in dp[r-1].items():
                if mask1 & mask2:
                    continue
                
                if r >= 2:
                    conflict = False
                    for mask0, _ in dp[r-2].items():
                        if mask0 & mask2:
                            conflict = True
                            break
                    if conflict:
                        continue
                
                new_val = val1 + cnt2
                if mask2 not in dp[r] or dp[r][mask2] < new_val:
                    dp[r][mask2] = new_val
    
    result = max(dp[N-1].values()) if dp[N-1] else 0
    print(result)


if __name__ == "__main__":
    solve()
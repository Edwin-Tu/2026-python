def find_min_b_plus_c(a):
    best = float('inf')
    a_sq = a * a
    
    for k in range(1, a + 1):
        if a_sq % k != 0:
            continue
        c = a + a_sq // k
        b = a + k
        best = min(best, b + c)
    
    return int(best)


def solve():
    import sys
    a = int(sys.stdin.read().strip())
    result = find_min_b_plus_c(a)
    print(result)


if __name__ == "__main__":
    solve()
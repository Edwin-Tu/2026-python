import sys
import math


def solve():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split()
        if len(parts) < 2:
            continue
            
        S = int(parts[0])
        D = int(parts[1])
        
        low = 1
        high = int(math.sqrt(2 * D)) + 100
        
        while low <= high:
            mid = (low + high) // 2
            total_days = mid * S + mid * (mid - 1) // 2
            
            if total_days >= D:
                result = S + mid - 1
                high = mid - 1
            else:
                low = mid + 1
        
        print(result)


if __name__ == "__main__":
    solve()
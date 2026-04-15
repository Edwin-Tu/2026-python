def calculate_umbrella_position(x, l, v, t, W):
    if v == 0:
        return max(0, x), min(x + l, W)
    
    total_distance = W - l
    if total_distance <= 0:
        return max(0, x), min(x + l, W)
    
    period = 2 * total_distance / abs(v)
    t_mod = t % period
    half_period = period / 2
    
    if t_mod <= half_period:
        left = x + v * t_mod
    else:
        left = x + v * (period - t_mod)
    
    left = max(0, min(left, W - l))
    right = min(left + l, W)
    
    return left, right


def calculate_rain_volume(umbrellas, W, T, V):
    dt = 0.1
    total_covered = 0
    
    for t in [i * dt for i in range(int(T / dt) + 1)]:
        intervals = []
        for x, l, v in umbrellas:
            left, right = calculate_umbrella_position(x, l, v, t, W)
            left = max(0, left)
            right = min(right, W)
            if right > left:
                intervals.append((left, right))
        
        intervals.sort()
        merged = []
        for a, b in intervals:
            if merged and a <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], b))
            else:
                merged.append((a, b))
        
        covered_length = sum(b - a for a, b in merged)
        covered_length = min(covered_length, W)
        total_covered += covered_length
    
    avg_covered = total_covered / (int(T / dt) + 1)
    uncovered = W - avg_covered
    
    return V * uncovered * T


def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    
    it = iter(input_data)
    N = int(next(it))
    W = int(next(it))
    T = int(next(it))
    V = int(next(it))
    
    umbrellas = []
    for _ in range(N):
        x = int(next(it))
        l = int(next(it))
        v = int(next(it))
        umbrellas.append((x, l, v))
    
    result = calculate_rain_volume(umbrellas, W, T, V)
    print(f"{result:.2f}")


if __name__ == "__main__":
    solve()
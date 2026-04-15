import math


def calculate_arc_length(r, a_rad):
    return r * a_rad


def calculate_chord_length(r, a_rad):
    return 2 * r * math.sin(a_rad / 2)


def solve():
    import sys
    lines = sys.stdin.read().strip().splitlines()
    
    for line in lines:
        if not line.strip():
            continue
        
        parts = line.strip().split()
        s = int(parts[0])
        a_val = int(parts[1])
        unit = parts[2]
        
        r = 6440 + s
        
        if unit == "deg":
            a_rad = math.radians(a_val)
        else:
            a_rad = math.radians(a_val / 60.0)
        
        arc = calculate_arc_length(r, a_rad)
        chord = calculate_chord_length(r, a_rad)
        
        print(f"{arc:.6f} {chord:.6f}")


if __name__ == "__main__":
    solve()
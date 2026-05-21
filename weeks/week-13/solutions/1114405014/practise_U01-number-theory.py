import math
import sys

def beat_the_spread(s: int, d: int):
    if (s + d) % 2 != 0:
        return None
    high = (s + d) // 2
    low = (s - d) // 2
    if low < 0:
        return None
    return (high, low)

def nine_degree(n_str: str):
    current = n_str
    degree = 0
    while len(current) > 1 or (degree == 0 and len(current) == 1):
        s = sum(int(c) for c in current)
        current = str(s)
        degree += 1
        if len(current) == 1:
            break
    if current == "9":
        return True, degree
    return False, -1

def position(x, y):
    if x >= y:
        return x * x + x + y
    else:
        return y * y + x

def steps(x1, y1, x2, y2):
    return abs(position(x2, y2) - position(x1, y1))

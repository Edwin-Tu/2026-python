import sys

def digit_sum(s):
    return sum(int(ch) for ch in s)

def nine_degree(s):
    total = digit_sum(s)
    if total % 9 != 0:
        return 0
    degree = 1
    while total != 9:
        total = digit_sum(str(total))
        degree += 1
    return degree

def solve():
    out = []
    for s in sys.stdin.read().strip().split():
        if s == "0":
            break
        degree = nine_degree(s)
        if degree == 0:
            out.append(f"{s} is not a multiple of 9.")
        else:
            out.append(f"{s} is a multiple of 9 and has 9-degree {degree}.")
    print("\n".join(out))

if __name__ == "__main__":
    solve()

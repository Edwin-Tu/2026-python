import sys

def is_multiple_of_11(s):
    odd_sum = 0
    even_sum = 0
    for i, ch in enumerate(s):
        if i % 2 == 0:
            odd_sum += int(ch)
        else:
            even_sum += int(ch)
    return abs(odd_sum - even_sum) % 11 == 0

def solve():
    out = []
    for s in sys.stdin.read().strip().split():
        if s == "0":
            break
        if is_multiple_of_11(s):
            out.append(f"{s} is a multiple of 11.")
        else:
            out.append(f"{s} is not a multiple of 11.")
    print("\n".join(out))

if __name__ == "__main__":
    solve()

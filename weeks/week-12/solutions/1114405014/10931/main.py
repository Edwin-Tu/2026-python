import sys

def solve():
    out = []
    for token in sys.stdin.read().strip().split():
        n = int(token)
        if n == 0:
            break
        b = bin(n)[2:]
        p = b.count("1")
        out.append(f"The parity of {b} is {p} (mod 2).")
    print("\n".join(out))

if __name__ == "__main__":
    solve()

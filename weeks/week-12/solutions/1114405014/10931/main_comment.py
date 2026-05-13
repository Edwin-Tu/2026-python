import sys

def solve():
    out = []

    for token in sys.stdin.read().strip().split():
        n = int(token)
        if n == 0:
            break

        # bin(n) 會得到類似 0b1010 的字串，所以用 [2:] 去掉 0b
        b = bin(n)[2:]

        # parity 就是二進位中 1 的數量
        p = b.count("1")

        out.append(f"The parity of {b} is {p} (mod 2).")

    print("\n".join(out))

if __name__ == "__main__":
    solve()

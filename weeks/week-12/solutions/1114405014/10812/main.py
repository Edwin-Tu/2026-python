import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    ans = []
    idx = 1
    for _ in range(t):
        s = int(data[idx])
        d = int(data[idx + 1])
        idx += 2
        if s < d or (s + d) % 2 != 0:
            ans.append("impossible")
        else:
            high = (s + d) // 2
            low = (s - d) // 2
            ans.append(f"{high} {low}")
    print("\n".join(ans))

if __name__ == "__main__":
    solve()

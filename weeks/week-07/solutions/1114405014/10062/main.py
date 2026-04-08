import sys
sys.setrecursionlimit(10000)


def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    arr = [0] * (N + 1)
    for i in range(2, N + 1):
        arr[i] = int(data[i - 1])

    result = [0] * (N + 1)
    available = list(range(1, N + 1))

    for i in range(N, 0, -1):
        result[i] = available[arr[i]]
        available.pop(arr[i])

    for i in range(1, N + 1):
        print(result[i])


if __name__ == "__main__":
    solve()
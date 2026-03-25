def solve():
    n, q = map(int, input().split())
    states = [0] * n

    for _ in range(q):
        data = list(map(int, input().split()))
        if data[0] == 1:
            i = data[1] - 1
            states[i] = 1 - states[i]
        else:
            l = data[1] - 1
            r = data[2] - 1
            print(sum(states[l:r+1]) % 2)


if __name__ == "__main__":
    solve()
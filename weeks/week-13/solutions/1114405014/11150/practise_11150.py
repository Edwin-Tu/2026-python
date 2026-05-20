import sys


def min_stones(L, S, T, stones):
    raise NotImplementedError("Implement this function")


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    while idx < len(data):
        L = int(data[idx]); idx += 1
        if idx >= len(data):
            break
        S = int(data[idx]); T = int(data[idx + 1]); M = int(data[idx + 2])
        idx += 3
        stones = []
        for _ in range(M):
            stones.append(int(data[idx])); idx += 1
        print(min_stones(L, S, T, stones))


if __name__ == "__main__":
    main()

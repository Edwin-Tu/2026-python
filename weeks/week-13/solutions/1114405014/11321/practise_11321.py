import sys


def can_place_trap(N, M, traps):
    raise NotImplementedError("Implement this function")


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    while idx < len(data):
        N = int(data[idx]); M = int(data[idx + 1]); T = int(data[idx + 2])
        idx += 3
        traps = []
        for _ in range(T):
            x = int(data[idx]); y = int(data[idx + 1])
            idx += 2
            traps.append((x, y))
        results = can_place_trap(N, M, traps)
        for r in results:
            print(r)


if __name__ == "__main__":
    main()

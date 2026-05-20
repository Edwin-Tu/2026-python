import sys


def visible_mirrors(mirrors):
    raise NotImplementedError("Implement this function")


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    while idx < len(data):
        n = int(data[idx]); idx += 1
        mirrors = []
        for _ in range(n):
            sx = int(data[idx]); sy = int(data[idx + 1])
            ex = int(data[idx + 2]); ey = int(data[idx + 3])
            idx += 4
            mirrors.append((sx, sy, ex, ey))
        result = visible_mirrors(mirrors)
        print(" ".join(str(v) for v in result))


if __name__ == "__main__":
    main()

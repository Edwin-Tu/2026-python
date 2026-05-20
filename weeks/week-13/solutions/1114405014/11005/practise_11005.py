import sys

cost_table = []


def cheapest_base(costs, n):
    raise NotImplementedError("Implement this function")


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    for case_no in range(1, t + 1):
        costs = list(map(int, data[idx:idx + 36]))
        idx += 36
        q = int(data[idx]); idx += 1
        print(f"Case {case_no}:")
        for _ in range(q):
            n = int(data[idx]); idx += 1
            bases = cheapest_base(costs, n)
            print(f"Cheapest base(s) for number {n}:", *bases)
        if case_no < t:
            print()


if __name__ == "__main__":
    main()

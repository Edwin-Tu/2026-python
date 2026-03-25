def calculate_min_distance(addresses):
    addresses.sort()
    vito = addresses[len(addresses) // 2]
    total = 0
    for addr in addresses:
        total += abs(addr - vito)
    return total


def solve():
    t = int(input())
    for _ in range(t):
        data = list(map(int, input().split()))
        r = data[0]
        addresses = data[1:]
        print(calculate_min_distance(addresses))


if __name__ == "__main__":
    solve()
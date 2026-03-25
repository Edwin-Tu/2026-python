def min_total_distance(addresses):
    """
    回傳讓所有親戚到 Vito 家距離總和最小的值
    """
    sorted_addresses = sorted(addresses)
    n = len(sorted_addresses)

    # 中位數位置
    median = sorted_addresses[n // 2]

    total_distance = 0
    for address in sorted_addresses:
        total_distance += abs(address - median)

    return total_distance


def solve(data):
    """
    接收整份輸入字串，回傳整份輸出字串
    """
    tokens = data.split()
    t = int(tokens[0])
    index = 1
    results = []

    for _ in range(t):
        r = int(tokens[index])
        index += 1

        addresses = []
        for _ in range(r):
            addresses.append(int(tokens[index]))
            index += 1

        results.append(str(min_total_distance(addresses)))

    return "\n".join(results) + "\n"


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()), end="")
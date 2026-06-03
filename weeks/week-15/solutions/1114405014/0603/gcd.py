from math import gcd


def sum_of_gcd(n: int) -> int:
    total = 0

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total += gcd(i, j)

    return total


def main():
    while True:
        n = int(input())

        if n == 0:
            break

        print(sum_of_gcd(n))


if __name__ == "__main__":
    main()
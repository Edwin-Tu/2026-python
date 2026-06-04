import math


def count_square_numbers(n: int) -> int:
    if n < 1:
        return 0

    return math.isqrt(n)


def main():
    n = int(input("請輸入一個整數 n："))
    result = count_square_numbers(n)
    print(f"1 到 {n} 之間的平方數有 {result} 個")


if __name__ == "__main__":
    main()
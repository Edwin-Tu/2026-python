def digit_sum(s):
    return sum(int(ch) for ch in s)

while True:
    n = input().strip()

    if n == "0":
        break

    current = n
    degree = 0

    while True:
        total = digit_sum(current)

        if total % 9 != 0:
            print(f"{n} is not a multiple of 9.")
            break

        degree += 1

        if total == 9:
            print(f"{n} has 9-degree {degree}.")
            break

        current = str(total)

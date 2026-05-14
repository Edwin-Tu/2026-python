while True:
    n = input().strip()

    if n == "0":
        break

    odd_sum = 0
    even_sum = 0

    for i, ch in enumerate(n):
        if i % 2 == 0:
            odd_sum += int(ch)
        else:
            even_sum += int(ch)

    if (odd_sum - even_sum) % 11 == 0:
        print(f"{n} is a multiple of 11.")
    else:
        print(f"{n} is not a multiple of 11.")

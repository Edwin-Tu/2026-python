while True:
    n = int(input())

    if n == 0:
        break

    binary = bin(n)[2:]
    parity = binary.count("1")

    print(f"The parity of {binary} is {parity} (mod 2).")

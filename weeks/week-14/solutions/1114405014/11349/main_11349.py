def solve():
    t = int(input().strip())
    for case in range(1, t + 1):
        line = input().strip()
        while line == '':
            line = input().strip()
        n = int(line.split('=')[1].strip())
        M = [list(map(int, input().split())) for _ in range(n)]
        symmetric = True
        for i in range(n):
            for j in range(n):
                if M[i][j] < 0 or M[i][j] != M[n - 1 - i][n - 1 - j]:
                    symmetric = False
                    break
            if not symmetric:
                break
        if symmetric:
            print(f"Test #{case}: Symmetric.")
        else:
            print(f"Test #{case}: Non-symmetric.")


if __name__ == "__main__":
    solve()

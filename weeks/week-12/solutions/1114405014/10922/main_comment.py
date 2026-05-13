import sys

def digit_sum(s):
    # 將字串中的每一個數字轉成整數後加總
    return sum(int(ch) for ch in s)

def nine_degree(s):
    # 先計算原數字的各位數總和
    total = digit_sum(s)

    # 若第一次加總後不是 9 的倍數，原數就不是 9 的倍數
    if total % 9 != 0:
        return 0

    # 只要能被 9 整除，至少需要做一次加總，因此 degree 從 1 開始
    degree = 1

    # 持續把總和再做各位數加總，直到變成 9
    while total != 9:
        total = digit_sum(str(total))
        degree += 1

    return degree

def solve():
    out = []

    # 每行可能是很大的數字，所以用字串處理
    for s in sys.stdin.read().strip().split():
        if s == "0":
            break

        degree = nine_degree(s)
        if degree == 0:
            out.append(f"{s} is not a multiple of 9.")
        else:
            out.append(f"{s} is a multiple of 9 and has 9-degree {degree}.")

    print("\n".join(out))

if __name__ == "__main__":
    solve()

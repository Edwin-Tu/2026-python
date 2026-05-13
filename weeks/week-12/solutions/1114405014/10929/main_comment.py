import sys

def is_multiple_of_11(s):
    # odd_sum 記錄第 1、3、5... 位數字總和
    # even_sum 記錄第 2、4、6... 位數字總和
    # 在 Python 中索引從 0 開始，所以 i % 2 == 0 對應第奇數位
    odd_sum = 0
    even_sum = 0

    for i, ch in enumerate(s):
        if i % 2 == 0:
            odd_sum += int(ch)
        else:
            even_sum += int(ch)

    # 若奇數位和偶數位的差是 11 的倍數，原數就是 11 的倍數
    return abs(odd_sum - even_sum) % 11 == 0

def solve():
    out = []

    # 數字最多可能有 1000 位，因此使用字串讀取
    for s in sys.stdin.read().strip().split():
        if s == "0":
            break

        if is_multiple_of_11(s):
            out.append(f"{s} is a multiple of 11.")
        else:
            out.append(f"{s} is not a multiple of 11.")

    print("\n".join(out))

if __name__ == "__main__":
    solve()

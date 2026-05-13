import sys

def solve():
    # 一次讀入所有資料，並用空白切開
    data = sys.stdin.read().strip().split()
    if not data:
        return

    # 第一個數字是測試資料筆數
    t = int(data[0])
    ans = []
    idx = 1

    for _ in range(t):
        # s 是兩隊分數總和，d 是兩隊分數差
        s = int(data[idx])
        d = int(data[idx + 1])
        idx += 2

        # 若差比總和大，或 s+d 不是偶數，就不可能得到整數分數
        if s < d or (s + d) % 2 != 0:
            ans.append("impossible")
        else:
            # 高分 = (總和 + 差) / 2，低分 = (總和 - 差) / 2
            high = (s + d) // 2
            low = (s - d) // 2
            ans.append(f"{high} {low}")

    print("\n".join(ans))

if __name__ == "__main__":
    solve()

# 分析資料
def analyze(nums):
    nums.sort()
    n = len(nums)

    # 找中位數範圍
    left = nums[(n - 1) // 2]
    right = nums[n // 2]

    # 計算有多少數在這個範圍內
    count = 0
    for x in nums:
        if left <= x <= right:
            count += 1

    # 有幾個可能的最佳值
    total = right - left + 1

    return left, count, total


# 主程式
def solve():
    while True:
        try:
            n = int(input())
            nums = list(map(int, input().split()))

            a, b, c = analyze(nums)

            print(a, b, c)
        except:
            break


if __name__ == "__main__":
    solve()
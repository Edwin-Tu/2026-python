def analyze(nums):
    nums.sort()
    n = len(nums)
    left = nums[(n - 1) // 2]
    right = nums[n // 2]
    count = sum(1 for x in nums if left <= x <= right)
    total = right - left + 1
    return left, count, total


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
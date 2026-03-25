"""
UVA 10041 - Vito's Family

題目說明：
給定一群親戚的住址，找一個位置，使得所有親戚到該位置的距離總和最小。

解題核心：
👉 最佳位置 = 排序後的「中位數」
👉 再計算所有人到中位數的距離總和

時間複雜度：
O(n log n)（排序）
"""

def calculate_min_distance(addresses):
    """
    計算最小總距離

    參數：
    addresses (list): 親戚的地址列表

    回傳：
    int: 最小總距離
    """

    # 1️⃣ 排序地址
    addresses.sort()

    # 2️⃣ 找中位數（最佳位置）
    mid = len(addresses) // 2
    vito = addresses[mid]

    # 3️⃣ 計算總距離
    total_distance = 0
    for addr in addresses:
        total_distance += abs(addr - vito)

    return total_distance


def solve():
    """
    主程式：處理輸入輸出
    """

    # 測試案例數量
    t = int(input())

    for _ in range(t):
        data = list(map(int, input().split()))

        # 第一個數字是親戚數量，其餘是地址
        r = data[0]
        addresses = data[1:]

        result = calculate_min_distance(addresses)

        print(result)


if __name__ == "__main__":
    solve()
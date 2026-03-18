from typing import List


def is_jolly(nums: List[int]) -> bool:
    """
    判斷一個整數序列是否為 Jolly Jumper

    規則說明：
    若序列長度為 n，則相鄰元素的差值（取絕對值）必須剛好包含：
        1, 2, 3, ..., n-1（每個都要出現一次）

    例如：
    [1, 4, 2, 3]
    差值為 → 3, 2, 1 → 符合 → Jolly

    參數：
    nums → 整數序列

    回傳：
    True  → 是 Jolly
    False → 不是 Jolly
    """

    n = len(nums)

    # 若只有一個數字，必定是 Jolly
    if n == 1:
        return True

    # 用 set 存放出現過的差值（避免重複）
    differences = set()

    # 計算每一對相鄰元素的差值
    for i in range(1, n):
        diff = abs(nums[i] - nums[i - 1])

        # 若差值不在合法範圍（1 ~ n-1），直接判定失敗
        if diff < 1 or diff >= n:
            return False

        differences.add(diff)

    # 最後檢查是否剛好有 n-1 個不同的差值
    return len(differences) == n - 1


def solve(input_data: str) -> str:
    """
    主程式邏輯：處理輸入並輸出結果

    輸入格式：
    每一行：
        n a1 a2 a3 ... an

    功能：
    - 逐行讀取資料
    - 判斷是否為 Jolly Jumper
    - 輸出對應結果

    回傳：
    多行結果（Jolly / Not jolly）
    """

    results = []  # 儲存所有輸出結果

    for line in input_data.splitlines():
        line = line.strip()

        # 跳過空行
        if not line:
            continue

        # 將整行轉成整數列表
        parts = list(map(int, line.split()))

        n = parts[0]            # 序列長度
        nums = parts[1:1 + n]   # 實際數列

        # 判斷是否為 Jolly
        if is_jolly(nums):
            results.append("Jolly")
        else:
            results.append("Not jolly")

    # 將所有結果用換行連接
    return "\n".join(results)


def main() -> None:
    """
    程式進入點（標準輸入輸出）

    從 stdin 讀取輸入資料，
    並將處理結果輸出。
    """
    import sys
    input_data = sys.stdin.read()
    print(solve(input_data))


if __name__ == "__main__":
    main()
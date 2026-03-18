def diff(a: int, b: int) -> int:
    """
    計算兩個整數的差值（取絕對值）

    參數：
    a, b → 兩個整數

    回傳：
    兩數之間的絕對差（永遠為非負數）
    """
    return abs(a - b)


def solve(input_data: str) -> str:
    """
    主程式邏輯：處理整份輸入並回傳結果

    功能：
    - 每一行包含兩個整數
    - 計算每行兩數的差值
    - 忽略空行或格式錯誤的行
    - 最後將所有結果用換行組合

    參數：
    input_data → 整份輸入（字串形式）

    回傳：
    每行結果組成的字串（以換行分隔）
    """

    # 將輸入依照每行切割
    lines = input_data.splitlines()

    # 用來存放每行計算結果
    results = []

    # 逐行處理輸入
    for line in lines:
        line = line.strip()  # 去除前後空白

        # 如果是空行，跳過
        if not line:
            continue

        # 將該行拆成兩個數字
        parts = line.split()

        # 若不是兩個數字，跳過（避免錯誤輸入）
        if len(parts) != 2:
            continue

        # 將字串轉成整數
        a, b = map(int, parts)

        # 計算差值並加入結果
        results.append(str(diff(a, b)))

    # 用換行符號將結果串接起來
    return "\n".join(results)


def main() -> None:
    """
    程式進入點（標準輸入輸出）

    從 stdin 讀取資料，交給 solve() 處理，
    再將結果輸出。
    """
    import sys
    input_data = sys.stdin.read()
    print(solve(input_data))


if __name__ == "__main__":
    main()
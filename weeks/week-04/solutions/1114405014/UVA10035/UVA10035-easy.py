def count_carries(a: str, b: str) -> int:
    """
    計算兩個整數相加時的「進位次數」

    作法：
    - 模擬直式加法（從右邊開始）
    - 每一位相加時，若 >= 10 則產生進位
    - 記錄總共出現幾次進位

    參數：
    a, b → 兩個整數（以字串形式表示，方便逐位處理）

    回傳：
    進位發生的次數
    """

    # 從個位數開始（字串最後一位）
    i = len(a) - 1
    j = len(b) - 1

    carry = 0   # 當前是否有進位（0 或 1）
    count = 0   # 總進位次數

    # 只要還有位數沒處理，就持續計算
    while i >= 0 or j >= 0:

        # 取出當前位數（若超出長度則補 0）
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        # 計算當前位的總和（包含上一位的進位）
        total = digit_a + digit_b + carry

        # 判斷是否產生進位
        if total >= 10:
            carry = 1
            count += 1  # 記錄一次進位
        else:
            carry = 0

        # 移動到下一位（往左）
        i -= 1
        j -= 1

    return count


def format_result(carries: int) -> str:
    """
    將進位次數轉換成題目要求的輸出格式

    規則：
    0 → "No carry operation."
    1 → "1 carry operation."
    >1 → "X carry operations."
    """

    if carries == 0:
        return "No carry operation."
    elif carries == 1:
        return "1 carry operation."
    else:
        return f"{carries} carry operations."


def solve(input_data: str) -> str:
    """
    主流程：處理輸入並產生輸出

    功能：
    - 每行包含兩個整數
    - 當遇到 "0 0" 時停止
    - 對每行計算進位次數
    - 將結果整理成多行輸出

    參數：
    input_data → 整份輸入（字串）

    回傳：
    每筆結果組成的字串（以換行分隔）
    """

    # 去除前後空白後，依行切割
    lines = input_data.strip().splitlines()

    results = []  # 儲存所有輸出結果

    for line in lines:
        line = line.strip()

        # 跳過空行（避免格式問題）
        if not line:
            continue

        # 拆成兩個數字
        a, b = line.split()

        # 若遇到終止條件，結束處理
        if a == "0" and b == "0":
            break

        # 計算進位次數
        carries = count_carries(a, b)

        # 轉換成指定輸出格式
        results.append(format_result(carries))

    # 將所有結果用換行連接
    return "\n".join(results)


def main() -> None:
    """
    程式進入點（標準輸入輸出）

    從 stdin 讀取資料，
    並將處理結果輸出到畫面
    """
    import sys
    input_data = sys.stdin.read()
    print(solve(input_data))


if __name__ == "__main__":
    main()
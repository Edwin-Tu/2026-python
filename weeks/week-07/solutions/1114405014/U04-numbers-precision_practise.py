# U04. 數字精度的陷阱與選擇（3.1–3.7）
# 銀行家捨入 / NaN 比較陷阱 / float vs Decimal 選擇

import math
import timeit
from decimal import Decimal, ROUND_HALF_UP

# ── 銀行家捨入（3.1）─────────────────────────────────
# 說明：Python 的 round() 函數使用「銀行家捨入」（Banker's Rounding）
# 又稱「偶數捨入」或「四捨六入五取偶」
# 規則：當要捨入的位是 5 時，結果取最近的偶數
# 例如：0.5 → 0（因為 0 是偶數），1.5 → 2（因為 2 是偶數）
# 這與日常生活中「四捨五入」不同，是 IEEE 754 標準規定
print(round(0.5))  # 0（不是 1！）
print(round(2.5))  # 2（不是 3！）
print(round(3.5))  # 4


# 若需傳統四捨五入，用 Decimal + ROUND_HALF_UP
# 說明：Decimal 是 Python 的精確小數類別
# quantize() 方法可指定捨入模式（rounding mode）
# ROUND_HALF_UP：傳統四捨五入（>=0.5 進位，<0.5 捨去）
def trad_round(x: float, n: int = 0) -> Decimal:
    # 使用 str(x) 而非直接用 x，以避免 float 精度問題
    # 例如：0.1 + 0.2 的實際值不是精確的 0.3
    d = Decimal(str(x))
    # 建立格式化用的 Decimal
    # n=0 → Decimal("1") 表示整數
    # n=2 → Decimal("0.00") 表示小數點後兩位
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    # quantize 進行捨入，rounding 指定捨入模式
    return d.quantize(fmt, rounding=ROUND_HALF_UP)


print(trad_round(0.5))  # 1
print(trad_round(2.5))  # 3


# ── NaN 無法用 == 比較（3.7）─────────────────────────
# 說明：NaN（Not a Number）代表「非數值」，如 0/0、sqrt(-1) 的結果
# NaN 的特殊行為：自己不等於自己（根據 IEEE 754 標準）
# 這是因為 NaN 代表「未定義」或「不可比較」的值
c = float("nan")
print(c == c)  # False（自己不等於自己！）
print(c == float("nan"))  # False
print(math.isnan(c))  # True（唯一正確的檢測方式）

# 處理含 NaN 的資料：過濾掉 NaN 值
data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
clean = [x for x in data if not math.isnan(x)]
print(clean)  # [1.0, 3.0, 5.0]


# ── float vs Decimal 選擇（3.2）──────────────────────
# 說明：Python 提供兩種小數類型，各有優缺點
# float：基於 IEEE 754 二進位浮點數，硬體支援，效能高但有精度問題
# Decimal：基於十進位表示，精度高但效能較低

# float：快但有誤差（科學/工程適用）
print(0.1 + 0.2)  # 0.30000000000000004（精度誤差）
print(0.1 + 0.2 == 0.3)  # False（精度問題導致比較失敗）

# Decimal：精確但慢（金融/會計適用）
# 注意：建立 Decimal 時應使用字串而非 float，避免繼承精度問題
print(Decimal("0.1") + Decimal("0.2"))  # 0.3（精確結果）
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True

# 效能比較
t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
print(f"float: {t1:.3f}s  Decimal: {t2:.3f}s（Decimal 約慢 {t2 / t1:.0f} 倍）")
# 結論：float 快數十倍，Decimal 精度高一倍
# TEST_LOG

## 任務名稱

6/4 Starter — 平方數計數

## 測試目標

本次任務使用 TDD（Test-Driven Development）流程完成 `square_counter.py` 的平方數計數功能。

目標函式：

```python
count_square_numbers(n: int) -> int
```

功能說明：

計算 `1` 到 `n` 之間共有多少個平方數。

例如：

```text
n = 10
平方數為 1, 4, 9
結果為 3
```

---

## 測試檔案

本次將需求拆成三個測試檔案：

```text
test_square_counter_basic.py
test_square_counter_edge.py
test_square_counter_range.py
```

### 1. `test_square_counter_basic.py`

測試基本平方數情境，例如：

```text
n = 1  -> 1
n = 4  -> 2
n = 9  -> 3
n = 16 -> 4
```

### 2. `test_square_counter_edge.py`

測試邊界與特殊情境，例如：

```text
n = 0  -> 0
n = -1 -> 0
n = 2  -> 1
n = 3  -> 1
n = 8  -> 2
```

### 3. `test_square_counter_range.py`

測試較大的範圍，確認程式不是只針對小數字硬寫，例如：

```text
n = 10  -> 3
n = 25  -> 5
n = 26  -> 5
n = 100 -> 10
n = 101 -> 10
```

---

## RED 階段：測試失敗

### 執行指令

```bash
pytest
```

### 測試結果

```text
collected 9 items

test_square_counter_basic.py FFFF
test_square_counter_edge.py FFFFF

9 failed in 0.30s
```

### 失敗原因

第一次執行測試時，`count_square_numbers()` 尚未完成實作，因此函式回傳 `None`。

錯誤範例：

```text
assert None == 1
where None = count_square_numbers(1)
```

代表測試期望 `count_square_numbers(1)` 回傳 `1`，但實際得到 `None`。

### RED 階段結論

此階段符合 TDD 的 Red 流程：

```text
先寫測試，執行後確認測試失敗。
```

失敗原因明確，表示接下來需要完成 `square_counter.py` 的主程式邏輯。

---

## GREEN 階段：完成實作並通過測試

### 實作內容

完成 `square_counter.py`：

```python
import math


def count_square_numbers(n: int) -> int:
    if n < 1:
        return 0

    return math.isqrt(n)


def main():
    n = int(input("請輸入一個整數 n："))
    result = count_square_numbers(n)
    print(f"1 到 {n} 之間的平方數有 {result} 個")


if __name__ == "__main__":
    main()
```

### 實作說明

使用 `math.isqrt(n)` 取得 `n` 的整數平方根。

因為 `1` 到 `n` 之間的平方數數量，等於：

```text
floor(sqrt(n))
```

例如：

```text
n = 10
sqrt(10) 約為 3.16
floor(sqrt(10)) = 3
所以 1 到 10 之間共有 3 個平方數：1, 4, 9
```

另外，若 `n < 1`，代表範圍內沒有正平方數，因此回傳 `0`。

---

## 第二次測試結果

### 執行指令

```bash
pytest
```

### 測試結果

```text
collected 14 items

test_square_counter_basic.py ....
test_square_counter_edge.py .....
test_square_counter_range.py .....

14 passed in 0.06s
```

### GREEN 階段結論

完成主程式後，三個測試檔案全部通過。

```text
14 passed
```

代表基本案例、邊界案例與較大範圍案例皆符合預期。

---

## TDD 流程紀錄

### Red

先建立測試檔案並執行 pytest。

結果：

```text
9 failed
```

原因是主程式尚未完成，函式回傳 `None`。

### Green

完成 `count_square_numbers()` 的功能。

結果：

```text
14 passed
```

所有測試成功通過。

### Refactor

目前程式邏輯簡潔，使用 `math.isqrt()` 直接計算整數平方根，暫無額外重構需求。

---

## 最終結論

本次任務已完成平方數計數功能，並依照 TDD 流程完成測試與實作。

最終測試結果：

```text
14 passed in 0.06s
```

完成項目：

* 建立三個測試檔案
* 建立並完成 `square_counter.py`
* 加入輸入與輸出功能
* 第一次測試確認失敗
* 第二次測試確認全部通過
* 完成 TDD 測試紀錄

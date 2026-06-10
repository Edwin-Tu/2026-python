# 數字根 digit_root

## 一、作業說明

本作業實作 `digit_root(n: int) -> int` 函式。

數字根的概念是：反覆將整數的每一位數字相加，直到結果只剩下一位數，最後回傳該一位數。

例如：

```text
199 → 1 + 9 + 9 = 19
19 → 1 + 9 = 10
10 → 1 + 0 = 1
```

因此：

```python
digit_root(199) == 1
```

---

## 二、功能規格

### 函式名稱

```python
def digit_root(n: int) -> int:
    ...
```

### 輸入

- `n`：正整數
- 題目範圍：`1 ≤ n ≤ 2,000,000,000`

### 輸出

- 回傳 `n` 的數字根
- 結果會是一位數整數

### 例外處理

若 `n < 1`，必須丟出：

```python
ValueError("n must be >= 1")
```

錯誤訊息必須完全一致。

---

## 三、檔案結構

```text
.
├── digit_root.py
├── test_digit_root.py
├── TEST_LOG.md
├── AI_LOG.md
├── README.md
└── PR.md
```

| 檔案 | 說明 |
|---|---|
| `digit_root.py` | 主程式，包含 `digit_root(n)` 函式與簡單輸入輸出 |
| `test_digit_root.py` | 單元測試檔，使用 `unittest` 撰寫 |
| `TEST_LOG.md` | 測試紀錄，包含 Red / Green 結果與案例說明 |
| `AI_LOG.md` | AI 協作紀錄，包含提示詞與修改紀錄 |
| `README.md` | 作業說明文件 |
| `PR.md` | Pull Request 說明文件 |

---

## 四、主程式說明

`digit_root.py` 主要邏輯如下：

```python
def digit_root(n: int) -> int:
    if n < 1:
        raise ValueError("n must be >= 1")

    while n >= 10:
        total = 0
        for digit in str(n):
            total += int(digit)
        n = total

    return n
```

程式流程：

1. 先檢查 `n < 1`
2. 若輸入不合法，丟出 `ValueError`
3. 若 `n` 已經是一位數，直接回傳
4. 若 `n` 是多位數，將每一位數字相加
5. 重複步驟 4，直到結果小於 10
6. 回傳最後的一位數結果

---

## 五、輸入與輸出

本作業核心是函式測試，因此測試會直接 import `digit_root`。

同時，`digit_root.py` 也提供簡單的手動輸入輸出：

```python
if __name__ == "__main__":
    n = int(input("請輸入正整數 n："))
    result = digit_root(n)
    print(result)
```

### 執行方式

```bash
python digit_root.py
```

### 範例

輸入：

```text
199
```

輸出：

```text
1
```

---

## 六、測試方式

本作業測試使用 `unittest` 撰寫，也可以用 `pytest` 執行。

### 使用 unittest

```bash
python -m unittest
```

### 使用 pytest

```bash
pytest
```

---

## 七、測試案例

本次共撰寫 5 個測試案例。

| 測試名稱 | 輸入 | 預期結果 | 類型 |
|---|---:|---:|---|
| `test_basic_24_should_return_6` | `24` | `6` | 基本案例 |
| `test_basic_199_should_return_1` | `199` | `1` | 多輪加總案例 |
| `test_edge_single_digit_should_return_itself` | `5` | `5` | 邊界案例 |
| `test_large_number_should_return_digit_root` | `2000000000` | `2` | 極端大數案例 |
| `test_invalid_input_raises` | `0` | `ValueError("n must be >= 1")` | 例外案例 |

測試涵蓋：

- 一般多位數
- 需要多次加總的數字
- 一位數邊界值
- 接近輸入上限的大數
- 非法輸入與錯誤訊息檢查

---

## 八、測試結果

### Red 階段

第一次執行測試時，因主程式尚未完成，測試失敗：

```text
test_digit_root.py FFFFF [100%]

5 failed in 0.20s
```

### Green 階段

完成 `digit_root.py` 後，再次執行測試：

```text
test_digit_root.py ..... [100%]

5 passed in 0.05s
```

代表所有測試皆已通過。

---

## 九、TDD 流程紀錄

本作業依照 TDD 流程完成：

1. 先閱讀題目規格
2. 撰寫 `test_digit_root.py`
3. 執行測試，確認 Red
4. Commit 測試
5. 撰寫 `digit_root.py`
6. 再次執行測試，確認 Green
7. Commit 實作
8. 撰寫 `TEST_LOG.md`
9. 撰寫 `AI_LOG.md`
10. 整理 README 與 PR 說明

---

## 十、完成狀態

- [x] 完成 `digit_root.py`
- [x] 完成 `test_digit_root.py`
- [x] 測試案例 3 個以上
- [x] 包含基本案例
- [x] 包含邊界案例
- [x] 包含極端案例
- [x] 包含例外案例
- [x] 錯誤訊息符合題目要求
- [x] 測試由 Red 轉 Green
- [x] 完成 `TEST_LOG.md`
- [x] 完成 `AI_LOG.md`

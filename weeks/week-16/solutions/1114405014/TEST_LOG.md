# TEST_LOG.md

# 數字根 digit_root 測試紀錄

## 一、測試目標

本次測試的目標是驗證 `digit_root(n)` 函式是否符合題目規格。

`digit_root(n)` 的功能是反覆將整數 `n` 的每一位數字相加，直到結果只剩下一位數，最後回傳該一位數。

例如：

```text
199 → 1 + 9 + 9 = 19
19 → 1 + 9 = 10
10 → 1 + 0 = 1
```

所以：

```python
digit_root(199) == 1
```

此外，題目規定輸入必須為正整數。如果 `n < 1`，必須丟出：

```python
ValueError("n must be >= 1")
```

---

## 二、測試環境

測試指令：

```bash
pytest
```

測試環境紀錄：

```text
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
```

測試檔案：

```text
test_digit_root.py
```

---

## 三、測試案例整理

本次共撰寫 5 個測試案例。

| 測試名稱 | 測試輸入 | 預期結果 | 測試目的 |
|---|---:|---:|---|
| `test_basic_24_should_return_6` | `24` | `6` | 測試一般多位數，且只需加總一次 |
| `test_basic_199_should_return_1` | `199` | `1` | 測試需要多次反覆加總的情況 |
| `test_edge_single_digit_should_return_itself` | `5` | `5` | 測試邊界案例：輸入本身已經是一位數 |
| `test_large_number_should_return_digit_root` | `2000000000` | `2` | 測試極端案例：接近題目輸入上限的大數 |
| `test_invalid_input_raises` | `0` | `ValueError` | 測試例外案例：輸入小於 1 時必須丟出錯誤 |

---

## 四、各測試案例說明

### 1. 基本案例：`digit_root(24)`

```python
self.assertEqual(digit_root(24), 6)
```

測試原因：

`24` 是一般的多位數案例，只需要進行一次各位數相加。

計算過程：

```text
2 + 4 = 6
```

預期結果：

```text
6
```

這個案例用來確認函式能正確處理基本的數字根計算。

---

### 2. 多輪加總案例：`digit_root(199)`

```python
self.assertEqual(digit_root(199), 1)
```

測試原因：

`199` 不是加總一次就會得到一位數，因此可以確認函式是否有「反覆加總直到剩一位數」的能力。

計算過程：

```text
1 + 9 + 9 = 19
1 + 9 = 10
1 + 0 = 1
```

預期結果：

```text
1
```

這個案例可以避免函式只做一次加總就直接回傳。

---

### 3. 邊界案例：`digit_root(5)`

```python
self.assertEqual(digit_root(5), 5)
```

測試原因：

`5` 是一位數，依照題目規格，一位數應該直接回傳自己。

預期結果：

```text
5
```

這是重要的邊界案例，因為它測試函式是否能正確處理已經符合結束條件的輸入。

---

### 4. 極端案例：`digit_root(2000000000)`

```python
self.assertEqual(digit_root(2000000000), 2)
```

測試原因：

題目規定輸入範圍為：

```text
1 ≤ n ≤ 2,000,000,000
```

因此使用 `2000000000` 測試接近輸入上限的大數。

計算過程：

```text
2 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 = 2
```

預期結果：

```text
2
```

這個案例用來確認函式在處理大數時仍然能正確計算。

---

### 5. 例外案例：`digit_root(0)`

```python
with self.assertRaises(ValueError) as context:
    digit_root(0)

self.assertEqual(str(context.exception), "n must be >= 1")
```

測試原因：

題目要求當 `n < 1` 時，必須丟出：

```python
ValueError("n must be >= 1")
```

因此使用 `0` 測試非法輸入。

這個測試不只確認有丟出 `ValueError`，也確認錯誤訊息必須完全等於：

```text
n must be >= 1
```

這可以避免只丟出錯誤，但錯誤訊息不符合題目要求的情況。

---

## 五、紅燈測試紀錄

第一次執行測試時，測試結果為失敗。

執行指令：

```bash
pytest
```

測試結果：

```text
collected 5 items

test_digit_root.py FFFFF [100%]

5 failed in 0.20s
```

失敗原因整理如下：

| 測試案例 | 失敗原因 |
|---|---|
| `test_basic_199_should_return_1` | 回傳 `None`，但預期為 `1` |
| `test_basic_24_should_return_6` | 回傳 `None`，但預期為 `6` |
| `test_edge_single_digit_should_return_itself` | 回傳 `None`，但預期為 `5` |
| `test_large_number_should_return_digit_root` | 回傳 `None`，但預期為 `2` |
| `test_invalid_input_raises` | 沒有丟出 `ValueError` |

紅燈原因判斷：

當時 `digit_root` 尚未完成正確實作，因此一般案例、大數案例與邊界案例都回傳 `None`。此外，非法輸入 `0` 也沒有正確丟出 `ValueError`。

這符合 TDD 流程中的「先寫測試，確認測試失敗」階段。

---

## 六、綠燈測試紀錄

完成 `digit_root.py` 實作後，再次執行測試。

執行指令：

```bash
pytest
```

測試結果：

```text
collected 5 items

test_digit_root.py ..... [100%]

5 passed in 0.05s
```

代表 5 個測試案例全部通過。

---

## 七、測試結果總結

本次測試涵蓋以下情況：

| 類型 | 是否涵蓋 | 對應測試 |
|---|---|---|
| 基本案例 | 有 | `24 → 6` |
| 多輪加總案例 | 有 | `199 → 1` |
| 邊界案例 | 有 | `5 → 5` |
| 極端大數案例 | 有 | `2000000000 → 2` |
| 例外案例 | 有 | `0` 應丟出 `ValueError` |

測試結果從一開始的：

```text
5 failed
```

修正實作後變成：

```text
5 passed
```

因此可以確認 `digit_root(n)` 已符合本次題目需求。

---

## 八、自我檢查

- [x] 至少 3 個測試案例
- [x] 包含基本案例
- [x] 包含邊界案例
- [x] 包含極端案例
- [x] 包含例外案例
- [x] 檢查錯誤訊息是否完全符合題目要求
- [x] 有紅燈紀錄
- [x] 有綠燈紀錄
- [x] 測試最後全部通過

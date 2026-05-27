# Week 14 解題作業 — 學號 1114405014

## 題目清單

| 題號 | 題名 | 解題程式 | 註解版 | 測試程式 |
|------|------|----------|--------|----------|
| 11349 | UVA 11349 — Symmetric Matrix | [main_11349.py](./11349/main_11349.py) | [main_11349_tw.py](./11349/main_11349_tw.py) | [test_11349.py](./11349/test_11349.py) |
| 11417 | UVA 11417 — GCD | [main_11417.py](./11417/main_11417.py) | [main_11417_tw.py](./11417/main_11417_tw.py) | [test_11417.py](./11417/test_11417.py) |
| 11461 | UVA 11461 — Square Numbers | [main_11461.py](./11461/main_11461.py) | [main_11461_tw.py](./11461/main_11461_tw.py) | [test_11461.py](./11461/test_11461.py) |
| 12019 | UVA 12019 — Doom's Day Algorithm | [main_12019.py](./12019/main_12019.py) | [main_12019_tw.py](./12019/main_12019_tw.py) | [test_12019.py](./12019/test_12019.py) |

## 開發方式

採 TDD（Test-Driven Development）進行：
1. 先撰寫測試，包含題目範例與邊界案例
2. 撰寫解題程式直到測試通過
3. 全數 25 個測試通過

## 執行測試

```bash
python3 -m pytest 11349/test_11349.py 11417/test_11417.py 11461/test_11461.py 12019/test_12019.py -v
```

## 測試結果

```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.0.3, pluggy-1.6.0
collected 25 items

11349/test_11349.py::test_sample PASSED                                  [  4%]
11349/test_11349.py::test_symmetric_1x1 PASSED                           [  8%]
11349/test_11349.py::test_non_symmetric_negative PASSED                  [ 12%]
11349/test_11349.py::test_non_symmetric_center PASSED                    [ 16%]
11349/test_11349.py::test_symmetric_2x2 PASSED                           [ 20%]
11349/test_11349.py::test_symmetric_4x4 PASSED                           [ 24%]
11349/test_11349.py::test_multiple_cases PASSED                          [ 28%]
11417/test_11417.py::test_sample PASSED                                  [ 32%]
11417/test_11417.py::test_n_2 PASSED                                     [ 36%]
11417/test_11417.py::test_n_3 PASSED                                     [ 40%]
11417/test_11417.py::test_n_4 PASSED                                     [ 44%]
11417/test_11417.py::test_n_5 PASSED                                     [ 48%]
11417/test_11417.py::test_n_6 PASSED                                     [ 52%]
11461/test_11461.py::test_sample PASSED                                  [ 56%]
11461/test_11461.py::test_single_number_perfect PASSED                   [ 60%]
11461/test_11461.py::test_single_number_not PASSED                       [ 64%]
11461/test_11461.py::test_range_no_squares PASSED                        [ 68%]
11461/test_11461.py::test_range_all_squares PASSED                       [ 72%]
11461/test_11461.py::test_a_equals_b_square PASSED                       [ 76%]
11461/test_11461.py::test_large_range PASSED                             [ 80%]
12019/test_12019.py::test_sample_jan PASSED                              [ 84%]
12019/test_12019.py::test_doomsday PASSED                                [ 88%]
12019/test_12019.py::test_known_dates PASSED                             [ 92%]
12019/test_12019.py::test_march PASSED                                   [ 96%]
12019/test_12019.py::test_february_leap PASSED                           [100%]

============================== 25 passed in 0.32s ==============================
```

## 各題解題思路

### 11349 — Symmetric Matrix
- 檢查所有元素 ≥ 0
- 檢查 M[i][j] == M[n-1-i][n-1-j]（中心對稱，非轉置對稱）
- 時間複雜度 O(n²)

### 11417 — GCD
- 雙層迴圈 sum(gcd(i, j)) for 1 ≤ i < j ≤ N
- 使用 `math.gcd`，N ≤ 500 效能可接受

### 11461 — Square Numbers
- 完全平方數個數 = ⌊√b⌋ - ⌊√(a-1)⌋
- 使用 `math.isqrt` 避免浮點誤差

### 12019 — Doom's Day Algorithm
- 2012 年 Doomsday = Wednesday
- 每月對應參考日期（表格），計算差值後映射星期

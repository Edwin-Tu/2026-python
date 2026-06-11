# TEST_LOG.md

## 專案名稱

0611 Sort Lab：排序效能實驗室

## 測試策略

本專案採用 TDD 流程完成五個階段。每個階段皆遵守：

```text
先寫測試 → 跑紅燈 → test commit → 寫實作 → 跑綠燈 → feat commit
```

測試重點包含：

1. 函式基本功能是否正確。
2. 邊界條件是否處理。
3. 是否符合規格限制。
4. 是否避免不合理輸入造成錯誤結果。
5. 是否保留可重現的 benchmark 結果。

---

## 測試總覽

| Stage | 測試檔案 | 測試數量 | 測試重點 | 狀態 |
|---|---|---:|---|---|
| Stage 1 | `test_timing.py` | 4 | timeit 回傳值、metadata、records、stdout | 通過 |
| Stage 2 | `test_sorts.py` | 5 | 三種排序、重複值、負數、空 list、不修改輸入 | 通過 |
| Stage 3 | `test_benchmark.py` | 5 | make_data、optimized sort、benchmark 結構、JSON 輸出 | 通過 |
| Stage 4 | `test_plot.py` | 6 | 讀 JSON、產 PNG、單資料點、missing file、Agg backend | 通過 |
| Stage 5 | `test_security.py` | 7 | 負數、空資料、非法 elapsed、非數字 size | 通過 |

---

## Stage 1：`test_timing.py`

### 測試目的

驗證 `timeit` 裝飾器符合規格。

### 測試項目

| 測試名稱 | 說明 |
|---|---|
| `test_timeit_preserves_return_value` | 被裝飾函式的回傳值不變 |
| `test_timeit_records_last_elapsed_and_records` | 呼叫後產生 `last_elapsed` 與 `records` |
| `test_timeit_preserves_function_metadata` | 使用 `functools.wraps` 保留函式名稱與 docstring |
| `test_timeit_does_not_print` | 確認裝飾器不輸出 stdout |

### 邊界與副作用

- 使用極短執行時間函式測試 `last_elapsed`。
- 使用 `redirect_stdout` 確認沒有不必要輸出。

### 測試結果

最終通過。

---

## Stage 2：`test_sorts.py`

### 測試目的

驗證 `bubble_sort`、`quick_sort`、`merge_sort` 的正確性與非破壞性。

### 測試項目

| 測試名稱 | 說明 |
|---|---|
| `test_sort_positive_numbers` | 一般正整數排序 |
| `test_sort_with_duplicates` | 含重複值 |
| `test_sort_with_negative_numbers` | 含負數 |
| `test_sort_empty_and_single_item_list` | 邊界：空 list、單一元素 list |
| `test_sort_does_not_modify_input_list` | 確認回傳新 list，不修改原輸入 |

### 紅燈紀錄

初始骨架只放 `pass` 時，排序函式回傳 `None`，因此測試失敗：

```text
AssertionError: None != [1, 2, 3]
AssertionError: None != []
AssertionError: None != [7]
```

### 綠燈紀錄

完成排序實作後通過。

---

## Stage 3：`test_benchmark.py`

### 測試目的

驗證 benchmark 與加速版排序可用。

### 測試項目

| 測試名稱 | 說明 |
|---|---|
| `test_make_data_is_deterministic_with_same_seed` | 相同 seed 產生相同資料 |
| `test_make_data_boundary_zero_size` | 邊界：`make_data(0)` 回傳空 list |
| `test_optimized_quick_sort_correctness` | 加速版排序正確且不修改輸入 |
| `test_run_benchmark_contains_required_algorithms_and_sizes` | benchmark 結果包含五種演算法 |
| `test_save_results_creates_json_file` | 可輸出並讀回 JSON |

### 紅燈紀錄

尚未建立 `benchmark.py` 時發生：

```text
ModuleNotFoundError: No module named 'benchmark'
```

### 綠燈紀錄

完成 `benchmark.py` 與 `optimized_quick_sort` 後通過。

---

## Stage 4：`test_plot.py`

### 測試目的

驗證 `plot.py` 可以正確讀取 benchmark 結果並輸出圖片。

### 測試項目

| 測試名稱 | 說明 |
|---|---|
| `test_load_results_reads_json_file` | 能讀取 `results.json` |
| `test_plot_results_creates_non_empty_png_file` | 能產生非空 PNG |
| `test_plot_results_boundary_single_algorithm_single_size` | 邊界：單演算法、單資料點 |
| `test_main_reads_results_and_creates_output_png` | `main()` 完整執行 |
| `test_load_results_missing_file_raises_file_not_found_error` | 檔案不存在時丟出 `FileNotFoundError` |
| `test_plot_uses_agg_backend` | 確認 matplotlib backend 是 `Agg` |

### 紅燈紀錄

尚未建立 `plot.py` 時發生：

```text
ModuleNotFoundError: No module named 'plot'
```

### 綠燈紀錄

完成 `plot.py` 後通過。

---

## Stage 5：`test_security.py`

### 測試目的

依安全程式設計原則進行輸入驗證與錯誤防護。

### 測試項目

| 測試名稱 | 說明 |
|---|---|
| `test_make_data_rejects_negative_size` | 拒絕負數資料量 |
| `test_run_benchmark_rejects_zero_repeats` | 拒絕 `repeats=0` |
| `test_run_benchmark_rejects_negative_size` | 拒絕負數 size |
| `test_plot_results_rejects_empty_results` | 拒絕空 results |
| `test_plot_results_rejects_results_without_data_points` | 拒絕無資料點 results |
| `test_plot_results_rejects_zero_or_negative_elapsed_time` | 拒絕 0 或負數 elapsed time |
| `test_plot_results_rejects_non_numeric_size_key` | 拒絕非數字 size key |

### 紅燈紀錄

初次安全測試有兩個失敗：

```text
FAILED test_security.py::TestSecurityValidation::test_plot_results_rejects_results_without_data_points
FAILED test_security.py::TestSecurityValidation::test_plot_results_rejects_zero_or_negative_elapsed_time
```

原因：

1. `plot_results` 會忽略空資料，但沒有阻止整張空圖被輸出。
2. `plot_results` 沒有拒絕 `elapsed <= 0`，導致 log scale 資料不安全。

### 修正方式

在 `plot.py` 新增 `_validate_and_collect_series(results)`：

- 確認每個演算法結果是 dict。
- 確認至少有一組有效資料點。
- 確認 size key 可轉成 int。
- 確認 size 不為負數。
- 確認 elapsed time 是數字。
- 確認 elapsed time 大於 0。

### 綠燈紀錄

```text
test_security.py .......
7 passed
```

---

## Benchmark 結果摘要

| Size | bubble_sort | quick_sort | merge_sort | sorted | optimized_quick_sort |
|---:|---:|---:|---:|---:|---:|
| 500 | 0.009279 | 0.001123 | 0.000934 | 0.000042 | 0.000340 |
| 1000 | 0.041029 | 0.000890 | 0.001714 | 0.000096 | 0.000734 |
| 2000 | 0.212945 | 0.003624 | 0.005817 | 0.000244 | 0.003041 |
| 4000 | 0.836264 | 0.005308 | 0.010688 | 0.000515 | 0.004099 |

`optimized_quick_sort` 相對 `quick_sort` 整體加速約 **24.95%**。

---

## 最終測試結論

最終整合測試通過：

```text
27 passed, 28 subtests passed
```

並確認：

```text
python benchmark.py  可執行
python plot.py       可產生 assets/benchmark.png
```

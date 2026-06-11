# 0611 Sort Lab：排序效能實驗室

## 專案簡介

本專案是 Week 16 的排序效能實驗室，目標是用 TDD 流程完成一個可測試、可量測、可視覺化、並經過安全性自掃的排序實驗專案。

專案共分五個階段：

1. Stage 1：`timing.py` — `@timeit` 計時裝飾器
2. Stage 2：`sorts.py` — bubble sort、quick sort、merge sort
3. Stage 3：`benchmark.py` — benchmark、`sorted()` baseline、`optimized_quick_sort`
4. Stage 4：`plot.py` — 讀取 `results.json` 並輸出 `assets/benchmark.png`
5. Stage 5：`test_security.py` — 安全性自掃與輸入驗證

本專案遵守以下 TDD 流程：

```text
Read spec → Dev for red → test commit → Dev for green → feat commit → push
```

---

## 檔案結構

```text
.
├── timing.py
├── test_timing.py
├── sorts.py
├── test_sorts.py
├── benchmark.py
├── test_benchmark.py
├── results.json
├── plot.py
├── test_plot.py
├── assets/
│   └── benchmark.png
├── test_security.py
├── README.md
├── TEST_LOG.md
├── AI_LOG.md
└── PR.md
```

## 執行環境

```text
OS: Windows
Python: 3.14.3
pytest: 9.0.3
```

安裝必要套件：

```bash
pip install pytest matplotlib
```

---

## 如何執行測試

執行全部測試：

```bash
python -m pytest
```

分階段執行：

```bash
python -m pytest test_timing.py
python -m pytest test_sorts.py
python -m pytest test_benchmark.py
python -m pytest test_plot.py
python -m pytest test_security.py
```

---

## 如何執行 benchmark

```bash
python benchmark.py
```

執行後會：

1. 產生排序效能比較表。
2. 輸出 `results.json`。
3. 提供 `plot.py` 作為畫圖輸入。

---

## 如何產生圖表

```bash
python plot.py
```

輸出：

```text
assets/benchmark.png
```

`plot.py` 使用 `matplotlib.use("Agg")`，可以在無 GUI 環境產生圖片。

---

## Stage 1：timeit 裝飾器

`timing.py` 提供：

```python
def timeit(func): ...
```

功能：

- 保留原函式回傳值。
- 使用 `functools.wraps` 保留 `__name__` 與 `__doc__`。
- 使用 `time.perf_counter()` 計算執行時間。
- 在 wrapper 上記錄：
  - `last_elapsed`
  - `records`
- 裝飾器內不輸出 `print`，避免污染 stdout。

---

## Stage 2：排序演算法

`sorts.py` 提供：

```python
def bubble_sort(data: list) -> list: ...
def quick_sort(data: list) -> list: ...
def merge_sort(data: list) -> list: ...
```

共同規格：

- 回傳新的 list。
- 不修改原始輸入。
- 不使用 `sorted()` 或 `list.sort()`。
- 支援：
  - 一般正整數
  - 重複值
  - 負數
  - 空 list
  - 單一元素 list

---

## Stage 3：Benchmark 與加速實驗

`benchmark.py` 提供：

```python
def make_data(n: int, seed: int = 42) -> list: ...
def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict: ...
def save_results(results: dict, output_path: str = "results.json") -> None: ...
```

比較演算法：

- `bubble_sort`
- `quick_sort`
- `merge_sort`
- Python 內建 `sorted()`
- `optimized_quick_sort`

`optimized_quick_sort` 採用三個優化策略：

1. **Median-of-three pivot**：用 low、mid、high 三點中位數作為 pivot，降低退化機率。
2. **Insertion sort threshold**：小區間改用 insertion sort，降低小資料量遞迴成本。
3. **Tail recursion elimination**：優先遞迴處理較小區間，降低遞迴深度。

---

## Benchmark 結果

單位：秒。

| Size | bubble_sort | quick_sort | merge_sort | sorted | optimized_quick_sort |
|---:|---:|---:|---:|---:|---:|
| 500 | 0.009279 | 0.001123 | 0.000934 | 0.000042 | 0.000340 |
| 1000 | 0.041029 | 0.000890 | 0.001714 | 0.000096 | 0.000734 |
| 2000 | 0.212945 | 0.003624 | 0.005817 | 0.000244 | 0.003041 |
| 4000 | 0.836264 | 0.005308 | 0.010688 | 0.000515 | 0.004099 |

---

## 加速效果

以 `quick_sort` 作為比較基準：

| Size | quick_sort | optimized_quick_sort | Improvement |
|---:|---:|---:|---:|
| 500 | 0.001123 | 0.000340 | 69.71% |
| 1000 | 0.000890 | 0.000734 | 17.47% |
| 2000 | 0.003624 | 0.003041 | 16.10% |
| 4000 | 0.005308 | 0.004099 | 22.77% |

整體加速幅度約 **24.95%**。

---

## 結果解讀

從 benchmark 數據可以看出：

1. `bubble_sort` 在資料量增加時明顯變慢，符合 O(n²) 的特性。
2. `quick_sort` 與 `merge_sort` 在大資料量下比 bubble sort 穩定許多。
3. Python 內建 `sorted()` 由於使用高度優化的 Timsort 與底層實作，因此是本次實驗中最快的 baseline。
4. `optimized_quick_sort` 相對原始 `quick_sort` 整體約有 **24.95%** 的改善。

---

## Stage 4：圖表輸出

`plot.py` 功能：

- 讀取 `results.json`
- 畫出各演算法折線圖
- x 軸為資料量
- y 軸為平均耗時秒數
- y 軸使用 log scale
- 輸出 `assets/benchmark.png`

使用 log scale 的原因是：`bubble_sort` 和其他 O(n log n) 演算法差距過大，若使用線性比例，其他線條容易被壓在底部。

---

## Stage 5：安全性自掃

安全性與穩定性修補項目：

| 檢查項目 | 修補方式 |
|---|---|
| `make_data(-1)` | 丟出 `ValueError` |
| `run_benchmark(repeats=0)` | 丟出 `ValueError`，避免除以 0 |
| `run_benchmark(sizes=(-1,))` | 丟出 `ValueError` |
| 空 `results` | `plot_results` 丟出 `ValueError` |
| 所有演算法都沒有資料點 | `plot_results` 丟出 `ValueError` |
| elapsed time 為 0 或負數 | 丟出 `ValueError`，避免 log scale 錯誤 |
| size key 非數字 | 丟出 `ValueError` |

不適用項目：

| 項目 | 理由 |
|---|---|
| 將 `random` 改成 `secrets` | 不適用。此專案的亂數只用於 benchmark 測試資料，不涉及密碼、token、session ID。 |
| 網路安全檢查 | 不適用。此專案沒有網路請求或伺服器功能。 |
| `pickle` 反序列化風險 | 不適用。本專案使用 `json` 讀取 `results.json`，沒有使用 `pickle`。 |

---

## 最終檢查

已確認：

- [x] `timing.py` 命名正確
- [x] `test_timing.py` 測試 `timeit`
- [x] `test_benchmark.py` 命名正確
- [x] `results.json` 已產生
- [x] `plot.py` 可產生 `assets/benchmark.png`
- [x] Stage 5 安全性測試通過
- [x] README、TEST_LOG、AI_LOG、PR.md 已整理

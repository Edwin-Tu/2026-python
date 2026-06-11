# AI_LOG.md

## 專案名稱

0611 Sort Lab：排序效能實驗室

## AI 協作原則

本專案使用 AI 作為開發訪談助教，協助進行規格釐清、測試設計、實作檢查、錯誤修正與文件整理。

本專案遵守 TDD 流程：

```text
先寫測試 → 跑紅燈 → commit test → 寫實作 → 跑綠燈 → commit feat
```

---

## AI 協作紀錄

| 階段 | 我實際輸入的提示詞 | AI 協助內容 | 我採用或修改的內容 |
|---|---|---|---|
| 工作流程 | 說明工作流程 | 說明五階段流程、紅燈/綠燈 commit、PR 規則 | 依照五階段拆分任務 |
| Stage 1-2 測試 | 撰寫timeit、sorts測試，每個測試檔至少3個以上測試 | 提供 `test_timing.py` 與 `test_sorts.py` 測試方向 | 採用至少 3 個測試，加入邊界與不可修改輸入 |
| Stage 1-2 骨架 | 尚未進行實作先給我主程式的函式內容先pass，不至於報找不到檔案的錯 | 提供最小函式骨架 | 保留紅燈狀態，避免 import 錯誤 |
| Stage 1-2 實作 | 進行開發 | 提供 `timeit`、三種排序實作 | 採用 `functools.wraps`、`time.perf_counter()` 與非破壞性排序 |
| Stage 3 流程 | 目前已經完成sorts、timint紅綠TDD流程，下一步? | 說明 push、開 PR、進入 Stage 3 | 依照 Stage 3 建立 benchmark |
| Stage 3 測試 | 撰寫測試檔，至少三個測試並包含邊界 | 提供 benchmark 測試 | 加入 deterministic、`n=0`、optimized sort、JSON 輸出測試 |
| Stage 3 實作 | 進行實作 | 提供 `benchmark.py` 與 `optimized_quick_sort` | 採用 `sorted()` baseline 與演算法優化版 quick sort |
| Stage 4 目標 | 進入第四步畫圖 說明任務目標 | 說明 `plot.py` 任務、log scale、PNG 輸出 | 確認 Stage 4 是視覺化，不重新 benchmark |
| Stage 4 測試 | 撰寫測試 | 提供 `test_plot.py` | 加入 JSON 讀取、PNG 輸出、單資料點、Agg backend |
| Stage 4 實作 | 進入實作 | 提供 `plot.py` | 採用 `matplotlib.use("Agg")` 與 y 軸 log scale |
| Stage 5 目標 | 進入第五步 安全 | 說明安全性自掃任務 | 聚焦輸入驗證與避免無效圖表 |
| Stage 5 測試 | 撰寫測試 | 提供 `test_security.py` | 加入負數、空資料、0 或負 elapsed、非數字 size |
| Stage 5 修正 | 貼上 plot.py 並要求：進行修正 | 補上 `_validate_and_collect_series` | 修正無資料點與 log scale 不合法資料 |
| 檔名修正 | 說明問題3 timeit的問題 | 指出 `test_timing.py` 應測 `timeit`，不是排序 | 修正 `test_timing.py` 與 `timing.py` 命名 |
| 最終檢查 | 進行最終檢查 | 檢查檔名、測試、文件殘留問題 | 修正文件中舊錯字與未勾選項目 |
| 文件重寫 | 重新撰寫README.md、TEST_LOG.md、AI_LOG.md、PR.md | 重新產出四份交付文件 | 文件同步為最終正確狀態 |

---

## 加速實驗紀錄

### 加速多少百分比？

以 `quick_sort` 作為比較基準：

| Size | quick_sort | optimized_quick_sort | Improvement |
|---:|---:|---:|---:|
| 500 | 0.001123 | 0.000340 | 69.71% |
| 1000 | 0.000890 | 0.000734 | 17.47% |
| 2000 | 0.003624 | 0.003041 | 16.10% |
| 4000 | 0.005308 | 0.004099 | 22.77% |

整體加速約 **24.95%**。

### 演算法優化策略為何？

本專案使用演算法優化，不使用 Cython。原因是課堂時間有限，演算法優化較容易在現場快速驗證。

`optimized_quick_sort` 採用：

1. **Median-of-three pivot**
   - 使用 low、mid、high 三個位置的中位數作為 pivot。
   - 減少 pivot 選到極端值造成退化的機率。

2. **Insertion sort threshold**
   - 當子陣列長度小於等於 16 時，改用 insertion sort。
   - 小資料量時 insertion sort 的常數成本較低。

3. **Tail recursion elimination**
   - 優先遞迴處理較小區段，較大區段用 while 迴圈延續。
   - 降低遞迴深度與 call stack 成本。

---

## 安全性自掃紀錄

### 依 Python 安全程式原則，修補幾項程式問題？

本次共涵蓋 **7 項安全與穩定性測試**：

1. `make_data(n)` 拒絕負數。
2. `run_benchmark(repeats)` 拒絕 `repeats < 1`。
3. `run_benchmark(sizes)` 拒絕負數 size。
4. `plot_results` 拒絕空 results。
5. `plot_results` 拒絕所有演算法都沒有資料點。
6. `plot_results` 拒絕 elapsed time 為 0 或負數。
7. `plot_results` 拒絕非數字 size key。

其中 Stage 5 實際修補重點為：

- 無資料點不應輸出空圖。
- 0 或負數 elapsed time 不應進入 log scale。
- 非數字 size key 應主動丟出 `ValueError`。

### 不適用項目

| 項目 | 判定理由 |
|---|---|
| `random` 改成 `secrets` | 不適用。benchmark 測試資料不是安全敏感隨機數。 |
| `pickle` 安全風險 | 不適用。本專案使用 `json` 讀寫結果，不使用 `pickle`。 |
| 網路輸入驗證 | 不適用。本專案無 API、socket 或網路服務。 |

---

## AI 協作反思

AI 在本專案中幫助我快速拆分測試與實作，但仍需要由我負責驗收：

1. 測試是否真的符合題目規格。
2. 是否有遵守紅燈到綠燈的 TDD 流程。
3. 檔名與 import 是否一致。
4. benchmark 數據是否有寫進報告。
5. 安全性自掃是否有說明不適用項目。

最終修正包含：

- [x] `timint.py` 已修正為 `timing.py`
- [x] `test_banchmark.py` 已修正為 `test_benchmark.py`
- [x] `test_timing.py` 已確認為真正的 `timeit` 測試
- [x] README、TEST_LOG、AI_LOG、PR.md 已同步最新狀態

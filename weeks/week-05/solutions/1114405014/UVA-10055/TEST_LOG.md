# TEST_LOG.md

## 🧪 測試紀錄 - UVA 10055 (Function Monotonicity)

------------------------------------------------------------------------

### 🔴 Red 階段

執行測試：

    python -m unittest -v

測試結果：

    NotImplementedError

說明：

-   測試檔成功載入
-   `flip_function`、`query_monotonicity`、`solve` 尚未實作
-   屬於功能缺失錯誤（非語法錯）

✅ 成功進入 Red 階段

------------------------------------------------------------------------

### 🟢 Green 階段

補上最小可通過實作後再次執行：

    python -m unittest -v

測試結果：

    test_even_number_of_decreasing_functions_is_increasing ... ok
    test_flip_single_function_becomes_decreasing ... ok
    test_flip_twice_returns_to_original_state ... ok
    test_initial_single_function_is_increasing ... ok
    test_odd_number_of_decreasing_functions_is_decreasing ... ok
    test_subrange_query ... ok
    test_flip_then_query ... ok
    test_multiple_flips_and_queries ... ok
    test_single_query_without_flip ... ok

    ----------------------------------------------------------------------
    Ran 9 tests in 0.005s

    OK

說明：

-   所有測試皆通過
-   覆蓋情境包含：
    -   單一函數
    -   多函數奇偶判斷
    -   flip 操作正確性
    -   區間查詢
    -   多次操作組合

✅ Green 完成

------------------------------------------------------------------------

### 🔵 Refactor 階段

優化內容：

-   使用 `^= 1`（XOR）實現狀態翻轉
-   使用 `sum() % 2` 判斷奇偶
-   清楚拆分功能：
    -   `flip_function`
    -   `query_monotonicity`
    -   `solve`

------------------------------------------------------------------------

## 🧠 核心驗證點

-   遞減函數數量奇偶決定結果
-   flip 操作正確影響狀態
-   區間查詢包含邊界
-   多次操作結果一致

------------------------------------------------------------------------

## 🏁 總結

本題 TDD 流程：

-   ✔ Red：測試先行，驗證功能缺失
-   ✔ Green：完成最小可通過實作
-   ✔ Refactor：優化程式結構與可讀性

👉 最終 9/9 測試通過，開發完成

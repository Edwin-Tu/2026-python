# TEST_LOG.md

## 🧪 測試紀錄 - UVA 10050 (Hartals)

------------------------------------------------------------------------

### 🔴 Red 階段

執行測試：

    python -m unittest -v

結果：

    ImportError: cannot import name 'count_hartals'

說明： - 測試檔已建立 - 主程式尚未實作函式 - 成功進入 Red 階段

------------------------------------------------------------------------

### 🟢 Green 階段

實作 `count_hartals()` 與 `solve()` 後再次執行：

    python -m unittest -v

測試結果：

    test_multiple_parties (test_10050.TestHartals.test_multiple_parties) ... ok
    test_no_party (test_10050.TestHartals.test_no_party) ... ok
    test_overlap_days (test_10050.TestHartals.test_overlap_days) ... ok
    test_single_party (test_10050.TestHartals.test_single_party) ... ok
    test_skip_weekends (test_10050.TestHartals.test_skip_weekends) ... ok
    test_multiple_cases (test_10050.TestSolve.test_multiple_cases) ... ok
    test_single_case (test_10050.TestSolve.test_single_case) ... ok

    ----------------------------------------------------------------------
    Ran 7 tests in 0.003s

    OK

說明： - 所有測試皆通過 - 功能正確

------------------------------------------------------------------------

### 🔵 Refactor 階段

進行優化：

-   抽出 `is_weekend()` 函式
-   使用 `set()` 避免重複
-   使用 `range()` 簡化迴圈

------------------------------------------------------------------------

## 🏁 總結

本次開發流程：

-   ✔ Red：撰寫測試並確認失敗
-   ✔ Green：實作最小可通過版本
-   ✔ Refactor：提升程式可讀性與結構

👉 測試全部通過，開發完成

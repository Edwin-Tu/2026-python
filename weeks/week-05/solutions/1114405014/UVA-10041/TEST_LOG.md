# TEST_LOG.md

## 🧪 測試紀錄 - UVA 10041 (Vito's Family)

------------------------------------------------------------------------

### 🔴 Red 階段

執行測試指令：

    python -m unittest -v

測試結果：

    ImportError: cannot import name 'solve' from 'UVA_10041'

說明：

-   測試檔已建立並被 unittest 正確載入
-   但主程式尚未實作 `solve` 與 `min_total_distance`
-   屬於「尚未實作功能」的失敗

✅ 成功進入 Red 階段（測試先行）

------------------------------------------------------------------------

### 🟢 Green 階段

補上最小可通過實作後再次執行：

    python -m unittest -v

測試結果：

    test_duplicate_addresses ... ok
    test_duplicate_and_distinct_addresses ... ok
    test_even_count_addresses ... ok
    test_odd_count_addresses ... ok
    test_single_relative ... ok
    test_two_relatives ... ok
    test_unsorted_input ... ok
    test_case_with_duplicate_addresses ... ok
    test_multiple_cases ... ok
    test_single_case ... ok

    ----------------------------------------------------------------------
    Ran 10 tests in 0.001s

    OK

說明：

-   所有測試通過
-   包含：
    -   單一/多個親戚
    -   奇數/偶數數量
    -   重複門牌
    -   未排序輸入
    -   多筆測資解析

✅ Green 完成

------------------------------------------------------------------------

### 🔵 Refactor 階段

進行程式優化：

-   使用 `sorted()` + 中位數簡化邏輯
-   使用 `sum()` 計算距離總和
-   使用 `map()` / slicing 優化輸入解析
-   增加函式分工（`solve` / `min_total_distance`）

------------------------------------------------------------------------

## 🧠 核心驗證點

測試覆蓋的關鍵行為：

-   中位數確實最小化距離總和
-   重複值不影響正確性
-   偶數情況取中位數仍正確
-   輸入解析符合題目格式

------------------------------------------------------------------------

## 🏁 總結

本題完整 TDD 流程：

-   ✔ Red：測試先行，確認功能缺失
-   ✔ Green：實作最小可通過版本
-   ✔ Refactor：提升程式可讀性與結構

👉 最終 10/10 測試通過，功能正確完成

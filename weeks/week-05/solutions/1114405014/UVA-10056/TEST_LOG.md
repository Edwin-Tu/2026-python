# TEST_LOG.md

## 🧪 測試紀錄 - UVA 10056 (What is the Probability?)

------------------------------------------------------------------------

### 🔴 Red 階段

執行測試：

    python -m unittest -v

測試結果：

    NotImplementedError

說明：

-   測試檔已建立並成功被 unittest 載入
-   `win_probability()` 與 `solve()` 尚未實作
-   測試失敗原因為功能缺失（非語法錯誤）

✅ 成功進入 Red 階段

------------------------------------------------------------------------

### 🟢 Green 階段

實作完成後再次執行測試：

    python -m unittest -v

測試結果：

    test_multiple_cases (test_10056.TestSolve.test_multiple_cases) ... ok
    test_single_case (test_10056.TestSolve.test_single_case) ... ok
    test_example_style_case (test_10056.TestWinProbability.test_example_style_case) ... ok
    test_single_player (test_10056.TestWinProbability.test_single_player) ... ok
    test_two_players_first_player (test_10056.TestWinProbability.test_two_players_first_player) ... ok
    test_two_players_second_player (test_10056.TestWinProbability.test_two_players_second_player) ... ok
    test_zero_probability (test_10056.TestWinProbability.test_zero_probability) ... ok

    ----------------------------------------------------------------------
    Ran 7 tests in 0.004s

    OK

說明：

-   所有測試皆通過
-   測試涵蓋：
    -   單一玩家情況
    -   多玩家機率分布
    -   p = 0 特殊情況
    -   等比級數計算正確性
    -   多筆測資解析

✅ Green 完成

------------------------------------------------------------------------

### 🔵 Refactor 階段

進行程式優化：

-   使用等比級數公式取代模擬
-   加入 `p == 0` 特判避免除以 0
-   使用 f-string 控制輸出格式（四位小數）
-   清楚拆分：
    -   `win_probability`
    -   `solve`

------------------------------------------------------------------------

## 🧠 核心驗證點

-   第 i 位玩家成功機率公式正確
-   無限輪迴機率正確轉換為等比級數
-   輸出格式符合題目要求
-   邊界條件（p=0）處理正確

------------------------------------------------------------------------

## 🏁 總結

本題完整 TDD 流程：

-   ✔ Red：測試先行，驗證功能缺失
-   ✔ Green：完成最小可通過實作
-   ✔ Refactor：優化程式結構與數學模型

👉 最終 7/7 測試通過，開發完成

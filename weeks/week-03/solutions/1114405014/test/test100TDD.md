測試檔案內容概述
TDD 策略說明
在測試檔案中，我保留了 TDD 的三個階段：

紅燈階段：先寫測試，讓測試失敗
綠燈階段：實現功能，讓測試通過
重構階段：優化代碼，保持測試通過
測試案例設計
我設計了多個測試案例來覆蓋不同的情況：

基本 cycle-length 測試：

test_cycle_length_of_1：測試 n=1 的情況
test_cycle_length_of_2：測試 n=2 的情況
test_cycle_length_of_3：測試 n=3 的情況（長度 8）
test_cycle_length_of_22：根據題目範例測試 n=22（長度 16）
test_cycle_length_of_9：測試 n=9（已知最長的早期數字）
區間最大值測試：

test_max_cycle_length_single_number：單個數字的區間
test_max_cycle_length_range_1_to_10：1-10 區間（最大值 20）
test_max_cycle_length_range_100_to_200：較大範圍測試
邊界情況測試：

test_max_cycle_length_i_greater_than_j：處理 i > j 的情況
test_process_input_output：測試輸出格式
實現函數
測試檔案中包含了兩個核心函數：

cycle_length(n)：計算單個數字的 cycle-length
max_cycle_length(i, j)：計算區間內的最大 cycle-length
測試執行結果
運行測試後，所有測試都通過了（9 個測試案例全部成功），證明實現正確。
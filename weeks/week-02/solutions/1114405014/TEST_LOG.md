# 測試執行紀錄（TEST_LOG）

本文件記錄本次作業在開發與測試過程中的測試執行紀錄，包括測試失敗（Red）與測試成功（Green）的過程。

---

# Run 1 - Red（測試失敗）

## 執行指令

```bash
python tests\test_task1.py
```

## 結果

測試未成功執行。

### 錯誤訊息

```text
ModuleNotFoundError: No module named 'task1_sequence_clean'
```

## 問題原因

- 測試檔案是從 `tests` 資料夾中直接執行。
- Python 在此情況下無法正確解析專案根目錄的模組路徑。
- 因此無法找到 `task1_sequence_clean.py` 模組。

## 修正方式

- 改為在**專案根目錄**執行測試。
- 使用 `unittest` 的 **discovery 模式**來執行所有測試。

---

# Run 2 - Red（測試失敗）

## 執行指令

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 結果

測試仍未成功開始執行。

### 錯誤訊息

```text
ImportError: Start directory is not importable: 'tests'
```

## 問題原因

- 指令是在錯誤的目錄下執行：

```
C:\Edwin\2026-python
```

- 實際作業專案根目錄應為：

```
C:\Edwin\2026-python\weeks\week-02\solutions\1114405014
```

- 因此 `tests` 資料夾無法被 Python 正確識別為測試起始目錄。

## 修正方式

- 切換至正確的專案根目錄後再執行測試。

---

# Run 3 - Green（測試成功）

## 執行指令

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 測試結果

```text
test_all_duplicates (test_task1.TestTask1SequenceClean.test_all_duplicates) ... ok
test_all_odds (test_task1.TestTask1SequenceClean.test_all_odds) ... ok
test_empty_input (test_task1.TestTask1SequenceClean.test_empty_input) ... ok
test_negative_numbers_and_zero (test_task1.TestTask1SequenceClean.test_negative_numbers_and_zero) ... ok
test_normal_case (test_task1.TestTask1SequenceClean.test_normal_case) ... ok
test_k_smaller_than_n (test_task2.TestTask2StudentRanking.test_k_smaller_than_n) ... ok
test_k_zero (test_task2.TestTask2StudentRanking.test_k_zero) ... ok
test_sample_case (test_task2.TestTask2StudentRanking.test_sample_case) ... ok
test_single_student (test_task2.TestTask2StudentRanking.test_single_student) ... ok
test_tie_break_by_age_then_name (test_task2.TestTask2StudentRanking.test_tie_break_by_age_then_name) ... ok
test_action_tie_sorted_by_action_name (test_task3.TestTask3LogSummary.test_action_tie_sorted_by_action_name) ... ok
test_empty_logs (test_task3.TestTask3LogSummary.test_empty_logs) ... ok
test_sample_case (test_task3.TestTask3LogSummary.test_sample_case) ... ok
test_single_user_multiple_actions (test_task3.TestTask3LogSummary.test_single_user_multiple_actions) ... ok
test_user_count_tie_sorted_by_name (test_task3.TestTask3LogSummary.test_user_count_tie_sorted_by_name) ... ok

----------------------------------------------------------------------
Ran 15 tests in 0.002s

OK
```

---

# 測試總結

| 項目 | 結果 |
|-----|-----|
| 測試總數 | 15 |
| 通過測試 | 15 |
| 失敗測試 | 0 |

---

# 已驗證程式

以下三個主程式已通過所有測試：

- `task1_sequence_clean.py`
- `task2_student_ranking.py`
- `task3_log_summary.py`

---

# 驗證內容說明

## Task 1 — Sequence Clean

驗證內容包含：

- 移除重複元素並保留第一次出現順序
- 數列升冪排序
- 數列降冪排序
- 偶數序列擷取

---

## Task 2 — Student Ranking

驗證內容包含：

- 依 **分數（score）降序排序**
- 若分數相同，依 **年齡（age）升序排序**
- 若分數與年齡皆相同，依 **姓名（name）字典序排序**
- 正確輸出前 `k` 名學生

---

## Task 3 — Log Summary

驗證內容包含：

- 計算每位使用者的事件總數
- 若事件數相同，依 **使用者名稱字典序排序**
- 計算全域最常見的 `action`
- 若 `action` 次數相同，依 **action 名稱字典序排序**

---

# 測試過程反思

在測試過程中，主要遇到的問題並非演算法邏輯錯誤，而是：

- Python 模組匯入路徑問題
- 測試執行目錄不正確
- unittest discovery 的使用方式

透過修正執行目錄並使用 `unittest discover` 進行測試後，三個程式皆成功通過所有測試案例。

此過程也說明在 **TDD（Test-Driven Development）流程中，測試環境的正確設定同樣是重要的一環**。
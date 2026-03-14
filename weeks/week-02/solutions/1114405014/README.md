# Week 02 作業說明（README）

學生 ID：1114405014  

本作業依據 Week 02 課程內容實作排序與序列處理，並使用 **Test-Oriented Development（TDD）** 的方式進行開發與驗證。

---

# 完成題目清單

本次作業完成以下三個題目：

1. **Task 1 – Sequence Clean**
   - 整數序列去重（保留首次出現順序）
   - 升冪排序
   - 降冪排序
   - 偶數序列擷取

2. **Task 2 – Student Ranking**
   - 依 score 降序排序
   - score 相同時 age 升序排序
   - score 與 age 相同時 name 字母序排序
   - 輸出前 k 名學生

3. **Task 3 – Log Summary**
   - 統計每位使用者事件總數
   - 依事件數排序使用者
   - 找出全域最常見 action
   - 處理空輸入情況

---

# 執行方式

## Python 版本

本作業使用：

```
Python 3.14
```

---

# 程式執行指令

進入作業資料夾：

```bash
cd weeks/week-02/solutions/1114405014
```

執行各題程式：

### Task 1

```bash
python task1_sequence_clean.py
```

### Task 2

```bash
python task2_student_ranking.py
```

### Task 3

```bash
python task3_log_summary.py
```

---

# 測試執行指令

本作業使用 Python 內建 `unittest` 進行測試。

執行全部測試：

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

測試總數：

```
15 tests
```

所有測試均成功通過。

---

# 資料結構選擇理由

## Task 1 – Sequence Clean

使用 `list` 作為主要資料結構。

原因：

- `list` 可以保持元素的原始順序
- 可以透過迴圈檢查是否出現過來實現去重
- `sorted()` 可以直接對 list 進行排序

---

## Task 2 – Student Ranking

學生資料使用 **tuple + list** 儲存。

格式：

```
(name, score, age)
```

排序使用：

```
sorted(students, key=lambda s: (-score, age, name))
```

原因：

- `tuple` 可以清楚表示學生資料結構
- `sorted()` 搭配 `key` 可以簡潔實作多條件排序
- 避免手寫交換排序，提高可讀性

---

## Task 3 – Log Summary

使用：

- `defaultdict`
- `Counter`

原因：

- `defaultdict` 可以方便統計使用者事件次數
- `Counter` 可以快速計算 action 出現頻率
- 適合做計數型問題

---

# 遇到的錯誤與修正

在測試過程中遇到的主要問題為 **Python 模組匯入錯誤**。

錯誤訊息：

```
ModuleNotFoundError: No module named 'task1_sequence_clean'
```

原因：

- 測試檔案是直接從 `tests` 資料夾執行
- Python 無法正確找到專案根目錄的模組

修正方式：

- 改為在專案根目錄執行測試
- 使用 `unittest discover` 指令執行測試

```
python -m unittest discover -s tests -p "test_*.py" -v
```

---

# TDD 開發過程摘要

本作業採用 **Red → Green → Refactor** 的開發流程。

---

# Task 1 – Sequence Clean

### Red

先撰寫測試案例（正常輸入、空輸入、重複值等）。

執行測試時：

- 程式尚未實作
- 測試失敗

### Green

撰寫最小可行程式：

- 解析輸入
- 去重並保留順序
- 升冪排序
- 降冪排序
- 偶數篩選

測試全部通過。

### Refactor

重構程式：

- 拆分函式
- 改善命名
- 將輸出格式化邏輯抽離

---

# Task 2 – Student Ranking

### Red

先撰寫測試：

- 一般排序
- 同分不同年齡
- 同分同年齡不同名稱
- k = 0

測試初期未通過。

### Green

實作排序邏輯：

```
sorted(students, key=lambda s: (-score, age, name))
```

測試全部通過。

### Refactor

重構程式：

- 將解析輸入與排序邏輯拆分為函式
- 提高程式可讀性

---

# Task 3 – Log Summary

### Red

先設計測試：

- 一般事件統計
- 使用者事件數相同
- action 次數相同
- 空輸入

測試失敗。

### Green

使用：

- `defaultdict`
- `Counter`

完成統計與排序邏輯。

測試全部通過。

### Refactor

重構程式：

- 將統計函式與排序函式拆開
- 改善輸出格式

---

# 總結

本作業透過 TDD 開發流程完成三個題目：

- Sequence Clean
- Student Ranking
- Log Summary

所有測試案例皆成功通過，共 **15 個測試**。

透過測試導向開發，可以在撰寫程式前先確認需求與邏輯，並在重構後仍確保程式正確性。
# AI_USAGE

本文件記錄本次作業中使用 AI 工具協助學習與開發的過程，以及實際採用與修正的經驗。

---

# 1. 我向 AI 詢問的問題

在完成作業過程中，我主要向 AI 詢問以下類型的問題：

1. Python `unittest` 測試框架如何撰寫測試案例
2. Python `sorted()` 搭配 `key` 參數的排序方式
3. 如何使用 `Counter` 或 `defaultdict` 進行統計
4. Python 模組匯入錯誤 (`ModuleNotFoundError`) 的原因與修正
5. Markdown 文件（README、TEST_LOG）的撰寫方式

透過 AI 的回答，我能更快理解測試流程與資料處理方式。

---

# 2. 我採用的 AI 建議

以下是我在作業中採用的 AI 建議：

### 1. 使用 `sorted(..., key=...)` 實作多條件排序

在 Task 2 中使用：

```
sorted(students, key=lambda s: (-score, age, name))
```

可以簡潔實作三個排序條件。

---

### 2. 使用 `Counter` 統計 action

在 Task 3 中使用：

```
Counter()
```

快速統計每個 action 的出現次數。

---

### 3. 使用 `unittest discover` 執行測試

使用以下指令執行所有測試：

```
python -m unittest discover -s tests -p "test_*.py" -v
```

這可以一次執行全部測試檔案。

---

### 4. 將程式拆分為多個函式

AI 建議將程式邏輯拆分為：

- 輸入解析
- 排序處理
- 統計處理
- 輸出格式化

這樣可以提高程式可讀性與可測試性。

---

# 3. 我拒絕或修改的 AI 建議

有些 AI 建議我沒有直接採用，例如：

### 使用 `set` 進行去重

AI 曾建議使用：

```
list(set(numbers))
```

但題目明確限制：

> 不可使用 set 直接輸出去重結果

因為 `set` 會破壞原始順序。

因此我改用：

```
if num not in seen
```

來保留元素的首次出現順序。

---

# 4. AI 可能誤導的案例

在測試執行過程中曾遇到錯誤：

```
ModuleNotFoundError: No module named 'task1_sequence_clean'
```

一開始我使用：

```
python tests\test_task1.py
```

直接執行測試檔案。

這導致 Python 無法正確解析專案根目錄的模組路徑。

透過檢查後發現，正確做法應該是在專案根目錄執行：

```
python -m unittest discover -s tests -p "test_*.py" -v
```

這個案例說明：

AI 可以提供方向，但仍需要自己理解 Python 的執行環境與模組路徑。

---

# 5. 使用 AI 的心得

在本次作業中，AI 主要作為：

- 程式設計概念解釋工具
- Python 語法參考工具
- 測試設計輔助工具

但在實際實作過程中，仍需要：

- 自己理解題目規格
- 自己驗證測試結果
- 自己修正執行環境問題

透過這次作業，我理解到 AI 可以提升開發效率，但最終仍需要自己確認程式邏輯與測試結果是否正確。
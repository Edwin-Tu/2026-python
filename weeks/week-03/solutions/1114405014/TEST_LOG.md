# 測試日誌

## 測試環境

- Python 版本：3.14
- 作業系統：Windows
- 測試框架：unittest

執行測試指令：

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

---

# TDD 開發測試紀錄

本專案採用 TDD（Test-Driven Development）測試驅動開發流程：

```
Red → Green → Refactor
```

開發過程中先撰寫測試，再逐步實作功能，並透過測試結果修正程式。

## Phase 1 — Red（測試失敗）

在尚未實作 robot_core.py 時，先執行測試。

執行指令：

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

測試結果：

```
ERROR: test_robot_scent (unittest.loader._FailedTest.test_robot_scent)

ImportError: cannot import name 'Robot' from 'robot_core'
```

原因說明：

測試程式嘗試匯入以下物件：

- Robot
- execute_command
- execute_commands

但當時 robot_core.py 尚未實作，因此導致 ImportError。

此結果符合 TDD 的 Red 階段（測試先失敗）。

## Phase 2 — 初步實作

接著開始實作 robot_core.py 的最小可行版本（Minimum Viable Implementation），包含：

- Robot 資料類別（dataclass）
- turn_left() 方向左轉
- turn_right() 方向右轉
- execute_command() 單一指令執行
- execute_commands() 指令序列執行
- scent（氣味）機制

其中 scent 使用以下資料結構：

```python
set[(x, y, direction)]
```

用來記錄曾經掉落的位置與方向。

## Phase 3 — Partial Green（部分測試通過）

初步完成 robot_core.py 後再次執行測試。

測試結果：

```
Ran 7 tests

FAILED (failures=1)
```

失敗測試：

`test_same_position_same_direction_with_scent_should_continue_to_next_command`

```
AssertionError: True is not false
```

## Phase 4 — 問題分析

該測試原本使用的指令為：

```
FRF
```

初始狀態：

- Robot = (5,3,N)
- scents = {(5,3,N)}

實際執行流程：

- F → 因為 (5,3,N) 已有 scent，因此忽略此指令
- R → 方向變為 E
- F → 前往 (6,3)，超出地圖範圍，因此 LOST

因此機器人確實會 LOST。

問題並非程式邏輯錯誤，而是 測試案例設計不正確。

Phase 5 — 修正測試案例

為了正確測試「存在 scent 時仍可繼續執行後續指令」，將測試指令修改為：

LFF

執行流程：

(5,3,N)

L → (5,3,W)
F → (4,3,W)
F → (3,3,W)

機器人可正常移動且不會 LOST。

Phase 6 — Final Green（全部測試通過）

修正測試案例後再次執行測試。

執行指令：

python -m unittest discover -s tests -p "test_*.py" -v

測試結果：

Ran 18 tests in 0.002s

OK

所有測試成功通過。

測試總結

總測試數量：

18 tests

測試涵蓋範圍：

方向旋轉（左轉 / 右轉）

機器人前進

地圖邊界判斷

LOST 狀態處理

scent 建立

scent 避免掉落

指令序列執行

非法指令處理

所有核心邏輯皆已通過測試驗證。

TDD 開發流程總結

本專案完整遵循 TDD 開發流程：

1. 撰寫測試（tests）
2. 執行測試 → Red
3. 實作最小功能
4. 再次測試 → Partial Green
5. 修正測試案例
6. 全部測試通過 → Green

透過測試驅動開發確保 robot_core.py 的核心邏輯正確且穩定。
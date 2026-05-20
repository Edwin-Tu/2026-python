# TEST_LOG - 學號 1114405014

## TDD 開發模式

### Phase 1: Red (測試撰寫完成，尚未實作)

| 題號 | 題名 | 測試數量 | 測試狀態 | 說明 |
|------|------|----------|----------|------|
| 11005 | Cheapest Base | 8 | ❌ All Failed | 實作 `cheapest_base(costs, n)` |
| 11063 | RGB to XYZ | 8 | ❌ All Failed | 實作 `rgb_to_xyz(pixels)` |
| 11150 | Frog Crossing Bridge | 12 | ❌ All Failed | 實作 `min_stones(L, S, T, stones)` |
| 11321 | Trap Placement | 11 | ❌ All Failed | 實作 `can_place_trap(N, M, traps)` |
| 11332 | Mirror Visibility | 11 | ❌ All Failed | 實作 `visible_mirrors(mirrors)` |
| **Total** | — | **50** | **❌ 0/50 Passed** | 全部為 NotImplementedError |

---

## 主程式測試 (stdin/stdout)

使用 `test_inputs/input_XX.txt` 作為標準輸入，執行 `main_XX.py` 測試 I/O 流程。

### 11005 — Cheapest Base

**輸入：**
```
2
1 1 ...(36個1)... 1
2
0
15
1 1 ...(36個1)... 1
1
100
```

**執行結果：** ❌ 失敗
```
Case 1:
NotImplementedError: Implement this function
```
- 輸入解析成功：正確輸出 `Case 1:`，到呼叫 `cheapest_base()` 時拋出未實作錯誤。

---

### 11063 — RGB to XYZ

**輸入：**
```
2
255 3 192 0 0 0
255 255 255 255 255 255
0 0 0 0 0 0
10 20 30 100 150 200
```

**執行結果：** ❌ 失敗
```
Case 1:
NotImplementedError: Implement this function
```
- 輸入解析成功：正確輸出 `Case 1:`，解析 4 個像素 (2×2)，到呼叫 `rgb_to_xyz()` 時拋出未實作錯誤。

---

### 11150 — Frog Crossing Bridge

**輸入：**
```
10
1 2 3
3 5 8
20
3 5 2
7 15
```

**執行結果：** ❌ 失敗
```
NotImplementedError: Implement this function
```
- 輸入解析成功：正確讀取 L=10, S=1, T=2, M=3, stones=[3,5,8]，到呼叫 `min_stones()` 時拋出未實作錯誤。

---

### 11321 — Trap Placement

**輸入：**
```
3 3 3
0 0
1 0
2 0
```

**執行結果：** ❌ 失敗
```
NotImplementedError: Implement this function
```
- 輸入解析成功：正確讀取 N=3, M=3, T=3, traps=[(0,0),(1,0),(2,0)]，到呼叫 `can_place_trap()` 時拋出未實作錯誤。

---

### 11332 — Mirror Visibility

**輸入：**
```
2
1 0 1 10
-5 -5 -1 -1
```

**執行結果：** ❌ 失敗
```
NotImplementedError: Implement this function
```
- 輸入解析成功：正確讀取 2 個鏡子線段，到呼叫 `visible_mirrors()` 時拋出未實作錯誤。

---

## 主程式測試總結

| 題號 | Input Parsing | Function Call | 結果 |
|------|:-------------:|:-------------:|:----:|
| 11005 | ✅ 正確 (`Case 1:`) | ❌ NotImplementedError | ❌ |
| 11063 | ✅ 正確 (`Case 1:`) | ❌ NotImplementedError | ❌ |
| 11150 | ✅ 正確 | ❌ NotImplementedError | ❌ |
| 11321 | ✅ 正確 | ❌ NotImplementedError | ❌ |
| 11332 | ✅ 正確 | ❌ NotImplementedError | ❌ |

> 所有主程式的輸入/輸出解析流程驗證通過，目前卡在核心函式未實作（NotImplementedError），符合 TDD Phase 1 Red 預期。

---

## 測試執行命令

```bash
# 執行 pytest（所有單元測試）
cd /mnt/d/Edwin/program/program-python/2026-python/weeks/week-13
python -m pytest solutions/1114405014/ -v

# 執行主程式（stdin I/O 測試）
python solutions/1114405014/11005/main_11005.py < test_inputs/input_11005.txt
python solutions/1114405014/11063/main_11063.py < test_inputs/input_11063.txt
python solutions/1114405014/11150/main_11150.py < test_inputs/input_11150.txt
python solutions/1114405014/11321/main_11321.py < test_inputs/input_11321.txt
python solutions/1114405014/11332/main_11332.py < test_inputs/input_11332.txt
```

---

## 題目函式簽名

| 題號 | 函式簽名 |
|------|----------|
| 11005 | `cheapest_base(costs: list[int], n: int) -> list[int]` |
| 11063 | `rgb_to_xyz(pixels: list[tuple[int,int,int]]) -> tuple[list[tuple[float,float,float]], float]` |
| 11150 | `min_stones(L: int, S: int, T: int, stones: list[int]) -> int` |
| 11321 | `can_place_trap(N: int, M: int, traps: list[tuple[int,int]]) -> list[str]` |
| 11332 | `visible_mirrors(mirrors: list[tuple[int,int,int,int]]) -> list[int]` |

---

### Phase 2: Green (待實作)

> 在 `main_XX.py` 中實作對應函式，使所有測試通過。

### Phase 3: Refactor (待完成)

> 測試通過後，檢視程式碼並優化結構與效能。

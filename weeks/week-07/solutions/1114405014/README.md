# Week 07 Solutions

## Student ID: 1114405014

## Problems Completed

| Problem | Title | Status |
|---------|-------|--------|
| 10062 | Lost Cows | ✅ Complete |
| 10071 | ABCDEF | ✅ Complete |
| 10093 | The Battle of Phony War | ✅ Complete |
| 10101 | Mad Counting / Bangla Numbers | ✅ Complete |
| 10170 | The Hotel with Infinite Rooms | ✅ Complete |

---

## Problem 10062 - Lost Cows

### 解題思路
使用 TreeMap / 模擬由後往前插入：維護可用編號清單，從最後一個位置往前，依序取出對應位置的編號。

### 複雜度
- 時間：O(N log N)
- 空間：O(N)

### 檔案
- `10062/main.py`
- `10062/test_10062.py`

---

## Problem 10071 - ABCDEF

### 解題思路
公式：`a * b * c = d * e * f`

使用 HashMap 統計所有 `a * b * c` 的出現次數，然後枚舉 `d * e * f` 查表累加。

### 複雜度
- 時間：O(N³)
- 空間：O(N³)

### 檔案
- `10071/main.py`
- `10071/test_10071.py`

---

## Problem 10093 - The Battle of Phony War

### 解題思路
將每列可放置炮兵的位置用 bitmask 表示。炮兵攻擊範圍為左右 2 格，同列內需間隔至少 3 格。相鄰兩列不能在同一欄位放置。

使用 DP：
- `dp[i][mask] =` 第 i 列使用 mask 配置時的最大炮兵數
- 轉移時檢查與上一列是否衝突

### 複雜度
- 時間：O(N * 2^M * 2^M)，M ≤ 10
- 空間：O(N * 2^M)

### 檔案
- `10093/main.py`
- `10093/test_10093.py`

---

## Problem 10101 - Mad Counting / Bangla Numbers

### 解題思路
1. 解析等式，計算左右兩邊的值
2. 若已相等，輸出原式
3. 否則枚舉所有數字中的每個數字，嘗試改變為其他數字（透過移動一根木棒），檢查是否能使等式成立
4. 七段顯示器數字對應的木棒數量：
   - 0(6), 1(2), 2(5), 3(5), 4(4), 5(5), 6(6), 7(3), 8(7), 9(6)

### 複雜度
- 時間：O(L * 10)，L 為數字長度
- 空間：O(1)

### 檔案
- `10101/main.py`
- `10101/test_10101.py`

---

## Problem 10170 - The Hotel with Infinite Rooms

### 解題思路
第 n 個旅行團人數為 `S + n - 1`，住宿天數為 `S + n - 1` 天。

前 k 個旅行團總住宿天數：
```
total = S + (S+1) + ... + (S+k-1)
      = k * S + k*(k-1)/2
```

使用二分搜尋找到第 D 天所在的旅行團。

### 複雜度
- 時間：O(log D)
- 空間：O(1)

### 檔案
- `10170/main.py`
- `10170/test_10170.py`

---

## 執行測試

```bash
cd solutions/1114405014

# 各題測試
python3 10062/test_10062.py -v
python3 10071/test_10071.py -v
python3 10093/test_10093.py -v
python3 10101/test_10101.py -v
python3 10170/test_10170.py -v
```

---

## 測試結果

| Problem | Tests | Passed | Failed |
|---------|-------|--------|--------|
| 10062 | 3 | 3 | 0 |
| 10071 | 4 | 4 | 0 |
| 10093 | 3 | 3 | 0 |
| 10101 | 2 | 2 | 0 |
| 10170 | 3 | 3 | 0 |
| **Total** | **15** | **15** | **0** |

---

*Generated: 2026-04-08*
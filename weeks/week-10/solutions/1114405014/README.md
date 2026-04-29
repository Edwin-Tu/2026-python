# 1114405014 程式解題集

## 概述

本專案包含五道 UVa/ZeroJudge 經典題目的解答，采用 TDD（測試驅動開發）策略開發。

## 題目列表

| 題號 | 名稱 | 難度 | 類型 |
|------|------|------|------|
| 10226 | 限制排列 | 中等 | DFS/回溯 |
| 10235 | 就少一個插座用很不方便 | 困難 | 狀態壓縮 DP |
| 10242 | APIO2009 抢掠计划 | 困難 | 圖論/SPFA |
| 10252 | 王老師愛兩條線 | 中等 | 幾何/中位數 |
| 10268 | Dropping water balloons | 中等 | DP |

## 資料夾結構

```
1114405014/
├── 10226/
│   ├── main_annotated.py  # 含詳細中文註解
│   ├── main.py            # 純程式碼（已優化）
│   └── test_10226.py      # TDD 測試檔
├── 10235/
│   ├── main_annotated.py
│   ├── main.py            # 純程式碼（已優化）
│   └── test_10235.py
├── 10242/
│   ├── main_annotated.py
│   ├── main.py            # 純程式碼（已優化）
│   └── test_10242.py
├── 10252/
│   ├── main_annotated.py
│   ├── main.py            # 純程式碼（已優化）
│   └── test_10252.py
├── 10268/
│   ├── main_annotated.py
│   ├── main.py            # 純程式碼（已優化）
│   └── test_10268.py
├── README.md
└── pr.md
```

## 優化說明（與原版差異）

本版本對 `main.py` 進行了以下優化：

### 共同優化項目

1. **類型註解增強**：為函數參數和返回值添加完整的型別提示
2. **輸入處理改進**：統一使用 `sys.stdin.read().splitlines()` 並改善索引管理
3. **輸出處理優化**：使用 `sys.stdout.write()` 替代多次 `print()` 調用
4. **代碼簡化**：使用列表推導式、生成器表達式簡化代碼

### 各題目特定優化

#### 10226 - 限制排列
- 將 `forbidden` 參數從 `Dict[int, List[int]]` 改為 `List[Set[int]]`，提升查找效率
- 優化 `output_diff()` 函數，使用 `zip` 和 `enumerate` 簡化邏輯
- 簡化 `solve()` 中的輸入解析邏輯

#### 10235 - 就少一個插座用很不方便
- 使用 `directions` 元組列表替代多個 `if-elif` 判斷方向
- 使用 `next()` 和生成器表達式簡化尋找第一個未設定位
- 添加輸入驗證（`cell_count == 0` 的處理）

#### 10242 - APIO2009 抢掠计划
- 移除未使用的 `reverse_graph`
- 使用 `float('-inf')` 替代 `-10**18` 作為負無窮大
- 使用 `max()` 的 `default` 參數簡化結果計算
- 使用列表推導式簡化輸入處理

#### 10252 - 王老師愛兩條線
- 修復 shebang 行（`#!/usr/bin/env python3`）
- 簡化中位數計算邏輯
- 使用生成器表達式計算方案數

#### 10268 - Dropping water balloons
- 簡化 `min_trials()` 中的條件判斷
- 使用 `for t in range(1, 64)` 替代 `while` 循環
- 改善邊界條件處理

## 執行方式

### 執行測試

```bash
cd 1114405014/10226
python -m pytest test_10226.py

cd ../10235
python -m pytest test_10235.py

# ... 以此類推
```

### 執行解答

```bash
cd 1114405014/10226
python main.py < input.txt
```

## 開發說明

- 所有題目均包含測試檔（test_*.py）
- 主程式有兩個版本：
  - `main_annotated.py`: 含詳細繁體中文註解
  - `main.py`: 純程式碼版本（已優化）

## 參考資源

- [ZeroJudge 題目系統](https://zerojudge.tw/)
- [Yui Huang 題解](https://yuihuang.com/)

## 授權

本專案僅供學習使用。

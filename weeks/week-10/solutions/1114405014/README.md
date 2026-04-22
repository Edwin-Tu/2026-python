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
| 10268 | Dropping water balloons | 中等 | DP/二分搜 |

## 資料夾結構

```
1114405014/
├── 10226/
│   ├── main_annotated.py  # 含詳細中文註解
│   ├── main.py            # 純程式碼
│   └── test_10226.py      # TDD 測試檔
├── 10235/
│   ├── main_annotated.py
│   ├── main.py
│   └── test_10235.py
├── 10242/
│   ├── main_annotated.py
│   ├── main.py
│   └── test_10242.py
├── 10252/
│   ├── main_annotated.py
│   ├── main.py
│   └── test_10252.py
├── 10268/
│   ├── main_annotated.py
│   ├── main.py
│   └── test_10268.py
├── README.md
└── pr.md
```

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
  - `main.py`: 純程式碼版本

## 參考資源

- [ZeroJudge 題目系統](https://zerojudge.tw/)
- [Yui Huang 題解](https://yuihuang.com/)

## 授權

本專案僅供學習使用。

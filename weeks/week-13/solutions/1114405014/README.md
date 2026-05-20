# UVA 題解練習 — 學號 1114405014

採用 **TDD (Test-Driven Development)** 模式開發，先撰寫測試再實作程式碼。

## 目錄結構

```
1114405014/
├── README.md          # 本文件
├── TEST_LOG.md        # 測試記錄（Red/Green/Refactor 各階段結果）
├── test_inputs/       # 主程式測試用的樣本輸入檔
│   ├── input_11005.txt
│   ├── input_11063.txt
│   ├── input_11150.txt
│   ├── input_11321.txt
│   └── input_11332.txt
├── 11005/             # UVA 11005 — Cheapest Base
│   ├── main_11005.py      # 主程式（含待實作函式 + stdin/stdout）
│   ├── practise_11005.py  # 練習用副本
│   └── test_11005.py      # 單元測試（8 tests）
├── 11063/             # UVA 11063 — RGB to XYZ
│   ├── main_11063.py
│   ├── practise_11063.py
│   └── test_11063.py      # 8 tests
├── 11150/             # UVA 11150 — Frog Crossing Bridge
│   ├── main_11150.py
│   ├── practise_11150.py
│   └── test_11150.py      # 12 tests
├── 11321/             # UVA 11321 — Trap Placement
│   ├── main_11321.py
│   ├── practise_11321.py
│   └── test_11321.py      # 11 tests
└── 11332/             # UVA 11332 — Mirror Visibility
    ├── main_11332.py
    ├── practise_11332.py
    └── test_11332.py      # 11 tests
```

## 題目一覽

| 題號 | 題名 | 標籤 | 測試數 |
|:----:|------|------|:------:|
| 11005 | Cheapest Base | 進位制轉換、窮舉 | 8 |
| 11063 | RGB to XYZ | 色彩轉換、矩陣運算 | 8 |
| 11150 | Frog Crossing Bridge | DP、路徑壓縮 | 12 |
| 11321 | Trap Placement | BFS/DFS、連通性 | 11 |
| 11332 | Mirror Visibility | 計算幾何、線段相交 | 11 |

## TDD 流程

```
Phase 1 — Red   : 撰寫測試 → 執行確認全部失敗 ✅（目前在此階段）
Phase 2 — Green : 實作 `main_XX.py` 中的函式 → 測試全部通過
Phase 3 — Refactor: 重構程式碼，維持測試通過
```

## 如何使用

```bash
# 安裝 pytest
pip install pytest

# 執行所有單元測試
python -m pytest solutions/1114405014/ -v

# 執行單一題目測試
python -m pytest solutions/1114405014/11005/ -v

# 執行主程式（stdin 輸入）
python solutions/1114405014/11005/main_11005.py < test_inputs/input_11005.txt
```

## 各題函式介面

| 題號 | 函式 | 輸入 | 輸出 |
|:----:|------|------|------|
| 11005 | `cheapest_base(costs, n)` | `list[int]` 36字元成本, `int` 查詢數字 | `list[int]` 最低成本進位制列表 |
| 11063 | `rgb_to_xyz(pixels)` | `list[tuple[int,int,int]]` RGB像素 | `tuple[list[tuple[float,float,float]], float]` XYZ列表 + 平均Y |
| 11150 | `min_stones(L, S, T, stones)` | `int`橋長, `int`最小/大跳距, `list[int]`石子位置 | `int` 最少踩到石子數 |
| 11321 | `can_place_trap(N, M, traps)` | `int`行列, `list[tuple[int,int]]`陷阱座標 | `list[str]` 結果 ("<(_ _)>" / ">_<") |
| 11332 | `visible_mirrors(mirrors)` | `list[tuple[int,int,int,int]]` 線段端點 | `list[int]` 0/1 可見標記 |

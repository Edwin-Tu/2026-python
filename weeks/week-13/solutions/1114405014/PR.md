## Summary

以 TDD 模式為 5 題 UVA 題目建立測試框架與主程式，包含完整的 Red 階段測試用例與 stdin/stdout I/O 流程。

## Changes

### 新增檔案

| 檔案 | 說明 |
|------|------|
| `11005/main_11005.py` | Cheapest Base 主程式 + `cheapest_base()` stub |
| `11005/practise_11005.py` | 練習用副本 |
| `11005/test_11005.py` | 8 個單元測試 |
| `11063/main_11063.py` | RGB to XYZ 主程式 + `rgb_to_xyz()` stub |
| `11063/practise_11063.py` | 練習用副本 |
| `11063/test_11063.py` | 8 個單元測試 |
| `11150/main_11150.py` | Frog Crossing Bridge 主程式 + `min_stones()` stub |
| `11150/practise_11150.py` | 練習用副本 |
| `11150/test_11150.py` | 12 個單元測試 |
| `11321/main_11321.py` | Trap Placement 主程式 + `can_place_trap()` stub |
| `11321/practise_11321.py` | 練習用副本 |
| `11321/test_11321.py` | 11 個單元測試 |
| `11332/main_11332.py` | Mirror Visibility 主程式 + `visible_mirrors()` stub |
| `11332/practise_11332.py` | 練習用副本 |
| `11332/test_11332.py` | 11 個單元測試 |
| `test_inputs/input_*.txt` | 各題主程式測試樣本輸入 |
| `TEST_LOG.md` | TDD 測試過程記錄（Phase 1 Red） |
| `README.md` | 專案說明文件 |
| `PR.md` | 本文件 |

### TDD 狀態

- **Phase 1 — Red** ✅ 完成
  - 50 個測試全部撰寫完畢
  - 執行確認全部為 NotImplementedError（紅燈）
  - 主程式 stdin/stdout 解析流程驗證通過
- **Phase 2 — Green** ⏳ 待實作
- **Phase 3 — Refactor** ⏳ 待完成

### 測試覆蓋重點

- **11005**: 單一進位、多重進位同成本、n=0 邊界、大數值
- **11063**: 全黑/全白像素、公式驗算、平均亮度、小數位數格式
- **11150**: 無石子、可閃避、強制踩石、s=t 邊界、大 L 壓縮
- **11321**: 單行封死、L 形不擋、整列封路、重複陷阱、連通性檢查
- **11332**: 可見/不可見鏡子、被遮擋、通過原點、空輸入

## How to Test

```bash
pip install pytest
python -m pytest solutions/1114405014/ -v
```

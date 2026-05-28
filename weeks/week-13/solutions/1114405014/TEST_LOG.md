# TEST_LOG.md — Red → Green 執行紀錄

## Red 階段（測試先寫，預期失敗）

- 2026-05-28 撰寫 `tests/test_task1.py` 與 `tests/test_task2.py`
- 執行 `python -m unittest discover -s tests -p "test_*.py" -v`，因尚未實作函式，所有測試皆 Fail（紅色）

## Green 階段（實作後全部通過）

- 2026-05-28 完成 `task1_grouped_bar.py` 與 `task2_zipcode_heatmap.py` 實作
- 執行 `python -m unittest discover -s tests -p "test_*.py" -v`，全部測試 Pass（綠色）

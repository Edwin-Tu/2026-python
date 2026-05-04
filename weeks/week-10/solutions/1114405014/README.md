# Week 10 Homework Template

## 專案說明

本專案為 Week 10 回家作業模板，主要任務如下：

1. Task 1：CSV 轉 JSON
2. Task 2：JSON 轉 XML
3. Task 3：使用 timeit 結果產生耗時比較圖

## 專案架構

```text
.
├── task1_csv_to_json.py
├── task2_json_to_xml.py
├── task3_plot_comparison.py
├── tests/
│   ├── test_task1.py
│   └── test_task2.py
├── TIMING_REPORT.md
├── TEST_LOG.md
├── AI_USAGE.md
└── README.md
```

## 執行測試

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 執行任務

```bash
python task1_csv_to_json.py
python task2_json_to_xml.py
python task3_plot_comparison.py
```

## TDD 流程建議

1. 先執行測試，確認 Red。
2. 實作最小功能，讓測試通過 Green。
3. 重構程式，保持測試通過 Refactor。

## 注意事項

- CSV 建議使用 `encoding="utf-8-sig"`。
- JSON 輸出建議使用 `ensure_ascii=False`。
- `output/` 資料夾應由程式自動建立。
- 測試程式不要依賴真實 CSV，應使用小型假資料。

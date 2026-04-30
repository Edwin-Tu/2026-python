# Week 10 作業解答 - 學號 1114405014

本目錄包含 Python 程式設計週期第十週的作業解答，涵蓋檔案處理、資料分析與視覺化、裝飾器等主題。

## 目錄結構

```
.
├── A07-apply-to-student-zip.py                # 學生資料分析（含詳細註解）
├── A07-apply-to-student-zip_practise.py       # A07 純程式碼練習檔
├── A08-seaborn-college-trend.py              # 學院趨勢視覺化（含詳細註解）
├── A08-seaborn-college-trend_practise.py     # A08 純程式碼練習檔
├── U01-timeit-decorator.py                   # 計時裝飾器與效能比較（含詳細註解）
├── U01-timeit-decorator_practise.py          # U01 純程式碼練習檔
├── README.md                                 # 本文件
└── pr.md                                     # Pull Request 描述
```

## 檔案說明

### A07 - 學生資料綜合應用分析
**檔案：** `A07-apply-to-student-zip.py`  
**主題：** 綜合應用 Python I/O 技巧處理真實學生資料壓縮檔

**學習重點：**
- `zipfile` 模組：不解壓直接讀取壓縮檔內容
- `pathlib`：跨平台路徑處理
- `csv.DictReader`：讀取 CSV 格式資料
- `io.StringIO`：將位元組轉為檔案類似物件
- `tempfile.TemporaryDirectory`：沙箱環境輸出
- `pickle`：序列化統計結果
- `collections.Counter`：統計系所與入學方式分布

**資料來源：** `assets/npu-stu-109-114-anon.zip`（6 屆新生資料庫）

---

### A08 - 學院生源趨勢視覺化
**檔案：** `A08-seaborn-college-trend.py`  
**主題：** 使用 seaborn 繪製 109~114 學年各學院新生人數分析圖

**學習重點：**
- `pandas` DataFrame 資料處理
- `seaborn` 與 `matplotlib` 資料視覺化
- 折線圖與堆疊長條圖繪製
- 中文字型跨平台設定
- 將統計結果轉為長格式（long-form）資料

**相依套件：**
```bash
pip install seaborn matplotlib pandas
```

---

### U01 - 計時裝飾器實作
**檔案：** `U01-timeit-decorator.py`  
**主題：** 從重複計時程式碼出發，學習裝飾器設計模式與資料格式效能比較

**學習重點：**
- Python 裝飾器（Decorator）基礎與進階
- `functools.wraps` 保留原函式 metadata
- `time.perf_counter()` 高精度計時
- CSV、JSON、XML 三種資料格式解析速度比較
- 關注點分離（Separation of Concerns）的程式設計原則

**實驗結果：**
- JSON 通常最快（C 語言實作）
- XML 通常最慢（文字解析開銷大）
- CSV 介於中間（格式簡單但需手動轉型）

---

## 練習檔案使用說明

每個主檔案都有對應的 `_practise.py` 版本：
- **主檔案**：包含詳細的繁體中文註解，說明每一段程式碼的功能與原理
- **練習檔案**：純程式碼版本（無註解），適合：
  - 自我測試：嘗試自己添加註解
  - 程式碼複習：專注於邏輯結構
  - 教學用途：提供給學生練習

## 執行方式

```bash
# 進入作業目錄
cd /mnt/d/Edwin/program/program-python/2026-python/weeks/week-10/solutions/1114405014

# 執行 A07 學生資料分析
python A07-apply-to-student-zip.py

# 執行 A08 視覺化（需先安裝相依套件）
python A08-seaborn-college-trend.py

# 執行 U01 計時裝飾器測試
python U01-timeit-decorator.py
```

## 注意事項

1. A07 與 A08 需要存取 `assets/npu-stu-109-114-anon.zip` 資料檔，請確保路徑正確
2. A08 需要安裝 `seaborn`、`matplotlib`、`pandas` 套件
3. 執行 A08 時會產生 `A08-college-trend.png` 圖檔（使用 'x' 模式，已存在則不覆蓋）

## 學習資源

本作業對應課本章節：
- 第 5 章：檔案與 I/O 處理
- 第 6 章：裝飾器與高階函式特性
- 第 10 章：資料視覺化基礎

---

**學號：** 1114405014  
**學期：** 2026 Python 程式設計  
**週次：** Week 10

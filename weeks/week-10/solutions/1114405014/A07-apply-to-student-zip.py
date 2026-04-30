# A07. 綜合應用：把 I/O 技巧套到真實學生資料
# Bloom: Apply — 複習並組合 R01~A06 的 API
#
# 本程式示範如何結合多個 Python I/O 技巧處理真實的學生資料壓縮檔
# 資料來源：assets/npu-stu-109-114-anon.zip（6 屆新生資料庫，學號已匿名）
#
# 使用到的 Python 標準庫技巧對照：
#   • 5.11 pathlib 組路徑：使用 Path 物件處理檔案路徑
#   • 5.12 exists 檢查：確認資料檔是否存在
#   • 5.7  zipfile：不解壓直接讀取壓縮檔內容
#   • 5.1  encoding='utf-8-sig'：處理 Excel 輸出 CSV 的 BOM（位元組順序標記）
#   • 5.6  io.StringIO：將 bytes 轉換為 csv 模組可讀的 file-like 物件
#   • 5.19 TemporaryDirectory：建立沙箱環境輸出檔案，自動清理
#   • 5.5  open(..., 'x')：排他性寫入，避免覆蓋已存在的檔案
#   • 5.21 pickle：序列化統計結果，便於日後快速載入
#   • 5.2  print(file=...)：將輸出導向檔案，用於產生 Markdown 報告

import csv
import io
import pickle
import tempfile
import zipfile
from collections import Counter
from pathlib import Path

# ═══════════════════════════════════════════════════════════
# 步驟一：定位資料檔（5.11 pathlib / 5.12 exists）
# ═══════════════════════════════════════════════════════════

# 取得目前腳本所在目錄的絕對路徑
HERE = Path(__file__).resolve().parent

# 使用 pathlib 的除法運算子組合路徑（跨平台相容）
# 這裡往上三層找到專案根目錄，再進入 assets 資料夾
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"

# 斷言檢查：確保資料檔存在，否則給出清楚錯誤訊息
assert ZIP_PATH.exists(), f"找不到資料：{ZIP_PATH}"
print("資料來源:", ZIP_PATH.name)

# ═══════════════════════════════════════════════════════════
# 步驟二：不解壓讀取 zip 內的 CSV 檔（5.7 + 5.6 + 5.1）
# ═══════════════════════════════════════════════════════════

def iter_year_csv(zip_path: Path):
    """
    逐年度讀取 zip 壓縮檔中的 CSV 檔案
    參數：
        zip_path: zip 檔案的 Path 物件
    回傳：
        生成器，每次 yield (年度字串, 標頭列表, 資料列列表)
    """
    with zipfile.ZipFile(zip_path) as z:
        # infolist() 回傳 zip 內所有檔案的資訊物件
        for info in z.infolist():
            # 舊版 zip 壓縮檔的中文檔名可能會有 cp437 編碼錯誤
            # 此資料集的檔名已是乾淨的 utf-8 編碼
            name = info.filename

            # 只處理 CSV 檔案
            if not name.endswith(".csv"):
                continue

            # 從檔名前 3 個字元取得學年度（如 '109'、'110'...'114'）
            year = name[:3]  # '109'~'114'

            # z.read(info) 讀取檔案內容為 bytes
            raw = z.read(info)

            # 5.1: 使用 utf-8-sig 解碼，會自動去除 BOM（\ufeff）
            # Excel 輸出的 CSV 常會在開頭加上 BOM
            text = raw.decode("utf-8-sig")

            # 5.6: 使用 io.StringIO 將字串轉為 file-like 物件
            # 這樣 csv.reader 就可以像讀檔一樣讀取字串內容
            reader = csv.reader(io.StringIO(text))

            # 將所有列讀入記憶體：第一列是標頭，其餘是資料
            rows = list(reader)

            # yield 標頭（第一列）和資料列（其餘列）
            yield year, rows[0], rows[1:]

# ═══════════════════════════════════════════════════════════
# 步驟三：跨屆統計分析
# ═══════════════════════════════════════════════════════════

# summary 字典：以年度為鍵，值為該年度的統計資訊
# 結構：{年度: {'total': 總人數, 'by_dept': 系所計數器, 'by_entry': 入學方式計數器}}
summary = {}

# all_depts：累計所有年度各系所的總人數
all_depts = Counter()

# 遍歷每一年的 CSV 資料
for year, header, rows in iter_year_csv(ZIP_PATH):
    # 找出「系所名稱」和「入學方式」欄位的索引位置
    dept_idx  = header.index("系所名稱")
    entry_idx = header.index("入學方式")

    # 使用 Counter 統計該年度各系所的人數
    # 條件判斷 len(r) > dept_idx 避免資料不完整導致 index out of range
    by_dept  = Counter(r[dept_idx]  for r in rows if len(r) > dept_idx)

    # 統計該年度各入學方式的人數
    by_entry = Counter(r[entry_idx] for r in rows if len(r) > entry_idx)

    # 將統計結果存入 summary 字典
    summary[year] = {
        "total":    len(rows),       # 該年度總人數
        "by_dept":  by_dept,         # 系所分布計數器
        "by_entry": by_entry,        # 入學方式分布計數器
    }

    # 更新累計系所人數（用於計算全體最熱門系所）
    all_depts.update(by_dept)

# ═══════════════════════════════════════════════════════════
# 步驟四：終端機輸出統計結果
# ═══════════════════════════════════════════════════════════

print("\n=== 6 屆新生人數 ===")
for year in sorted(summary):  # 依年度排序輸出
    print(f"  {year} 學年：{summary[year]['total']:>4} 人")

print("\n=== 全體最熱門 5 個系所（累計 6 屆） ===")
# most_common(n) 回傳出現次數最多的 n 個項目
for dept, n in all_depts.most_common(5):
    print(f"  {n:>4} 人  {dept}")

print("\n=== 114 學年入學方式分布 ===")
for kind, n in summary["114"]["by_entry"].most_common():
    print(f"  {n:>4} 人  {kind}")

# ═══════════════════════════════════════════════════════════
# 步驟五：沙箱產生報告（5.19 + 5.5 + 5.2）與快照（5.21）
# ═══════════════════════════════════════════════════════════

# 使用 TemporaryDirectory 建立臨時目錄作為沙箱
# 優點：with 區塊結束後自動清理，不會在專案留下垃圾檔案
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)  # 轉為 Path 物件

    # 5.21: 使用 pickle 將整個 summary 字典序列化保存
    # 好處：日後可直接載入，不需重新分析原始資料
    snap = tmp / "summary.pkl"
    with open(snap, "wb") as f:
        pickle.dump(summary, f)
    print(f"\n快照寫入 {snap.name}：{snap.stat().st_size} bytes")

    # 5.5: 使用 'x' 模式開啟檔案 → 若檔案已存在會拋出 FileExistsError
    # 這確保不會意外覆蓋已有的報告
    report = tmp / "report.md"
    with open(report, "x", encoding="utf-8") as f:

        # 5.2: 使用 print(file=...) 將輸出導向檔案
        # 這比 f.write() 更方便，因為 print 會自動處理換行
        print("# 6 屆新生概況報告\n", file=f)

        # 輸出 Markdown 格式的表格
        print("| 學年 | 人數 | 第一大系所 |", file=f)
        print("|------|------|------------|", file=f)

        for year in sorted(summary):
            # most_common(1)[0] 取得出現次數最多的第一個項目
            top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]
            print(f"| {year} | {summary[year]['total']} | "
                  f"{top_dept} ({top_n}) |", file=f)

    # 5.1: 讀回 Markdown 報告內容並印出（文字讀檔示範）
    print("\n=== Markdown 報告預覽 ===")
    print(report.read_text(encoding="utf-8"))

    # 驗證 pickle 是否能正確讀回（檢查型別與內容一致性）
    with open(snap, "rb") as f:
        loaded = pickle.load(f)
    print("pickle 讀回 key:", sorted(loaded.keys()))

# 離開 with 區塊 → 臨時目錄 tmp 會自動刪除，不在專案留下任何檔案
print("\n(沙箱已自動清理)")

# ═══════════════════════════════════════════════════════════
# 課堂延伸挑戰
# ═══════════════════════════════════════════════════════════
# 1) 把報告改寫到 HERE / 'report.md'：
#    改用 'w' 模式會覆蓋現有檔案，'x' 模式在檔案存在時會報錯
#
# 2) 加一欄「女性比例」：
#    找出性別欄位後用 Counter 統計男女比例
#    gender_idx = header.index("性別")
#    by_gender = Counter(r[gender_idx] for r in rows if len(r) > gender_idx)
#
# 3) 把 summary 壓縮存成 summary.pkl.gz：
#    import gzip
#    with gzip.open(tmp / 'summary.pkl.gz', 'wb') as f:
#        pickle.dump(summary, f)
#
# 4) 跨屆找出「人數逐年下降最明顯」的系所：
#    需要把 by_dept 按年排成時間序列，計算各系所的趨勢斜率

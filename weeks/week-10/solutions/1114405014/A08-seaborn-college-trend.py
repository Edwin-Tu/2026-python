# A08. 用 seaborn 畫 109~114 學年各學院生源分析圖
# Bloom: Apply — 把 A07 的統計成果交給視覺化套件
#
# 本程式讀取學生資料壓縮檔，整理成 Pandas DataFrame，並使用 seaborn 繪製
# 109~114 學年各學院新生人數的趨勢圖與堆疊長條圖
#
# 需要安裝：pip install seaborn matplotlib pandas
#
# 使用到的 I/O 技巧（延續 A07）：
#   • 5.7  zipfile：不解壓直接讀取壓縮檔內容
#   • 5.1  utf-8-sig：去除 Excel 輸出 CSV 的 BOM
#   • 5.6  io.StringIO：將字串轉為 csv.DictReader 可讀的物件
#   • 5.11 pathlib：跨平台的路徑處理
#   • 5.5  open('x')：排他性寫入，避免覆蓋已存在的輸出圖檔

import csv
import io
import platform
import zipfile
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ═══════════════════════════════════════════════════════════
# 區塊一：中文字型設定（跨平台相容）
# ═══════════════════════════════════════════════════════════

# 根據作業系統選擇可用的中文字型
# matplotlib 在 macOS 預設可能抓不到中文字型，需手動指定
_CJK_FONTS = {
    "Darwin":  ["Heiti TC", "Arial Unicode MS", "PingFang TC"],  # macOS
    "Windows": ["Microsoft JhengHei", "Microsoft YaHei"],        # Windows
    "Linux":   ["Noto Sans CJK TC", "WenQuanYi Zen Hei"],        # Linux
}.get(platform.system(), ["sans-serif"])  # 預設：如果都不是就用 sans-serif


def _apply_cjk_font():
    """
    套用中文字型設定到 matplotlib
    注意：sns.set_theme() 會重設 rcParams，所以需要在它之後再呼叫此函式
    """
    # 將 CJK 字型加到現有字型列表的最前面（優先使用）
    plt.rcParams["font.sans-serif"] = _CJK_FONTS + plt.rcParams["font.sans-serif"]
    plt.rcParams["font.family"] = "sans-serif"
    # 解決負號顯示為方塊的問題
    plt.rcParams["axes.unicode_minus"] = False


# 初始套用中文字型
_apply_cjk_font()

# ═══════════════════════════════════════════════════════════
# 區塊二：系所 → 學院 對照表（NPU 國立澎湖科技大學三大學院）
# ═══════════════════════════════════════════════════════════

DEPT_TO_COLLEGE = {
    # 人文暨管理學院（6 個系）
    "應用外語系":       "人文暨管理學院",
    "航運管理系":       "人文暨管理學院",
    "行銷與物流管理系": "人文暨管理學院",
    "觀光休閒系":       "人文暨管理學院",
    "資訊管理系":       "人文暨管理學院",
    "餐旅管理系":       "人文暨管理學院",
    # 海洋資源暨工程學院（3 個系）
    "水產養殖系":       "海洋資源暨工程學院",
    "海洋遊憩系":       "海洋資源暨工程學院",
    "食品科學系":       "海洋資源暨工程學院",
    # 電資工程學院（3 個系）
    "資訊工程系":       "電資工程學院",
    "電信工程系":       "電資工程學院",
    "電機工程系":       "電資工程學院",
}

# ═══════════════════════════════════════════════════════════
# 區塊三：定位資料檔（5.11 pathlib）
# ═══════════════════════════════════════════════════════════

HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
assert ZIP_PATH.exists(), f"找不到：{ZIP_PATH}"

# ═══════════════════════════════════════════════════════════
# 區塊四：讀取 zip 內 CSV 並轉為 Pandas DataFrame
#         （5.7 zipfile + 5.6 io.StringIO + 5.1 utf-8-sig）
# ═══════════════════════════════════════════════════════════

def load_long_frame(zip_path: Path) -> pd.DataFrame:
    """
    讀取 zip 壓縮檔內所有 CSV，轉換為長格式（long-form）DataFrame
    欄位：學年（int）、學院（str）、系所（str）
    """
    records = []  # 用於收集所有記錄的列表

    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            # 只處理 CSV 檔案
            if not info.filename.endswith(".csv"):
                continue

            # 從檔名前 3 個字元取得學年度
            year = info.filename[:3]  # '109'..'114'

            # 讀取並解碼：去 BOM（utf-8-sig 會自動處理 \ufeff）
            text = z.read(info).decode("utf-8-sig")

            # 使用 csv.DictReader 讀取，每列是字典（鍵為標頭）
            reader = csv.DictReader(io.StringIO(text))

            for row in reader:
                dept = row.get("系所名稱", "").strip()
                if not dept:
                    continue  # 跳過沒有系所名稱的資料列

                # 將系所對應到學院，找不到則標示為「其他」
                college = DEPT_TO_COLLEGE.get(dept, "其他")

                records.append({
                    "學年": int(year),
                    "學院": college,
                    "系所": dept,
                })

    # 將記錄列表轉換為 Pandas DataFrame
    return pd.DataFrame.from_records(records)


# 載入資料
df = load_long_frame(ZIP_PATH)
print("總筆數:", len(df))
print(df.head())

# ═══════════════════════════════════════════════════════════
# 區塊五：資料整理 — 各學年 × 各學院 的人數統計
# ═══════════════════════════════════════════════════════════

# 使用 groupby 分組統計，然後 reset_index 將結果轉為 DataFrame
pivot = (df.groupby(["學年", "學院"])
           .size()                     # 計算每組的數量
           .reset_index(name="人數"))  # 將結果命名為「人數」欄

print("\n各學年各學院:")
# pivot 顯示：將學年設為索引，學院設為欄，人數設為值
print(pivot.pivot(index="學年", columns="學院", values="人數"))

# ═══════════════════════════════════════════════════════════
# 區塊六：使用 seaborn 繪製視覺化圖表
# ═══════════════════════════════════════════════════════════

# 設定 seaborn 主題：白底網格、大字體、Set2 調色盤
sns.set_theme(style="whitegrid", context="talk", palette="Set2")

# 重新套用中文字型（sns.set_theme 會重設 rcParams）
_apply_cjk_font()

# 建立 1×2 的子圖：左圖較寬（比例 1.3），右圖較窄（比例 1）
fig, axes = plt.subplots(1, 2, figsize=(15, 6),
                         gridspec_kw={"width_ratios": [1.3, 1]})

# ── 圖 A：折線圖 + 散點圖 —— 各學院逐年趨勢 ──────────────
sns.lineplot(data=pivot, x="學年", y="人數", hue="學院",
             marker="o", markersize=10, linewidth=2.5, ax=axes[0])

axes[0].set_title("109–114 各學院新生人數趨勢", fontsize=16, pad=12)
axes[0].set_xticks(sorted(pivot["學年"].unique()))  # 明確設定 x 軸刻度
axes[0].legend(title="學院", loc="upper right", frameon=True)

# 在每個資料點上標註人數
for _, r in pivot.iterrows():  # _ 忽略索引
    axes[0].annotate(int(r["人數"]),                      # 標註文字（轉為整數）
                     (r["學年"], r["人數"]),               # 標註位置
                     textcoords="offset points",
                     xytext=(0, 8),                       # 向上偏移 8 點
                     ha="center", fontsize=9, alpha=0.8)  # 水平置中、半透明

# ── 圖 B：堆疊長條圖 —— 每年學院人數占比 ─────────────────
# 將長格式轉為寬格式：學年為索引，學院為欄，人數為值
pivot_wide = pivot.pivot(index="學年", columns="學院", values="人數").fillna(0)

# 繪製堆疊長條圖
pivot_wide.plot(kind="bar", stacked=True,
                ax=axes[1], colormap="Set2", width=0.75, edgecolor="white")

axes[1].set_title("各學年學院結構（堆疊）", fontsize=16, pad=12)
axes[1].set_ylabel("人數")
axes[1].tick_params(axis="x", rotation=0)  # x 軸文字不旋轉
axes[1].legend(title="學院", loc="upper right", fontsize=9)

# 設定整張圖的總標題
fig.suptitle("國立澎湖科技大學  109–114 學年新生生源分析",
             fontsize=18, fontweight="bold", y=1.02)

# 自動調整子圖間距，避免重疊
fig.tight_layout()

# ═══════════════════════════════════════════════════════════
# 區塊七：輸出圖檔（5.5 'x' 模式 — 不覆蓋已存在的檔案）
# ═══════════════════════════════════════════════════════════

OUT = HERE / "A08-college-trend.png"

try:
    # 'xb' 模式：若檔案已存在則拋出 FileExistsError
    with open(OUT, "xb") as f:
        # dpi=150 設定解析度；bbox_inches="tight" 確保邊界緊湊
        fig.savefig(f, dpi=150, bbox_inches="tight")
    print(f"\n圖檔已寫入：{OUT.name}")
except FileExistsError:
    print(f"\n{OUT.name} 已存在，保留舊檔（要重畫請先刪除）")

# 顯示圖表（在互動式環境中會彈出視窗）
plt.show()

# ═══════════════════════════════════════════════════════════
# 延伸挑戰
# ═══════════════════════════════════════════════════════════
# 1) 改畫「各系所」熱力圖：
#    pivot_by_dept = df.groupby(["學年", "系所"]).size().unstack(fill_value=0)
#    sns.heatmap(pivot_by_dept, annot=True, fmt='d', cmap='YlOrRd')
#
# 2) 加一張圓餅圖：114 學年學院占比
#    college_114 = df[df["學年"]==114]["學院"].value_counts()
#    plt.pie(college_114, labels=college_114.index, autopct='%1.1f%%')
#
# 3) 把年度 x 軸改成 '109學年'~'114學年' 字串：
#    year_labels = [f"{y}學年" for y in sorted(df["學年"].unique())]
#    axes[0].set_xticklabels(year_labels)


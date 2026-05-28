from pathlib import Path
import csv
import matplotlib.pyplot as plt
import matplotlib


def _setup_font():
    for candidate in [
        "Noto Sans CJK TC",
        "WenQuanYi Micro Hei",
        "Source Han Sans TW",
        "Microsoft JhengHei",
        "Apple LiGothic",
    ]:
        try:
            matplotlib.font_manager.findfont(candidate, fallback_to_default=False)
            matplotlib.rcParams["font.sans-serif"] = [candidate, "sans-serif"]
            matplotlib.rcParams["axes.unicode_minus"] = False
            return
        except Exception:
            continue


_setup_font()


def load_year(year: int, data_dir: Path) -> dict[str, int]:
    data_path = data_dir / f"{year}年新生資料庫.csv"
    counts: dict[str, int] = {}
    with open(data_path, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dept = row["系所名稱"]
            counts[dept] = counts.get(dept, 0) + 1
    return counts


def get_top_depts(year_data: dict[int, dict], top_n: int = 8) -> list[str]:
    totals: dict[str, int] = {}
    for dept_counts in year_data.values():
        for dept, count in dept_counts.items():
            totals[dept] = totals.get(dept, 0) + count
    sorted_depts = sorted(totals, key=totals.get, reverse=True)
    return sorted_depts[:top_n]


def main():
    data_dir = Path(__file__).parent.parent.parent.parent.parent / "assets" / "stu-data"
    years = [112, 113, 114]
    year_data = {y: load_year(y, data_dir) for y in years}
    top_depts = get_top_depts(year_data, top_n=8)

    fig, ax = plt.subplots(figsize=(12, 8))
    y_pos = range(len(top_depts))
    bar_height = 0.25
    colors = ["#4A90D9", "#7EC8E3", "#FFB347"]

    for i, year in enumerate(years):
        vals = [year_data[year].get(d, 0) for d in top_depts]
        ax.barh(
            [p + i * bar_height for p in y_pos],
            vals,
            bar_height,
            label=f"{year} 學年度",
            color=colors[i],
        )

    ax.set_yticks([p + bar_height for p in y_pos])
    ax.set_yticklabels(top_depts, fontsize=9)
    ax.set_xlabel("招生人數")
    ax.set_title("112～114 學年度各系招生人數比較")
    ax.legend(loc="lower right")
    ax.invert_yaxis()

    for i, year in enumerate(years):
        for j, d in enumerate(top_depts):
            v = year_data[year].get(d, 0)
            if v > 0:
                ax.text(
                    v + 0.5,
                    j + i * bar_height,
                    str(v),
                    va="center",
                    fontsize=7,
                )

    plt.tight_layout()
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    plt.savefig(output_dir / "task1.png", dpi=150)
    print("Task 1 圖表已儲存至 output/task1.png")


if __name__ == "__main__":
    main()

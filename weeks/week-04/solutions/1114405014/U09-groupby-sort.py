# U9. groupby 為何一定要先 sort（1.15）

# 匯入 groupby：可將「連續且相同鍵值」的資料分組
from itertools import groupby

# 匯入 itemgetter：方便依照字典中的某個欄位取值
from operator import itemgetter

# 建立範例資料
rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

# 先印出原始資料
print("原始資料：")
for row in rows:
    print(row)

# ----------------------------
# 沒有排序就直接 groupby
# ----------------------------
# groupby 只會把「連續且相同」的資料分成同一組
# 這裡雖然有兩筆 date 都是 07/02/2012
# 但它們中間被 07/01/2012 隔開了
# 所以 groupby 會把 07/02/2012 分成兩組
print("\n【未排序直接分組】")
for k, g in groupby(rows, key=itemgetter('date')):
    group_list = list(g)   # 把這一組轉成 list，方便印出
    print("分組鍵 =", k, "，分組內容 =", group_list)

# ----------------------------
# 先排序再 groupby
# ----------------------------
# 先依 date 排序，讓相同 date 的資料排在一起
rows.sort(key=itemgetter('date'))

# 印出排序後資料
print("\n排序後的資料：")
for row in rows:
    print(row)

# 排序後再做 groupby
# 這樣相同 date 就會連在一起，分組才會正確
print("\n【排序後再分組】")
for k, g in groupby(rows, key=itemgetter('date')):
    group_list = list(g)   # 把這一組轉成 list，方便印出
    print("分組鍵 =", k, "，分組內容 =", group_list)
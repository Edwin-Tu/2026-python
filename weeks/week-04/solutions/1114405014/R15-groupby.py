# 匯入 groupby：可將「連續且相同鍵值」的資料分組
from itertools import groupby

# 匯入 itemgetter：方便依照字典中的某個欄位取值
from operator import itemgetter

# 範例資料：每筆資料都是一個字典，包含日期與地址
# 這裡特別放入重複日期，才能看出 groupby 的分組效果
rows = [
    {'date': '07/01/2012', 'address': '台北市信義區'},
    {'date': '07/02/2012', 'address': '新北市板橋區'},
    {'date': '07/01/2012', 'address': '台中市西屯區'},
    {'date': '07/02/2012', 'address': '高雄市左營區'},
    {'date': '07/03/2012', 'address': '台南市東區'}
]

# 先依照 date 欄位排序
# 因為 groupby 只能將「相鄰且鍵值相同」的資料分在一起
# 所以如果不先排序，相同日期的資料可能會被分散，導致分組錯誤
rows.sort(key=itemgetter('date'))

# 先印出排序後的資料，方便觀察
print("排序後的資料：")
for row in rows:
    print(row)

print("\n開始分組：")

# 使用 groupby 依照 date 欄位分組
# date 會是目前這一組的日期
# items 會是該日期對應的一組資料（是一個可迭代物件）
for date, items in groupby(rows, key=itemgetter('date')):
    # 印出目前分組的日期
    print(f"\n日期：{date}")
    
    # 逐筆取出這一組中的資料
    for i in items:
        # 印出該日期底下的每一筆資料
        print(f"  地址：{i['address']}")
# U5. 優先佇列為何要加 index（1.5）

# 匯入 heapq 模組
# heapq 可以用來實作優先佇列
import heapq

# 自訂一個 Item 類別
class Item:
    def __init__(self, name):
        self.name = name

    # 方便印出物件內容，讓結果更好看
    def __repr__(self):
        return f"Item({self.name!r})"

# 建立空的優先佇列
pq = []

# ----------------------------
# 錯誤示範：只放 (priority, item)
# ----------------------------
# 如果 priority 一樣，heapq 會繼續比較第二個元素 item
# 但 Item 物件之間沒有定義 < 比較方式
# 因此會發生 TypeError

print("【錯誤示範】只放 (priority, item)：" )

try:
    bad_pq = []
    heapq.heappush(bad_pq, (-1, Item('a')))
    heapq.heappush(bad_pq, (-1, Item('b')))  # 這裡會出錯
except TypeError as e:
    print("發生錯誤：", e)

# ----------------------------
# 正確示範：放 (priority, index, item)
# ----------------------------
# 加入 index 後：
# 1. 先比較 priority
# 2. 如果 priority 一樣，再比較 index
# 3. 就不需要直接比較 Item 物件
# 這樣可避免 TypeError

print("\n【正確示範】加入 index 避免比較 Item：")

# 建立空的優先佇列
pq = []

# index 用來保證每筆資料都有可比較的第二順位
idx = 0

# 加入第一筆資料
heapq.heappush(pq, (-1, idx, Item('a')))
idx += 1

# 加入第二筆資料
heapq.heappush(pq, (-1, idx, Item('b')))
idx += 1

# 印出目前的優先佇列內容
print("目前 pq =", pq)

# 依序取出資料
# heappop 會每次取出「最小值」
# 這裡因為 priority 用負數，所以數值越小代表優先權越高
item1 = heapq.heappop(pq)
print("第一次取出：", item1)

item2 = heapq.heappop(pq)
print("第二次取出：", item2)
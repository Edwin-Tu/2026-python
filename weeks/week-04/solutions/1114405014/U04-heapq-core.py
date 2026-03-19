# U4. heap 為何能高效拿 Top-N（1.4）

# 匯入 heapq 模組
# heapq 可以把串列整理成「最小堆積（min heap）」
import heapq

# 原始數字串列
nums = [5, 1, 9, 2]

# 複製一份 nums，避免直接修改原本資料
h = nums[:]

# 將串列轉成 heap 結構
# 轉換後 h[0] 會永遠是目前最小值
heapq.heapify(h)

# 印出原始資料
print("原始串列 nums =", nums)

# 印出轉成 heap 後的內容
print("heapify 後的 h =", h)

# 觀察 heap 的最前面元素
print("目前最小值 h[0] =", h[0])

# 使用 heappop() 取出目前最小值
# 取出後，heap 會自動重新整理，保持最小堆積特性
m = heapq.heappop(h)

# 印出被取出的最小值
print("heappop 取出的最小值 =", m)

# 印出取出後剩下的 heap
print("取出後的 h =", h)

# 再多示範幾次，觀察每次都會拿到目前最小值
print("再取一次最小值 =", heapq.heappop(h))
print("再取一次最小值 =", heapq.heappop(h))
print("最後剩下的 h =", h)
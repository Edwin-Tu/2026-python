# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）

# 從 collections 模組匯入 deque
# deque 是雙向佇列，可以快速從前後加入或移除資料
from collections import deque

# 建立一個最大長度為 3 的 deque
# 代表這個佇列最多只能保留 3 筆資料
q = deque(maxlen=3)

# 依序加入資料
for i in [1, 2, 3, 4, 5]:
    q.append(i)
    
    # 每加入一次就印出目前內容
    print(f"加入 {i} 之後，q = {list(q)}")

# 最後印出結果
print("最後保留的資料：", list(q))
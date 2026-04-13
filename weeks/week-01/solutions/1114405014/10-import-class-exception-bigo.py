# 10 模組、類別、例外與 Big-O（最低門檻）範例
# 本範例展示 Python 中 deque 資料結構、類別定義、例外處理機制，以及時間複雜度的基本概念

# 從 collections 模組匯入 deque（雙端佇列）
# deque 是一種高效能的雙端佇列，適合用於需要快速在兩端新增或移除元素的場景
from collections import deque

# 建立一個有長度限制的 deque，maxlen=2 表示最多只能容納 2 個元素
q = deque(maxlen=2)

# 依序新增三個元素到 deque 中
q.append(1)
q.append(2)
# 當 deque 已滿（已有 2 個元素）時再新增元素
# 會自動移除最舊的元素（最先加入的元素），保持固定長度
q.append(3)  # 自動丟掉最舊

# 此時 q 的內容為 [2, 3]，數字 1 已自動被移除


# 類別（Class）定義
# 類別是建立物件（Object）的藍圖，封裝了資料與行為
class User:
    # __init__ 是建構函式，當建立新物件時會自動呼叫
    # self 是物件本身的參考，user_id 是傳入的參數
    def __init__(self, user_id):
        # 將 user_id 儲存為物件的屬性（attribute）
        self.user_id = user_id


# 建立 User 類別的實例（Instance），並傳入 user_id=42
u = User(42)

# 透過物件存取其屬性
uid = u.user_id


# 例外處理（Exception Handling）
# 用於處理可能發生錯誤的程式碼，避免程式因異常而直接終止

def is_int(val):
    """
    判斷傳入的值是否可以轉換為整數
    使用 try-except 區塊捕捉可能的轉換錯誤
    """
    try:
        # 嘗試將 val 轉換為整數
        # 如果成功（val 可以轉換），回傳 True
        int(val)
        return True
    except ValueError:
        # 如果失敗（ValueError 例外），表示 val 無法轉換為整數，回傳 False
        return False


# Big-O 只是觀念提示
# Big-O 記號用於描述演算法的時間或空間複雜度隨輸入規模成長的趨勢

# list.append 通常是 O(1)
# 平均情況下，在清單末端新增元素是常數時間操作，與清單大小無關

# list 切片是 O(N)
# 複製清單的切片需要遍歷被複製的元素，時間與切片長度成正比

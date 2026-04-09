# U06. 時區操作最佳實踐：UTC 優先（3.16）
# 為什麼？本地時間有夏令時跳躍問題，內部計算應一律用 UTC

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# 建立時區物件
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")

# 問題：直接在本地時間加减，夏令時邊界會出錯
# 美國 2013-03-10 凌晨 2:00 時鐘往前撥一小時（夏令時開始）
# 當天時間序列：1:00 → 1:30 → 2:00（跳過，直接到3:00）
# 這稱為「夏令時跳躍」（DST Gap）
local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)
# 直接在本地時間加上 30 分鐘，會產生錯誤結果
wrong = local_dt + timedelta(minutes=30)
print(f"錯誤結果：{wrong}")  # 2:15（不存在的時間！）

# 正確做法：先轉 UTC 計算，再轉回本地
# 步驟：
# 1. 將本地時間轉換為 UTC（此時會自動處理夏令時偏移）
# 2. 在 UTC 進行時間加减（無夏令時問題）
# 3. 將結果轉回本地時區
utc_dt = local_dt.astimezone(utc)  # 2013-03-10 07:45:00+00:00
correct = utc_dt + timedelta(minutes=30)  # UTC: 2013-03-10 08:15:00+00:00
print(f"正確結果：{correct.astimezone(central)}")  # 3:15（跳過了 2:xx）

# 最佳實踐：輸入→UTC→計算→輸出時轉本地
# 流程：
# 1. 接收使用者輸入（通常是本地時間）
# 2. 轉為 UTC 儲存（統一內部表示）
# 3. 進行任何時間計算（UTC）
# 4. 輸出時轉為目標時區
user_input = "2012-12-21 09:30:00"
naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
# 加上本地時區資訊，然後轉為 UTC 儲存
aware = naive.replace(tzinfo=central).astimezone(utc)
print(f"存 UTC：{aware}")
# 輸出時轉為台北時區顯示
print(f"顯示台北：{aware.astimezone(ZoneInfo('Asia/Taipei'))}")
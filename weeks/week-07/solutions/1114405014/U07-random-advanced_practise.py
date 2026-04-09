# U07. 隨機種子與安全亂數（3.11）
# random 模組為偽隨機，相同種子產生相同序列；密碼學請用 secrets

import random
import secrets

# 相同種子 → 相同序列（可重現）
# 說明：random 模組是「偽隨機」數產生器（Pseudo-Random Number Generator, PRNG）
# 透過演算法產生，看似隨機但實際上是確定的
# 相同种子（seed）會產生相同的隨機序列
# 用途：除錯、測試、模擬需要可重現結果的場景
random.seed(42)
seq1 = [random.randint(1, 100) for _ in range(5)]
random.seed(42)
seq2 = [random.randint(1, 100) for _ in range(5)]
print(seq1 == seq2)  # True（兩個序列完全相同）

# 不同 Random 實例各自獨立
# 說明：可以建立多個獨立的 Random 實例
# 每個實例有自己的內部狀態，互不影響
rng1 = random.Random(1)
rng2 = random.Random(2)
print(rng1.random(), rng2.random())  # 各自的隨機流

# 密碼學安全亂數（不可預測，不能設种子）
# 說明：random 模組不是密碼學安全的
# 攻擊者可能透過觀察输出一段序列，推測後續輸出（不安全！）
# 密碼學應使用 secrets 模組（Python 3.6+）
# 特性：
# - 使用作業系統的 CSPRNG（Cryptographically Secure PRNG）
# - 不可預測（無法透過過去輸出推測未來）
# - 無法設定种子（每次呼叫都是真正隨機）
print(secrets.randbelow(100))  # 密碼學安全整數（0-99）
print(secrets.token_hex(16))  # 密碼學安全 hex 字串（16 bytes = 32 hex digits）
print(secrets.token_bytes(16))  # 密碼學安全 bytes（16 bytes）

# 重要：random 模組不適合密碼、token、session key 等安全場景
# 只適合遊戲、模擬、測試等非安全用途
# 常見錯誤：
# - 使用 random.randint() 產生密碼（危險！）
# - 使用 random.random() 產生 session token（危險！）
# 正確做法：使用 secrets 模組產生任何安全相關的隨機數
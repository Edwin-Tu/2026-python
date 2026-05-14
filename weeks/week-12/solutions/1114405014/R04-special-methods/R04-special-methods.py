# R04. 特殊方法（8.2–8.3）
# 主題：__eq__ / __lt__ / __len__ / __contains__ / __iter__
# 特殊方法（也稱魔術方法）前後各有两个底線，讓自訂類別可以像內建型別一樣操作

# total_ordering 裝飾器可以自動補齊缺少的比較方法
# 只要定義 __eq__ 和任一個排序方法（如 __lt__），其餘（__le__, __gt__, __ge__）自動推導
from functools import total_ordering

# ── @total_ordering：只需定義 __eq__ 和一個比較方法 ──────────────────
@total_ordering
class Score:
    def __init__(self, name, value):
        # name 是學生姓名，value 是考試分數
        self.name = name
        self.value = value

    def __repr__(self):
        # 回傳開發者可讀的表示式
        return f"Score({self.name!r}, {self.value})"

    def __eq__(self, other):
        # 定義「相等」的邏輯：分數相同就視為相等
        # 如果 other 不是 Score 型別，回傳 NotImplemented
        # 讓 Python 去嘗試 other 的 __eq__ 或拋出適當的錯誤
        if not isinstance(other, Score):
            return NotImplemented
        # 比較兩個 Score 的 value（分數）是否相等
        return self.value == other.value

    def __lt__(self, other):
        # 定義「小於」的邏輯：分數較低就視為較小
        if not isinstance(other, Score):
            return NotImplemented
        # 比較兩個 Score 的 value（分數）
        return self.value < other.value

    # @total_ordering 會自動補上：
    # __le__（<=）、__gt__（>）、__ge__（>=）


# 建立三個 Score 實例，分數分別為 90, 75, 90
s1 = Score("Alice", 90)
s2 = Score("Bob", 75)
s3 = Score("Carol", 90)

# > 由 @total_ordering 根據 __lt__ 自動推導（a > b 等同於 b < a）
print(s1 > s2)      # True（90 > 75）
# == 使用自訂的 __eq__，只看 value 是否相等
print(s1 == s3)     # True（Alice 和 Carol 都是 90 分）
# != 由 __eq__ 自動推導（not a == b）
print(s1 != s2)     # True
# sorted() 會使用 __lt__ 來排序
print(sorted([s1, s2, s3]))     # 升冪排列

# ── __len__ / __contains__ / __iter__ ─────────────────────────────────
# 實作這些方法可以讓自訂類別使用 len()、in 運算子、for 迴圈
class Classroom:
    def __init__(self, name):
        # 班級名稱
        self.name = name
        # 內部使用 list 儲存學生名單（保護屬性）
        self._students = []

    def add(self, student):
        # add() 是一般方法，用來加入學生
        self._students.append(student)

    def __len__(self):
        # 讓 len(obj) 可以回傳學生人數
        # 內部委託給 list 的 __len__
        return len(self._students)

    def __contains__(self, student):
        # 讓 "Alice" in obj 可以檢查學生是否存在
        # 內部委託給 list 的 in 運算子
        return student in self._students

    def __iter__(self):
        # 讓 for student in obj 可以迭代學生
        # 回傳 list 的迭代器，Python 會自動處理迭代細節
        return iter(self._students)

    def __repr__(self):
        # 顯示班級名稱和人數，人數透過 __len__ 取得
        return f"Classroom({self.name!r}, {len(self)} 人)"


# 建立一個班級實例，名稱為「資工一甲」
cls = Classroom("資工一甲")
# 加入三位學生
cls.add("Alice")
cls.add("Bob")
cls.add("Carol")

# __len__ 讓 len() 可以作用在自訂物件上
print(len(cls))             # 3
# __contains__ 讓 in 運算子可以作用
print("Alice" in cls)       # True（Alice 有在名單中）
print("Dave" in cls)        # False（Dave 不在名單中）

# __iter__ 讓 for 迴圈可以遍歷班級中的所有學生
for student in cls:
    print(student)

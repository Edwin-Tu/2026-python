# R01. 類別基礎（8.1）
# 主題：__init__ 建構方法、實例方法、__repr__ 與 __str__ 的差異
# 以及類別變數（class variable）與實例變數（instance variable）的區別

# ── 第一部分：最簡單的 class ────────────────────────────────────────
# class 關鍵字用來定義一個類別，類別是物件的藍圖
class Point:
    # __init__ 是建構子（constructor），在建立實例時自動呼叫
    # self 代表「這個實例本身」，是第一個參數，名稱可自訂但慣例用 self
    def __init__(self, x, y):
        # 將參數 x, y 儲存為實例變數，每個 Point 物件都有自己的 x, y
        self.x = x
        self.y = y

    # __repr__：給開發者看的正式表示式
    # 目標是回傳一個字串，讓 eval() 可以重建此物件（理想情況）
    # 當在直譯環境直接輸入變數名稱時，會呼叫 __repr__
    def __repr__(self):
        # 使用 f-string 格式化，回傳像 Point(3, 4) 這樣的字串
        return f"Point({self.x}, {self.y})"

    # __str__：給使用者看的非正式表示式
    # print() 函數或 str() 轉換時會呼叫 __str__
    # 如果沒有定義 __str__，Python 會 fallback 使用 __repr__
    def __str__(self):
        # 回傳更簡潔、更人性化的格式
        return f"({self.x}, {self.y})"

    # 自訂的實例方法，計算目前點到另一點的歐幾里得距離
    # distance_to 接收另一個 Point 物件作為參數
    def distance_to(self, other):
        # 計算兩點間的直線距離：sqrt((x1-x2)^2 + (y1-y2)^2)
        # ** 0.5 相當於開根號，也可以使用 math.sqrt()
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


# 建立 Point 類別的兩個實例，分別代表原點和 (3,4)
p1 = Point(0, 0)
p2 = Point(3, 4)

# repr() 會呼叫 __repr__，輸出為 Point(0, 0)
print(repr(p1))             # Point(0, 0)
# str() 會呼叫 __str__，輸出為 (3, 4)
print(str(p2))              # (3, 4)
# 呼叫自訂方法 distance_to，計算 p1 到 p2 的距離
print(p1.distance_to(p2))  # 5.0

# ── 第二部分：類別變數 vs 實例變數 ──────────────────────────────────
# school 是類別變數，定義在 __init__ 外面
# 類別變數被所有實例共享，修改一次所有實例都受影響
class Student:
    # 類別變數：所有 Student 實例共用同一個 school 屬性
    # 類似 Java 中的 static 變數
    school = "國立澎湖科技大學"    # 類別變數

    def __init__(self, name, student_id):
        # 實例變數：每個 Student 實例各自獨立擁有
        # name 和 student_id 是每個學生的個別資料
        self.name = name            # 實例變數
        self.student_id = student_id

    def __repr__(self):
        # 回傳開發者導向的字串，顯示學號和姓名
        return f"Student({self.student_id}, {self.name})"

    # greeting 方法展示了如何同時使用類別變數和實例變數
    def greeting(self):
        # self.school 會先找實例變數，找不到才找類別變數
        return f"我是 {self.school} 的 {self.name}"


# 建立兩個 Student 實例，各自的 name 和 student_id 不同
s1 = Student("王小明", "11144050001")
s2 = Student("李小華", "11144050002")

# 呼叫實例方法 greeting()
# self.school 透過 MRO（Method Resolution Order）找到類別變數
print(s1.greeting())
# 透過實例存取類別變數 school
print(s2.school)            # 輸出：國立澎湖科技大學
# 直接透過類別名稱存取類別變數
print(Student.school)       # 輸出：國立澎湖科技大學

# 修改類別變數會影響所有實例（因為實例本身沒有同名的實例變數遮蔽）
Student.school = "NPU"
# 即使 s1, s2 已經建立，school 的值仍然跟著類別改變
print(s1.school)            # NPU
print(s2.school)            # NPU

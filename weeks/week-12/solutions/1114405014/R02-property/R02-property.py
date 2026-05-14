# R02. 屬性封裝（8.6）
# 主題：@property / getter / setter / 唯讀屬性
# property 裝飾器讓方法可以像屬性一樣存取，同時保留驗證邏輯
# 這是 Python 實現封裝（encapsulation）的主要方式

# ── 基本 @property ────────────────────────────────────────────────────
# 定義一個 Circle 類別，示範如何使用 property 控制屬性存取
class Circle:
    def __init__(self, radius):
        # _radius 使用底線開頭，是 Python 慣例表示「內部使用，請勿直接存取」
        # 這是一種保護性約定（protected），不是語法強制
        self._radius = radius   # 私有變數，慣例以底線開頭

    # @property 裝飾器將方法 radius() 變成唯讀屬性
    # 外界可以透過 c.radius 讀取，就像存取一般屬性一樣
    @property
    def radius(self):
        # 回傳內部儲存的 _radius 值
        # 可以在這裡加入日誌、權限檢查等邏輯
        return self._radius

    # @radius.setter 裝飾器定義屬性的設定方法
    # 當執行 c.radius = value 時會自動呼叫此方法
    @radius.setter
    def radius(self, value):
        # 在 setter 中可以加入驗證邏輯
        if value < 0:
            # 如果半徑為負數，主動拋出 ValueError 異常
            raise ValueError("半徑不能為負數")
        # 通過驗證後才真正更新內部變數
        self._radius = value

    # 沒有定義 setter 的 property 就是「唯讀屬性」
    # area 是根據半徑即時計算出來的，不需要儲存
    @property
    def area(self):
        # 唯讀屬性（沒有 setter），無法從外部賦值
        import math
        # 圓面積公式：π × r²
        return math.pi * self._radius ** 2

    # 另一個唯讀屬性：直徑 = 半徑 × 2
    @property
    def diameter(self):
        return self._radius * 2


# 建立半徑為 5 的 Circle 物件
c = Circle(5)

# 透過 property 讀取半徑，表面上是存取屬性，實際上是呼叫方法
print(c.radius)     # 5
# area 和 diameter 都是唯讀屬性，根據半徑即時計算
print(c.area)       # 78.53981633974483
print(c.diameter)   # 10

# 透過 setter 修改半徑，會觸發驗證邏輯
c.radius = 10       # 內部呼叫 radius.setter(10)
# area 會自動重新計算，因為每次取值都重新計算
print(c.area)       # 314.1592653589793

# 嘗試設定半徑為負數，驗證邏輯會拋出異常
try:
    c.radius = -1   # 觸發 ValueError
except ValueError as e:
    print(e)        # 輸出：半徑不能為負數

# 嘗試對唯讀屬性賦值，會拋出 AttributeError
try:
    c.area = 100    # 唯讀屬性不能設定
except AttributeError as e:
    # Python 會說：can't set attribute
    print(e)

# ── 用 property 做延遲計算 ────────────────────────────────────────────
# Rectangle 類別展示 property 的另一個常見用法
# 不需要預先計算，而是在取值時才動態算出結果
class Rectangle:
    def __init__(self, width, height):
        # width 和 height 是公開屬性，直接存取
        self.width = width
        self.height = height

    # area 是 property，每次取值都重新計算
    @property
    def area(self):
        # 矩形面積公式：寬 × 高
        return self.width * self.height

    # perimeter 也是 property
    @property
    def perimeter(self):
        # 矩形周長公式：2 × (寬 + 高)
        return 2 * (self.width + self.height)


r = Rectangle(4, 6)
print(r.area)       # 24
print(r.perimeter)  # 20

# 修改 width 之後，area 和 perimeter 會自動更新
# 因為它們沒有儲存值，而是每次重新計算
r.width = 8
print(r.area)       # 48（自動反映新的寬度）

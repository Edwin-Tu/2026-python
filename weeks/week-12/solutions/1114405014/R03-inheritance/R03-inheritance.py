# R03. 繼承與 super()（8.7）
# 主題：繼承（Inheritance） / 方法覆寫（Override） / super() /
#       isinstance / issubclass / 多型（Polymorphism）
# 繼承是物件導向三大特性之一，讓子類別可以重複使用父類別的程式碼

# ── 基底類別（Base Class / Parent Class）────────────────────────────
# Animal 是所有動物的抽象基底類別
class Animal:
    # 建構子：接受動物名稱作為參數
    def __init__(self, name):
        # 將名稱儲存為實例變數，供子類別繼承使用
        self.name = name

    # speak 是通用方法，子類別可以覆寫（override）來改變行為
    def speak(self):
        # 這是預設實作，如果子類別沒有覆寫就會使用這個版本
        return f"{self.name} 發出聲音"

    # __repr__ 使用 self.__class__.__name__ 動態取得類別名稱
    # 這樣即使被子類別繼承，也能正確顯示子類別的名稱
    def __repr__(self):
        # !r 表示使用 repr() 來格式化 name，會加上引號
        return f"{self.__class__.__name__}({self.name!r})"


# ── 子類別（Subclass / Child Class）：覆寫方法 ──────────────────────
# Dog 繼承 Animal，在類別名稱後用括號指定父類別
class Dog(Animal):
    # 覆寫 speak() 方法，提供狗專屬的叫聲
    # 當 Dog 實例呼叫 speak() 時，會執行這個版本而非父類別的版本
    def speak(self):
        # 完全取代父類別的實作
        return f"{self.name} 說：汪汪！"


# Cat 也繼承 Animal，覆寫 speak() 為貓叫聲
class Cat(Animal):
    def speak(self):
        return f"{self.name} 說：喵～"


# ── super()：呼叫父類別方法 ───────────────────────────────────────────
# GuideDog 繼承 Dog，展示如何使用 super() 呼叫父類別的方法
class GuideDog(Dog):
    # 覆寫建構子，新增 owner 屬性
    def __init__(self, name, owner):
        # super() 回傳一個臨時物件，讓你可以呼叫父類別的方法
        # super().__init__(name) 會沿著 MRO 向上呼叫 Dog → Animal 的 __init__
        # 這樣就不需要在子類別中重複 name 的賦值邏輯
        super().__init__(name)      # 呼叫父類別的建構子
        # 子類別特有的屬性
        self.owner = owner

    # 覆寫 speak() 方法，同時利用父類別的實作
    def speak(self):
        # super().speak() 呼叫 Dog 類別的 speak() 方法
        # 這樣可以在父類別邏輯的基礎上擴充，而不是全部重寫
        base = super().speak()      # 呼叫 Dog.speak()
        # 在父類別的回傳值後面加上導盲犬專屬資訊
        return f"{base}（導盲犬，主人：{self.owner}）"


# 建立各種動物的實例
d = Dog("小黑")         # Dog 實例
c = Cat("咪咪")         # Cat 實例
g = GuideDog("阿金", "王伯伯")  # GuideDog 實例，需要 name 和 owner

# 多型（Polymorphism）：相同的方法呼叫，不同的執行結果
# 雖然都是 .speak()，但根據物件的實際類別執行不同的版本
for animal in [d, c, g]:
    print(animal.speak())

# ── isinstance / issubclass ───────────────────────────────────────────
# isinstance(object, class) 檢查物件是否為某個類別（或其子類別）的實例
print(isinstance(d, Dog))       # True：d 是 Dog 的實例
print(isinstance(d, Animal))    # True：Dog 是 Animal 的子類別，所以 d 也是 Animal 的實例
print(isinstance(d, Cat))       # False：d 不是 Cat 的實例

# issubclass(class, class) 檢查某個類別是否為另一個類別的子類別
print(issubclass(Dog, Animal))  # True：Dog 繼承了 Animal
print(issubclass(Cat, Dog))     # False：Cat 沒有繼承 Dog

# ── 多型（Polymorphism）────────────────────────────────────────────────
# 多型的意思是「相同介面，不同實作」
# make_sounds 函數接受任何具有 speak() 方法的物件
# 不需要檢查型別，Python 的 duck typing 會自動處理
def make_sounds(animals: list):
    # 型別提示 list 只是輔助說明，Python 不會強制檢查
    for a in animals:
        # 只要 a 有 speak() 方法就可以呼叫
        # 這就是「鴨子型別」：如果它走起來像鴨子、叫起來像鴨子，那它就是鴨子
        print(a.speak())        # 各自呼叫自己的 speak()

# 傳入不同型別的動物 list，每個動物各自執行自己的 speak()
make_sounds([d, c, g])

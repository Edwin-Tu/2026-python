# 迭代器基礎概念

# 1. 迭代器協議的核心方法
items = [1, 2, 3]

# iter() 會呼叫物件的 __iter__()，取得一個迭代器
it = iter(items)
print(f"迭代器: {it}")

# next() 會呼叫迭代器的 __next__()，依序取出元素
print(f"第一個: {next(it)}")  # 1
print(f"第二個: {next(it)}")  # 2
print(f"第三個: {next(it)}")  # 3

# 當沒有更多元素時，會拋出 StopIteration
try:
    next(it)
except StopIteration:
    print("迭代結束!")

# 2. 常見可迭代物件
print("\n--- 常見可迭代物件 ---")

# 列表可以被 iter() 轉成迭代器
print(f"列表 iter: {iter([1, 2, 3])}")

# 字串也可以逐字元迭代
print(f"字串 iter: {iter('abc')}")

# 字典預設迭代的是 key
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

# 檔案物件也屬於可迭代物件，可逐行讀取
import io

f = io.StringIO("line1\nline2\nline3")
print(f"檔案 iter: {iter(f)}")


# 3. 自訂可迭代物件
class CountDown:
    def __init__(self, start):
        self.start = start

    # __iter__() 回傳一個真正負責逐步產生資料的迭代器物件
    def __iter__(self):
        return CountDownIterator(self.start)


class CountDownIterator:
    def __init__(self, start):
        self.current = start

    # __next__() 每次被呼叫時回傳下一個值
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


print("\n--- 自訂迭代器 ---")
for i in CountDown(3):
    print(i, end=" ")  # 3 2 1

# 4. 迭代器 vs 可迭代物件
print("\n\n--- 迭代器 vs 可迭代物件 ---")

# 列表本身是可迭代物件，但不是迭代器
my_list = [1, 2, 3]
print("列表: 可迭代物件 ✓, 迭代器 ✗")

# 對列表呼叫 iter() 後，才會得到真正的迭代器
my_iter = iter(my_list)
print("iter(列表): 可迭代物件 ✗, 迭代器 ✓")

# 迭代器本身通常同時具備 __iter__() 與 __next__()
print("迭代器: 可迭代物件 ✓ (有__iter__), 迭代器 ✓ (有__next__)")

# 5. StopIteration 例外
print("\n--- StopIteration 用法 ---")


# 手動遍歷：使用 try / except 捕捉 StopIteration
def manual_iter(items):
    it = iter(items)
    while True:
        try:
            item = next(it)
            print(f"取得: {item}")
        except StopIteration:
            break


manual_iter(["a", "b", "c"])


# 使用 next(it, 預設值) 避免直接拋出例外
def manual_iter_default(items):
    it = iter(items)
    while True:
        item = next(it, None)  # 若取不到值，回傳 None
        if item is None:
            break
        print(f"取得: {item}")


print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
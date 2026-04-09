items = [1, 2, 3]

it = iter(items)
print(f"迭代器: {it}")

print(f"第一個: {next(it)}")
print(f"第二個: {next(it)}")
print(f"第三個: {next(it)}")

try:
    next(it)
except StopIteration:
    print("迭代結束!")

print("\n--- 常見可迭代物件 ---")

print(f"列表 iter: {iter([1, 2, 3])}")
print(f"字串 iter: {iter('abc')}")
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

import io

f = io.StringIO("line1\nline2\nline3")
print(f"檔案 iter: {iter(f)}")


class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return CountDownIterator(self.start)


class CountDownIterator:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


print("\n--- 自訂迭代器 ---")
for i in CountDown(3):
    print(i, end=" ")

print("\n\n--- 迭代器 vs 可迭代物件 ---")

my_list = [1, 2, 3]
print("列表: 可迭代物件 ✓, 迭代器 ✗")

my_iter = iter(my_list)
print("iter(列表): 可迭代物件 ✗, 迭代器 ✓")

print("迭代器: 可迭代物件 ✓ (有__iter__), 迭代器 ✓ (有__next__)")

print("\n--- StopIteration 用法 ---")


def manual_iter(items):
    it = iter(items)
    while True:
        try:
            item = next(it)
            print(f"取得: {item}")
        except StopIteration:
            break


manual_iter(["a", "b", "c"])


def manual_iter_default(items):
    it = iter(items)
    while True:
        item = next(it, None)
        if item is None:
            break
        print(f"取得: {item}")


print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
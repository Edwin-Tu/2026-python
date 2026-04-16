# Understand（理解）- 生成器概念
# 生成器是一種特殊的迭代器，可以使用yield關鍵字來產生值，而不是一次性返回所有值。
# 生成器函數使用yield來暫停執行，並在下次呼叫時從上次位置繼續。

def frange(start, stop, step):  # 自訂浮點數範圍生成器函數
    x = start  # 初始化起始值
    while x < stop:  # 當x小於stop時繼續
        yield x  # 產生當前值並暫停
        x += step  # 增加步長

result = list(frange(0, 2, 0.5))  # 將生成器轉為列表
print(f"frange(0, 2, 0.5): {result}")  # 印出結果

def countdown(n):  # 倒數生成器函數
    print(f"Starting countdown from {n}")  # 印出開始訊息
    while n > 0:  # 當n大於0時繼續
        yield n  # 產生當前n值
        n -= 1  # 減少n
    print("Done!")  # 當完成時印出訊息

print("\n--- 建立生成器 ---")  # 印出分隔線
c = countdown(3)  # 創建生成器物件
print(f"生成器物件: {c}")  # 印出生成器物件

print("\n--- 逐步迭代 ---")  # 印出分隔線
print(f"next(c): {next(c)}")  # 呼叫next取得第一個值
print(f"next(c): {next(c)}")  # 第二個值
print(f"next(c): {next(c)}")  # 第三個值

try:
    next(c)  # 嘗試取得第四個值
except StopIteration:
    print("StopIteration!")  # 當生成器結束時印出

def fibonacci():  # 費波那契數列生成器
    a, b = 0, 1  # 初始化前兩個數
    while True:  # 無限迴圈
        yield a  # 產生當前a值
        a, b = b, a + b  # 更新a和b

print("\n--- Fibonacci 生成器 ---")  # 印出分隔線
fib = fibonacci()  # 創建費波那契生成器
for i in range(10):  # 迴圈10次
    print(next(fib), end=" ")  # 印出下一個費波那契數
print()  # 換行

def chain_iter(*iterables):  # 串聯多個可迭代物件的生成器
    for it in iterables:  # 遍歷每個可迭代物件
        yield from it  # 從每個物件中產生元素

print("\n--- yield from 用法 ---")  # 印出分隔線
result = list(chain_iter([1, 2], [3, 4], [5, 6]))  # 串聯三個列表
print(f"chain_iter: {result}")  # 印出結果

class Node:  # 樹節點類別
    def __init__(self, value):
        self.value = value  # 節點值
        self.children = []  # 子節點列表

    def add_child(self, node):
        self.children.append(node)  # 添加子節點

    def __iter__(self):
        return iter(self.children)  # 返回子節點的迭代器

    def depth_first(self):  # 深度優先遍歷生成器
        yield self  # 產生當前節點
        for child in self:  # 遍歷子節點
            yield from child.depth_first()  # 遞歸產生子樹

print("\n--- 樹的深度優先遍歷 ---")  # 印出分隔線
root = Node(0)  # 創建根節點
root.add_child(Node(1))  # 添加子節點1
root.add_child(Node(2))  # 添加子節點2
root.children[0].add_child(Node(3))  # 為節點1添加子節點3
root.children[0].add_child(Node(4))  # 為節點1添加子節點4

for node in root.depth_first():  # 遍歷樹
    print(node.value, end=" ")  # 印出節點值
print()  # 換行

def flatten(items):  # 攤平巢狀序列的生成器
    for x in items:  # 遍歷每個元素
        if hasattr(x, "__iter__") and not isinstance(x, str):  # 如果是可迭代且不是字串
            yield from flatten(x)  # 遞歸攤平
        else:
            yield x  # 產生元素

print("\n--- 巢狀序列攤平 ---")  # 印出分隔線
nested = [1, [2, [3, 4]], 5]  # 巢狀列表
print(f"展開: {list(flatten(nested))}")  # 印出攤平結果

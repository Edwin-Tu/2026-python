# Remember（記憶）- enumerate() 和 zip()
# enumerate() 函數用於將可迭代物件的元素與索引配對，返回一個枚舉物件。
# zip() 函數用於將多個可迭代物件的對應元素打包成元組。

colors = ["red", "green", "blue"]  # 定義一個顏色列表

print("--- enumerate() 基本用法 ---")  # 印出分隔線
for i, color in enumerate(colors):  # 使用enumerate遍歷列表，取得索引和值
    print(f"{i}: {color}")  # 印出索引和顏色

print("\n--- enumerate(start=1) ---")  # 印出分隔線
for i, color in enumerate(colors, 1):  # 指定起始索引為1
    print(f"第{i}個: {color}")  # 印出從1開始的索引和顏色

print("\n--- enumerate with 檔案 ---")  # 印出分隔線
lines = ["line1", "line2", "line3"]  # 模擬檔案行列表
for lineno, line in enumerate(lines, 1):  # 為每一行編號
    print(f"行 {lineno}: {line}")  # 印出行號和內容

print("\n--- zip() 基本用法 ---")  # 印出分隔線
names = ["Alice", "Bob", "Carol"]  # 姓名列表
scores = [90, 85, 92]  # 分數列表
for name, score in zip(names, scores):  # 將姓名和分數配對
    print(f"{name}: {score}")  # 印出姓名和分數

print("\n--- zip() 多個序列 ---")  # 印出分隔線
a = [1, 2, 3]  # 第一個列表
b = [10, 20, 30]  # 第二個列表
c = [100, 200, 300]  # 第三個列表
for x, y, z in zip(a, b, c):  # 將三個列表的對應元素配對
    print(f"{x} + {y} + {z} = {x + y + z}")  # 計算和印出總和

print("\n--- zip() 長度不同 ---")  # 印出分隔線
x = [1, 2]  # 短列表
y = ["a", "b", "c"]  # 長列表
print(f"list(zip(x, y)): {list(zip(x, y))}")  # zip會以最短序列為準

from itertools import zip_longest  # 匯入zip_longest用於處理不同長度
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")  # 使用fillvalue填充較短序列

print("\n--- 建立字典 ---")  # 印出分隔線
keys = ["name", "age", "city"]  # 鍵列表
values = ["John", "30", "NYC"]  # 值列表
d = dict(zip(keys, values))  # 使用zip建立字典
print(f"dict: {d}")  # 印出字典

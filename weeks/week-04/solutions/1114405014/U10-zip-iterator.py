# U10. zip 為何只能用一次（1.8）

# 建立一個字典
# key 是商品名稱，value 是價格
prices = {'A': 2.0, 'B': 1.0}

# 使用 zip 將 values 和 keys 配對
# 這裡產生的是一個「迭代器」，不是完整 list
z = zip(prices.values(), prices.keys())

# 先印出 z 的型態
print("z 的型態：", type(z))

# 第一次使用 min(z)
# 這時會把 z 裡的資料逐個取出來比較
# 一旦取完，z 裡面的內容就被「消耗掉」了
result1 = min(z)

# 印出第一次結果
print("第一次 min(z) 的結果：", result1)

# 再次把 z 轉成 list，觀察內容
# 會發現已經沒有資料了，因為剛剛已經被 min() 用完
print("min(z) 之後，z 剩下的內容：", list(z))


# ----------------------------
# 正確示範：如果要重複使用，應該重新建立 zip
# ----------------------------

# 重新建立一個新的 zip 物件
z = zip(prices.values(), prices.keys())

# 先用 min()
print("重新建立後，min(z) =", min(z))

# 再重新建立一次，才能用 max()
z = zip(prices.values(), prices.keys())
print("重新建立後，max(z) =", max(z))


# ----------------------------
# 另一種做法：先轉成 list，就能重複使用
# ----------------------------

# 把 zip 結果先存成 list
z_list = list(zip(prices.values(), prices.keys()))

# 印出 z_list
print("z_list =", z_list)

# 現在就可以重複使用
print("min(z_list) =", min(z_list))
print("max(z_list) =", max(z_list))
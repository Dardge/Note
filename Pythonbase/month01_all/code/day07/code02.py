"""
    集合 固定集合
"""

# 创建空
set01 = set()

# 创建有默认值集合
set01 = {1, 2, 3}

# 列表  转换为 集合
set01 = set([1, 2, 3, 2, 3, 5])
# 集合  转换为 列表
list01 = list(set01)
print(list01)

# 添加元素
set01.add("a")
set01.add("b")
set01.add("a")
print(set01)

# 删除元素
set01.remove("a")
# 如果要删除的数据不存在，则错误。
if "c" in set01:
    set01.remove("c")

# 如果丢弃不存在的数据，也不会错误。
set01.discard("c")  # 丢弃

# 获取全部元素
for item in set01:
    print(item, "**********")

# 计算
s01 = {1, 2, 3}
s02 = {2, 3, 4}
# 交集
print(s01 & s02)  # 2  3
# 并集 (合并  去重复)
print(s01 | s02)  # {1, 2, 3, 4}
# 补集（返回s01 有的但是s02没有的）
print(s01 - s02)  # {1}
print(s02 - s01)  # {4}
# 对称补集 s01 - s02   |   s02 - s01
print(s02 ^ s01)  # {1, 4}

# s01 是 s02的 超集
# s02 是 s01 的 子集
s01 = {1, 2, 3}
s02 = {2, 3}

print(s01 > s02)  # true
print(s01 < s02)  # false

# 集合推导式
numbers = [2, 4, 54, 656, 7, 8, 4]
result = {item for item in numbers if item < 100}
print(result)  # {8, 2, 4, 54, 7}

# 固定集合
frozen01 = frozenset(numbers)
print(frozen01)  # frozenset({2, 4, 7, 8, 656, 54})

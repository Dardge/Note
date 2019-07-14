"""

"""

list01 = ["a", "b", "c"]


# enumerate : 将列表中的每个元素 与 索引 组合为一个元组 16:28
# for item in enumerate(list01):
#     print(item[0],item[1])

def my_enumerate(list_target):
    index = 0
    for item in list_target:
        yield (index, item)
        index += 1

for item in my_enumerate(list01):
    print(item[0], item[1])

for index, item in my_enumerate(list01):
    print(index, item)

# 练习：my_zip
# zip：将多个可迭代对象的元素组合成一个个元组。  16:45
list02 = ["A", "B", "C"]
for item in zip(list01, list02):
    print(item)








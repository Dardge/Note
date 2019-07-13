"""
    字典
"""
# 创建空字典
d01 = {}
d01 = dict()

# 创建具有默认值的字典
d01 = {"zs":18,"ls":28}

# 添加元素
# 如果没有key则添加
d01["wz"] = 20
d01["qtx"] = 16
d01["dd"] = 20

# 删除
del d01["dd"]

# 修改
# 如果有key则修改
d01["qtx"] = 25

# 查找
print(d01["wz"])
# 如果查找没有的key，则错误
if "xx" in d01:
    print(d01["xx"])

# 遍历字典 获取的是key
for key in d01:
    print(key)

# 遍历字典记录(键值对)
for item in d01.items():
    # item 是元组
    print(item[0],item[1])

for value in d01.values():
    print(value)

print(d01)

d02 = {"a":"A"}
d03 = {"b":"B"}

# 字典不能相加
# print(d02 + d03)
# print(d02 * 2)

# 字典拼接
d04 = {**d02,**d03}
print(d04)


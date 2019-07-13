"""
    list  与  str
"""

# 拼接：1235
# 不建议每次使用字符串+进行拼接
result = ""
for item in range(1,4):
    # 每次拼接都会生成一个新的字符串对象
    result = result + str(item)
print(result)

# 建议字符串三次以上的拼接，使用下列代码
list01 = []
for item in range(1,4):
    # 向列表中添加元素
    list01.append(str(item))
print(list01)
# 列表 -->  str
result = "".join(list01)
print(result)
# 作业：画出内存图，进行对比。
# 字符串拆分
str01 = "a#b#c#d"
result = str01.split("#")
print(result)
















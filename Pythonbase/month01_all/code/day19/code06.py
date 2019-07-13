"""
    生成器表达式
"""

list01 = [2,3,4,5]

# list02 = []
# for item in list01:
#     list02.append(item ** 2)

# 列表推导式
list02 = [item ** 2 for item in list01] # 执行过后，内存中就存储了所有数据
for item in list02:
    print(item)

g03 = (item ** 2 for item in list01) # 执行过后，没有计算结果。
print(g03)
for item in g03: # 循环一次  计算一次  返回一次
    print(item)








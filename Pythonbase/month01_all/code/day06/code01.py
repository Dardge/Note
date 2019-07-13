"""
    列表推导式
    # 语法:
    # 变量 = [表达式 for 变量 in 可迭代对象]
    # 变量 = [表达式 for 变量 in 可迭代对象 if 条件]
"""

list01 = [2, 5, 7, 9, 4]
# 传统生成列表写法
list_result = []
for item in list01:
    list_result.append(item ** 2)
# 使用列表推导式生成列表
list_result = [item ** 2 for item in list01]

print(list_result)

# list_reuslt = []
# for item in list01:
#     if item % 2 == 0:
#         list_reuslt.append(item ** 2)
list_result = [item ** 2 for item in list01 if item % 2 == 0]

print(list_result)

















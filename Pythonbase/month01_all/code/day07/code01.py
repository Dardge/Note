"""
    字典推导式
"""
# 12345
# key：1  value:1**2
# key：2  value:2**2
# key：3  value:3**2

dic01 = {}
for item in range(1, 6):
    dic01[item] = item ** 2
# 字典推导式
# 语法：{键:值 for 变量 in 可迭代对象 if 条件}
#      {键:值 for 变量 in 可迭代对象}
dic02 = {item: item ** 2 for item in range(1, 6)}
print(dic01, dic02)



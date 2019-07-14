"""
    画出下列代码内存图：
"""

# 创建一个列表对象，赋值给变量list01
list01 = [1, 2]
# 将list01存储的列表对象地址，赋值给list02
list02 = list01
# 创建整数对象100，赋值给列表的第一个元素
list01[0] = 100
# 变量list02指向的列表的第一个元素
print(list02[0])  # ?100

list01 = [1, 2]
list02 = list01
# 创建新列表对象，赋值给变量list01
list01 = [100, 200]
print(list02[0])  # ?1

list01 = [1, 2]
# 通过切片将列表对象复制一份，赋值给变量list02
list02 = list01[:]
list01[0] = 100
print(list02[0],id(list01),id(list02))  # 1

list01 = [1, 2]
# 通过切片将列表对象复制一份，赋值给变量list02
list02 = list01.copy()  # 浅拷贝
list01[0] = 100
print(list02[0])

list01 = [1, [2, 3]]
# 通过切片将列表对象复制一份，赋值给变量list02
list02 = list01.copy()  # 浅拷贝
list01[1][0] = 100
print(list02[1][0])  # ?100

import copy

list01 = [1, [2, 3]]
# 通过切片将列表对象复制一份，赋值给变量list02
list02 = copy.deepcopy(list01)  # 浅拷贝
list01[1][0] = 100
print(list02[1][0])  # ?2

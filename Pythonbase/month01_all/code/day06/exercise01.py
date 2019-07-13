"""
    列表推导式练习
"""
# 练习1：使用列表推导式，生成1--10以内的奇数列表
# [1,3,5,7,9]

# list_result = []
# for item in range(1,11):
#     if item % 2 != 0:
#         list_result.append(item)
# print(list_result)

list_result = [item for item in range(1, 11) if item % 2 != 0]
print(list_result)

# list_result = []
# for item in range(1,11,2):
#         list_result.append(item)
# print(list_result)
list_result = [item for item in range(1, 11, 2)]
print(list_result)

# 练习2：[3,56,7,6,7,19,3] 获取列表中大于10的元素，组成新列表

list01 = [3, 56, 7, 6, 7, 19, 3]
list_result = [item for item in list01 if item > 10]
print(list_result)

# 练习3：在控制台中输入一个起始值，和一个终止值(不包含)。
#       将中间偶数存入一个列表，奇数存入一个列表
# 2     10
# 2  3  4  5  6  7  8  9
# 奇数列表3579
# 偶数列表2468
begin = int(input("请输入开始数："))
end = int(input("请输入结束数："))
list_temp = [item for item in range(begin, end)]
list01 = [item for item in list_temp if item % 2 != 0]
list02 = [item for item in list_temp if item % 2 == 0]
print(list01)
print(list02)

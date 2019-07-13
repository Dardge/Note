"""
    在控制台中依次获取两个变量，然后交换变量，输出结果。
"""

str_number01 = input("请输入第一个变量：")
str_number02 = input("请输入第二个变量：")
# 1.利用临时变量交换
# temp = str_number01
# str_number01 = str_number02
# str_number02 = temp
# 2.原地交换
str_number01, str_number02 = str_number02, str_number01
print("变量一是：" + str_number01)
print("变量二是：" + str_number02)
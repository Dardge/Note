"""
    在控制台中录入学生信息(姓名,年龄,性别,成绩。。。)
"""

str_name = input("输入姓名：")
str_age = input("请输入年龄：")
str_sex = input("请输入性别：")
str_score = input("请输入成绩：")
# 格式：xx的年龄是xx，性别是xx，成绩是xx。
result = str_name +"的年龄是" + str_age +"，性别是"+str_sex+"，成绩是"+str_score +"．"
print(result)



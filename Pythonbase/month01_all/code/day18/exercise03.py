"""
    练习：
    定义获取成绩的方法。
    要求：如果输入错误，重新录入。
         0  ---  100
"""


def get_score():
    while True:
        try:
            number = int(input("请输入成绩（1--100）："))
        except:
            print("输入有误")
            continue

        if 0 <= number <= 100:
            return number
        print("成绩不在范围内")


print(get_score())
# 练习：将学生管理系统UI层可能出错的逻辑，进行异常操作。
# 要求：哪里出错，解决哪里，然后按照既定流程向后执行。15:10

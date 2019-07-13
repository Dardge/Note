"""
    练习1：在控制台中录入学生信息（姓名，成绩，性别，年龄）
	步骤：1.创建类，定义4个数据成员
		  2. 在控制台中循环3次，录入学生成绩。
"""

class Student:
    def __init__(self,name = "",score = 0,sex=0,age=0):
        self.name = name
        self.score = score
        self.sex = sex
        self.age = age

    def print_self(self):
        print(self.name,self.score,self.sex,self.age)


list_stus = []
for i in range(3):
    stu = Student()
    stu.name = input("请输入姓名：")
    stu.score = int(input("请输入成绩："))
    stu.sex = input("请输入性别：")
    stu.age = int(input("请输入年龄："))
    list_stus.append(stu)

for item in list_stus:
    item.print_self()







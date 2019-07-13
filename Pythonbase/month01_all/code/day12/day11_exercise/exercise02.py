"""
作业：在控制台中录入狗的信息(姓名，年龄，性别)，按e键退出，最后将每个信息显示在控制台中。
"""


class Dog:
    def __init__(self, name="", age="", sex=""):
        self.name = name
        self.age = age
        self.sex = sex

    def print_self(self):
        print(self.name, self.age, self.sex)


list_dog = []
while True:
    obj = Dog()
    obj.name = input("请输入姓名：")
    obj.age = input("请输入年龄：")
    obj.sex = input("请输入性别：")
    list_dog.append(obj)
    if input("按e退出") == "e":
        break

for item in list_dog:
    item.print_self()

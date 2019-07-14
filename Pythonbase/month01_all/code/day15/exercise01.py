"""
定义宠物类，数据：姓名
定义狗类，数据：工作
定义猫类，行为：抓。
分别创建三个类对象，调用各自成员。
体会：继承的语法现象。
使用isinstance函数，测试各个对象的兼容性。
"""


class Pet:
    def __init__(self, name):
        self.name = name


class Dog(Pet):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job


class Cat(Pet):
    # 因为没有数据，所以不需要定义构造函数init
    def grab(self):
        print("抓")


p1 = Pet("米咻")
print(p1.name)

d1 = Dog("赵金多", "导盲")
print(d1.name)
print(d1.job)

c1 = Cat("喵喵")
c1.grab()
print(c1.name)

print(isinstance(p1, Pet))
print(isinstance(p1, Dog))
print(isinstance(d1, Dog))
print(isinstance(d1, Pet))
print(isinstance(c1, Dog))
print(isinstance(c1, Pet))

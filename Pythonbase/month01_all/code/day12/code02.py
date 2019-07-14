"""
    封装--私有化
    私有化实例变量：在变量名称前，加入双下划线。
            本质：修改了变量名称。
"""

# 练习：Student 类(姓名，年龄，成绩，性别) 15:00
class Wife01:
    # 类的设计者，限制该类对象只能有如下的实例变量
    __slots__ = ("__age","sex")

    def __init__(self, age,sex =""):
        # 属性 age
        self.age = age
        # 实例变量 sex
        self.sex = sex

    # @property 负责age属性的读取操作
    @property
    def age(self):
        return self.__age

    # @age.setter 负责age属性的写入操作
    @age.setter
    def age(self, value):
        if 20 <= value <= 30:
            self.__age = value
        else:
            raise ValueError("我不要")


w01 = Wife01(20)
w01.age = 21
print(w01.age)
# 获取对象实例变量
# print(w01.__dict__)
# dir(对象)  获取对象所有成员
print(dir(w01))
# w01.set_age(21)
# w01.get_age()

# w02 = Wife01(25)
# w02.agee = 10
# w02.money = 100 # 创建新成员变量
# print(w02.money)








"""
    继承--数据
    子类必须通过super()函数调用父类构造函数
"""


# 父类（基类 超类）
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    # 构造函数
    # 1. 类如果没有构造函数，解释器会自动添加一个。
    # 2. 如果类有构造函数，解释器不会自动添加。

    def __init__(self, name, score):
        # 调用父类构造函数
        # super() 表示 父类
        super().__init__(name)
        self.score = score


stu01 = Student("zs", 100)
print(stu01.name)
print(stu01.score)
per01 = Person("ls")


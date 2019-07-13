"""
    练习：对象计数器，统计Student类，总共创建了多少对象。
"""


class Student:
    # 类变量：所有对象共享的数据
    count = 0

    # 类方法：操作类变量
    @classmethod
    def get_count(cls):
        return cls.count

    def __init__(self):
        Student.count += 1


s01 = Student()
s01 = Student()
s01 = Student()
s01 = Student()
print(Student.get_count())

"""
    day11(JS) 复习
    1. 实例成员:对象的成员。例如：每个同学的杯子/牙刷。
    2. 类成员:表达所有对象的共享成员(各个支行，需要用总行的钱)。例如：饮水机/牙膏。
    3. 静态方法：表达不需要使用实例成员和类成员时，使用静态方法。
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 模长
    # 标准化/单位向量

    # 不需要使用对象成员，或者类成员时，使用静态方法。
    @staticmethod
    def get_right():
        # right = Vector(0, 1)
        # return right
        return 0,1

    @staticmethod
    def get_down():
        return Vector(1, 0)


import  random


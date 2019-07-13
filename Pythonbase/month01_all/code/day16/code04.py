"""
    自定义类的对象 使用运算符，本质就是调用内建方法。
"""

class Vector:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return "向量元素是：%d" % self.x

    # 正向运算符
    def __add__(self, other):
        # return self.x + other
        return Vector(self.x + other)

    def __radd__(self, other):
        super().__init__()
        return Vector(self.x + other)

    def __sub__(self, other):
        return Vector(self.x - other)

    def __mul__(self, other):
        return Vector(self.x * other)

    #累加
    def __iadd__(self, other):
        self.x += other
        return self

    def __lt__(self, other):
        return self.x  <  other

    def __gt__(self, other):
        return self.x > other

    #练习：等于  不等于

v06 = Vector(1)
re = v06 > 5
print(re)






v05 = Vector(1)
print(id(v05))
v05 += 2  # 内部：先调用__iadd__,如果么有，使用__add__.
print(id(v05))
print(v05)















# 练习：减法   乘法
v01 = Vector(1) + 2
v02 = 1 + Vector(1)
v03 = Vector(3) - 1
v04 = Vector(3) * 2
print(v01, v02, v03, v04)




"""
    总结：
    1. 内存图
"""
class MyClass:
    def __init__(self,a = 0,b = 0):
        self.a = a
        self.b = b

    def print_self(self):
        print(self.a,self.b)

c01 = MyClass(1,2)
c02 = MyClass()

# 方法只有一份   对象每次创建都有一份
# 问题：方法如何确定对象的数据？
# 答案：通过对象地址调用方法，会自动传递对象地址。
c01.print_self()
c02.print_self()

"""
  2. 实例变量/实例方法
     类变量/类方法
     
"""


class MyClass02:
    # 类变量
    b = 100

    @classmethod
    def fun2(cls):
        print(cls.b)

    def __init__(self,a):
        # 实例变量
        self.a = a

    # 实例方法
    def fun1(self):
        print(self.a)

    @staticmethod
    def fun3():
        print("fun3")


c01 = MyClass02(6)
# 调用实例方法
c01.fun1()
# 调用类方法
MyClass02.fun2()


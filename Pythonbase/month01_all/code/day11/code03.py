"""
    静态方法
"""
# def fun1():
#     print("fun1")
#
# def fun2():
#     print("fun2")


class MyClass:
    # 不需要使用对象的类的成员
    # 可是以面向对象的思想，应该使用类包装函数。
    @staticmethod
    def fun1():
        print("fun1")

    @staticmethod
    def fun2():
        print("fun2")


MyClass.fun1()
MyClass.fun2()




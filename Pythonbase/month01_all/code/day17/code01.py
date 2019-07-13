"""
    多继承

"""
class A:
    def m01(self):
        print("A的m01方法")

class B(A):
    def m01(self):
        print("B的m01方法")

class C(A):
    def m01(self):
        print("C的m01方法")

class D(B,C):
    def m01(self):
        super().m01()
        print("D的m01方法")

d01 = D()
d01.m01()
print(D.mro())



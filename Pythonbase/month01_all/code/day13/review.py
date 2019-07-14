"""
    day12(JS).txt 复习
    1.封装：
    （1）数据角度讲：用一个类包装多个变量（数据），还可以定义方法，操作数据。
        比如：向量(x，y   向右   模长  投影)

    （2）行为角度讲：不同程序员开发不同功能，需要使用时，只需要调用，不需要思考其内部实现。
        例如：张三开车回家，
        封装手段：私有成员/属性/__slots__

    (3) 设计角度讲：
        分而治之 -- 拿到需求后，分析解决问题的类，让每个类负责处理一件事。
        封装变化 -- 找出可能变化的功能，使用类单独定义。

        高内聚 -- 类中所有成员负责一件事。
        低耦合 -- 类与类之间的关系尽可能少，一个类的变化，不影响其他类。
"""
class MyClass:

    y = 0

    @classmethod
    def fun1(cls):
        pass

    def fun2(self):
        print(self.x)

    def __init__(self,x):
        self.x = x
        # 私有变量
        self.__y = 100
        self.__z = 0

    # 属性拦截了对变量的读写操作
    @property
    def x(self):
        if self.__x < 0:
            return 0
        return  self.__x

    @x.setter
    def x(self,value):
        self.__x = value

    # 只有 @property 的属性，称之为只读属性。
    @property
    def y(self):
        return  self.__y

    # @z.setter
    # def z(self, value):
    #     self.__z = value

    # 定义只写属性
    #1. 定义私有的写入方法
    def __set_z(self, value):
        self.__z = value

    # z = property(读取方法，写入方法)
    #2. 定义只写属性
    z = property(None,__set_z)


# 建议使用类名 访问类成员
print(MyClass.y)
MyClass.fun1()


# 其实语法上可以通过对象地址访问类成员
c01 = MyClass(1)
print(c01.y)
c01.fun1()
# 实例方法 建议通过对象地址调用
c01.fun2()
# 实际也可以通过类名调用，但仍然需要传递对象地址
MyClass.fun2(c01)

c01.x = -1
print(c01.x)

# 只读属性
print(c01.y)
# c01.y = 200

c01.z = 200
# c01.set_z(200)
# print(c01.z)
print(c01._MyClass__z)











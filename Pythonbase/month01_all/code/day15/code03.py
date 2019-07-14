"""
    继承 -- 架构设计
"""


# 老张开车回家
# 需求变化：可能坐飞机/火车/.....
class Person:
    # 违反面向对象设计原则
    # 开闭原则：对扩展开放   对修改关闭
    #          增加新功能   不要改变(增加/修改/删除)以前的代码
    # 依赖倒置：使用 抽象(父类)
    #          调用者，应该选择父类的成员，而无视子类。
    #
    """
    def go_home(self,type):
        if type == "火车":
            print("呜呜呜～")
        if type == "飞机":
            print("嗖嗖嗖～")

        # 增加：汽车
        if type == "汽车":
            print("滴滴 闷闷～")
        # 封装：分而治之 封装变化 高内聚  低耦合

p01 =Person()
p01.go_home("火车")
    """

    def go_home(self, vehicle):
        # 如果传入的对象 不是 交通工具 则退出方法
        if not isinstance(vehicle, Vehicle):
            return
        # if type == "火车":
        #     type.move()
        # if type == "飞机":
        #     type.fly()

        # 【多态】
        # 调用交通工具的运输方法
        # 实际执行火车/飞机的运输方法(因为传入的是子类对象)
        vehicle.transport()


class Vehicle:
    """
        交通工具
    """
    def transport(self):
        # 人为抛出一个未实现错误
        # 目的：约束/要求  子类必须具有当前方法
        raise NotImplementedError()


class Train(Vehicle):
    """
        火车类
    """

    # def move(self):
    #     print("呜呜呜~")
    def transport(self):
        print("呜呜呜~")


class Airplane(Vehicle):
    """
        飞机类
    """

    # def fly(self):
    #     print("嗖嗖~")
    def transport(self):
        print("嗖嗖~")


class Car(Vehicle):
    """
        汽车类
    """

    def transport(self):
        print("滴滴呜呜~")


# 测试..............................
p01 = Person()
p01.go_home(Train())
p01.go_home(Airplane())
p01.go_home(Car())

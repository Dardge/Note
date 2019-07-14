"""
作业1：在控制台中录入汽车信息(类型，速度，重量)，按e键退出，最后将每个信息显示在控制台中。
"""
class Car:
    # 构造函数
    def __init__(self,type,speed,weitht):
        self.type = type
        self.speed = speed
        self.weitht = weitht

    def print_self(self):
        print(self.type,self.speed,self.weitht)

    # count = 0
    #
    # @classmethod
    # def print_count(cls):
    #     print(cls.count)


list_car = []
while True:
    type = input("请输入类型：")
    speed = input("请输入速度：")
    weight = input("请输入重量：")
    obj = Car(type,speed,weight)
    list_car.append(obj)
    if input("按e键退出") == "e":
        break


for item in list_car:
    item.print_self()














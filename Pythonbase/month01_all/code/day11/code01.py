"""
    内存图
"""

class Wife01:
    """
        老婆类
    """
    # 构造函数
    def __init__(self,name,age,sex):
        # 数据
        self.name = name
        self.age = age
        self.sex = sex

    # 方法
    def print_self(self):
        print("奴家叫:%s,芳龄%d,性别%s"%(self.name,self.age,self.sex))


# 对象
w01 = Wife01("铁锤",60,"男")
w02 = Wife01("如花",20,"女")

w01.print_self()
w02.print_self()

# 通过对象地址调用方法，会自动传递对象地址到self变量中
# 如果对象存储该数据，则设置数据值。
w01.age = 16
w01.print_self()
# python 可以运行时为对象添加新数据
# 对象没有该数据，则添加数据。
w01.money = 10000
print(w01.money)

w02.print_self()






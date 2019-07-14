"""
    类 和 对象
"""

class Wife01:
    """
        老婆类    17:05 上课
    """
    # 备注：init方法，前后各有两个下划线。
    def __init__(self,name,age,sex):
        print(id(self))
        # self 会自动绑定对象地址
        # 数据
        self.name = name
        self.age = age
        self.sex = sex

    # 方法
    def cooking(self):
        print("做饭")

# 对象
w01 = Wife01("铁锤",60,"男")
print(id(w01))
w01.cooking()

w02 = Wife01("如花",20,"女")
w02.cooking()



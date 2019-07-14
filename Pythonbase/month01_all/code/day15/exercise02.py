"""
    若干个圆形(面积：半径平方*pi)，若干个矩形(面积：长*款)。
    定义图形管理器，定义记录所有图形(圆形，矩形)的变量.
                    定义计算所有图形面积的方法。
    需求变化：可能会增加新的图形(三角形…..)。
    要求：代码体现开闭原则，依赖倒置原则。
    验收：架构图、说出哪里体现了面向对象设计原则、代码实现。
"""
import math


class Graphic:
    """
        图形类,主要职责：约束所有图形，必须具有的行为
              次要任务：定义所有图形的共性代码
    """

    def __init__(self, name):
        self.name = name

    def get_area(self):
        """
            获取面积
        :return:
        """
        raise NotImplementedError()


class Circle(Graphic):
    """
        圆形
    """

    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def get_area(self):
        # 3.14 * self.radius ** 2
        return math.pi * self.radius ** 2


class Rectangle(Graphic):
    """
        矩形
    """

    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


class GraphicManager:
    # 记录所有图形
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        # graphic 必须是 图形
        if isinstance(graphic, Graphic):
            self.__graphics.append(graphic)

    # 计算所有图形的总面积
    def get_total_area(self):
        sum = 0
        for item in self.__graphics:
            #【多态】
            #调用的是图形计算面积方法
            #执行的是圆形/矩形计算面积方法
            sum += item.get_area()
        return sum


# 测试
c01 = Circle("大圆形", 10)
c02 = Circle("小圆形", 2)

r01 = Rectangle("大矩形", 5, 8)
r02 = Rectangle("小矩形", 2, 3)

manager = GraphicManager()
manager.add_graphic(c01)
manager.add_graphic(c02)
manager.add_graphic(r01)
manager.add_graphic(r02)
# manager.add_graphic(123)
# manager.graphics.append(c01)
# manager.graphics.append(c02)
# manager.graphics.append(r01)
# manager.graphics.append(r02)

total_area = manager.get_total_area()
print(total_area)

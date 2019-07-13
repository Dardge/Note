"""
     需求：张三开车回家。
     核心思想：分而治之   封装变化

"""


class Person:   
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    def go_home(self, car):
        print(self.name, end="")
        car.run("家")
class Car:
    def run(self, pos):
        print("移动到" + pos)
zs = Person("张三")
car = Car()
zs.go_home(car)

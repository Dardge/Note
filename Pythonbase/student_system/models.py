"""
    学生管理系统数据模块
"""

class StudentModel:
    """
        数据模型类
    """

    def __init__(self, id=0, name="", age=0, score=0):
        """
        创建学生对象
        :param id: 编号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def __str__(self):
        return "我的编号是%d,姓名是%s,年龄是%d,成绩是%d."%(self.id,self.name,self.age,self.score)

    def __repr__(self):
        return "StudentModel(%d,'%s',%d,%d)"%(self.id,self.name,self.age,self.score)
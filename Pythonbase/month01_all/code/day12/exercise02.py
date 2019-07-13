"""

"""

#15：35
class Student:
    def __init__(self, name, age, sex, score):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value


    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):
        self.__sex = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


s01 = Student("zs", 25, "男", 100)
print(s01.name)
s01.score = 110

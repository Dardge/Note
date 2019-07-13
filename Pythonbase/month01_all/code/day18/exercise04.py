"""
    16:50
"""

# 封装需要传递的错误信息
class ScoreError(Exception):
    def __init__(self, code, msg):
        super().__init__(msg)
        self.code = code
        self.msg = msg

class Student:
    def __init__(self, score):
        self.score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ScoreError(28, "范围不对") # 传递错误信息


try:
    w01 = Student(200)
    print(w01.age)
except ScoreError as e:  # 接收错误信息
    print("错误的行数是：", e.code)
    print("错误的原因是：", e.msg)

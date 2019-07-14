"""
    16:50
"""


# 自定义异常类，命名：XXXError，基类：Exception
class AgeError(Exception):
    def __init__(self, code, msg):
        # super().__init__(msg)
        self.code = code
        self.msg = msg
        # ...

class Wife:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 20 <= value <= 30:
            self.__age = value
        else:
            # 人为抛出异常：向外(34行的调用者)传递错误信息。
            # raise ValueError("我不要")
            raise AgeError(28, "我不要")


try:
    w01 = Wife(86)
    print(w01.age)
except AgeError as e:  # 接收错误信息
    print("错误的行数是：", e.code)
    print("错误的原因是：", e.msg)

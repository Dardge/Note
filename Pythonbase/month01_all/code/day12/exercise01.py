"""
    总结：私有化变量   __名称
        通过方法操作变量  set_名称(数据)
                        get_名称()
"""

class Student:
    def __init__(self,name,age):
        # self.name = name
        # self.age = age
        self.set_name(name)
        self.set_age(age)


    def get_name(self):
        return  self.__name

    def set_name(self,value):
        self.__name = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value


s01 = Student("zs",25)
s01.set_age(26)
print(s01.get_name())
print(s01.get_age())














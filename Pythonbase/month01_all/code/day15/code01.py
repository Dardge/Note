"""
    继承--方法
    子类 直接使用 父类的成员
"""
class Person:
    def say(self):
        print("说话")

class Student(Person):
    def study(self):
        print("学习")

class Teacher(Person):
    def teach(self):
        print("教学")

stu01 = Student()
stu01.study()
# 语法现象：子类直接具有父类成员
stu01.say()

tea01 = Teacher()
tea01.say()

# 语法现象：父类只能使用自身成员
per01 = Person()
per01.say()

# 对象是否兼容类 = isinstance(对象,类)
# True  本类对象 兼容  本类
#   字面意思： 对象是不是一种类
print(isinstance(stu01,Student))
# False
print(isinstance(stu01,Teacher))
# True 子类对象 兼容  父类
print(isinstance(stu01,Person))


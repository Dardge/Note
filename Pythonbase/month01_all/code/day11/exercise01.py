"""
    内存图
"""

class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_self(self):
        print(self.name,self.score)

# 画出下列代码内存图：14:15
s01 = Student("张三",100)
s02 = Student("李四",80)
s01.print_self()
s02.print_self()








s03 = s01
# 改变对象
s01.score = 200
print(s03.score)#

s04 = s02
# 改变变量
s02 = Student("王五",90)
print(s04.score)







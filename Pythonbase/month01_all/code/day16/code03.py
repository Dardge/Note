"""
    内建函数重写
"""
class Wife:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # 对象转换的字符串(给人看的)
    def __str__(self):
        return "我是%s,今年%d岁啦。"%(self.name,self.age)

    # 对象转换的字符串(给解释器看eval函数能执行的)
    def __repr__(self):
        return 'Wife("%s",%d)'%(self.name,self.age)

w01 = Wife("铁锤公主",26)
# w02 = eval(repr(w01)) # repr(w01) --> w01.__repr__()
print(w01) #print 内部使用  __str__ 返回的字符串
list01 = [w01]
print(list01) # print 列表时，内部使用的是__repr__ 返回对象字符串

# 练习：将学生管理系统中的StudentModel类，__str__/__repr__进行重写。


# 练习：使用eval函数，实现在控制台中录入4位整数，计算每位相加和。
# print(w01)
# num01 = eval("1+2")
# print(num01)
# str_input = "1234"
# re = eval("%static+%static+%static+%static"%(str_input[0],str_input[1],str_input[2],str_input[3]))
# print(re)







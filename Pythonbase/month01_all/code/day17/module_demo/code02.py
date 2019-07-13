"""
    模块
    调动功能的模块
"""

# 导入模块方式1:本质定义一个变量，与模块关联。
import module01
import module01# 重复导入模块，模块中的代码也不会重复执行

# module01.fun01()

my01 = module01.MyClass01()
my01.fun02()

# 可以使用隐藏成员
# module01._fun02()

# 导入模块方式2  通过as关键字 为模块起别名
# 适用于模块名比较长
# import module01 as m
#
# m.fun01()
#
# my01 = m.MyClass01()
# my01.fun02()

# 导入模块方式3：将模块内的成员，引入当前模块的作用域中
# from module01 import fun01
#
# fun01()
#
# # 无法使用MyClass01
# # my01 = MyClass01()
# # my01.fun02()



# 导入模块方式4：将指定模块中所有成员，引入到当前模块作用域中。
# 缺点：如果不清楚模块成员，可能会造成，命名冲突。
# from module01 import *
#
# def fun01():
#     print("code02--fun01")
#
# fun01()
# # 没有导入隐藏成员
# # fun02()
#
# my01 = MyClass01()
# my01.fun02()











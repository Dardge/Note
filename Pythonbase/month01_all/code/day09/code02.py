"""
    形参传递方式
    位置形参
        星号元组形参
"""

# 位置形参
def fun1(a,b,c):
    pass

# 星号元组形参：收集多余位置形参
def fun2(*args):
    # 对于函数而言，args就是元组
    print(len(args),args)

fun2()
fun2(1)
fun2(1,2)

#练习：定义函数，累加整数。


def fun3(a,*args):
    # 对于函数而言，args就是元组
    print(len(args),args)

fun3(1)






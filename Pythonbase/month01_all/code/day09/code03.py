"""
    形参传递方式
        命名关键字形参
"""


# 命名关键字形参:强制实参使用关键字传递。
def fun1(*, a, b):
    print(a, b)


# fun1(1,2)
# fun1(*[1,2])
fun1(b=2, a=1)
fun1(**{"b": 2, "a": 1})

# a b 是位置传参，c,d 必须是关键字传参
def fun2(a, b, *, c, d):
    print(a, b, c, d)


fun2(1, 2, c=3, d=4)

# 星号元组形参后的，位置形参是命名关键字形参。
def fun3(*args, c, d):
    print(args, c, d)

fun3(3,4,4,5665,d = 9,c=5)

# 练习：print函数定义
# print(*args, sep=' ', end='\n', file=None)
# 打印(内容，sep = “连接符号”, end = "结束符号")
print("asdf",1343,sep = "$",end = "\n\n\n\n\n")
print("ok")

# 双型号字典形参:可以收集多余的字典关键字实参
def fun4(**kwargs):
    # 对于函数内部而言，就是字典
    print(kwargs)

# fun4(1,2,3)
fun4(a = 1,c = "ccccc",d = [1,2,3],e = True)

def fun5(*args,**kwargs):
    print(args,kwargs)

fun5()
fun5(23,34,a = "adsf",qtx = "qtx")




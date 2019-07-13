"""
    day09 复习
    函数的参数传递
    实参传递方式：
        位置传参：实参与形参的位置依次对应
            -- 序列传参：实参用*拆解后与形参依次对应。
        关键字传参：实参根据形参的名字进行对应
                  配合形参的缺省参数，可以使调用者随意传参。
            -- 字典传参： 实参使用**将字典拆解后与形参的名字对应。

    形参传递方式：
        缺省(默认置传参)参数：参数具有默认值
            -- 星号元组参数：收集多余的位置传参。

        命名关键字传参：强制实参使用关键字传递
            -- 双星号字典参数：收集多余的关键字传参

"""
def fun1(a = 0,b = 0,c = 0):
    pass

fun1(1,2,3)
list01 = [2,5,7]
# 运行时构建列表
fun1(*list01)
fun1(a = 1,c =3,b = 2)
fun1(b = 1)
# 运行时构建字典
dict01 = {"a":1,"c":3,"b":2}
fun1(**dict01)


def fun2(*args):
    # args 就是一个元组
    for item in args:
        print(item)

# 可以不传
fun2()
# 也可以传递随意个数
fun2(123,123,4,5)


def fun3(e,*,a,b,c):
    pass

def fun4(*args,a,b,c):
    pass

fun4(1,2,3,3,a = 1,b=1,c = 3)

def fun5(**kwargs):
    print(kwargs)
    for item in kwargs.items():
        print(item)

fun5(a = 1,c = 2)
















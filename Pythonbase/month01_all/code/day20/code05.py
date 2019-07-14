"""
    Encolsing 外部嵌套作用域
"""
# def fun01():
#     a = 1
#     print("fun01 -- a",a)
#     def fun02():
#         print("fun02 -- a",a) # 可以访问外部嵌套变量
#
#     fun02()
#
# fun01()

def fun01():
    a = 1

    def fun02():
        # a = 2 # 创建了02内的新变量
        nonlocal a # 定义外部作用域变量a，不是fun02的局部变量
        a = 2
        print("fun02 -- a",a)

    fun02()
    print("fun01 -- a", a)

fun01()





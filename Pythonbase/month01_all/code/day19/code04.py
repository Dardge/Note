"""
    生成器
"""
def my_iter():
    print("准备生成数字1")
    yield 1

    print("准备生成数字2")
    yield 2

    print("准备生成数字3")
    yield 3

# 调用方法时不执行
iterator = my_iter()
print(iterator.__next__())
print(iterator.__next__())
# 练习：将迭代器实现的MyRange类，修改为yield实现。 15:50













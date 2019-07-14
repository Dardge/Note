"""
    身份运算符
"""


a = 500
b = 600
c = a
re01 = a is b
re02 = a is c
print(re01) # False
print(re02) # False
# ｉｄ函数返回变量所关联的对象地址
print(id(a),id(b),id(c))


# 文件式ｐｙｔｈｏｎ对一下代码做了优化
# 优化：创建一个８００对象
# 交互式ｐｙｔｈｏｎ中就是２个对象
num01 = 800
num02 = 800
print(id(num01),id(num02))
print(num01 is num02)# true





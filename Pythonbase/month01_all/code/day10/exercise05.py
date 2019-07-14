"""
    统计hello函数调用的次数。
"""
count = 0

def hello():
    # 函数内部修改全局变量
    global count
    count += 1
    print("hello")


hello()
hello()
hello()
print(count)
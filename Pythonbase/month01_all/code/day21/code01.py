"""
    装饰器
"""
"""
# 需要增加的功能
def print_func_name(func):
    print(func.__name__)

# 已有代码
def say_hello():
    print("hello")
    # 直接调用
    print_func_name(say_hello)


def say_goodbye():
    print("goodbye")
    print_func_name(say_goodbye)


say_hello()
say_goodbye()
"""
# ------在不改变原有功能代码，以及调用功能代码基础上，增加新功能------------
"""
def print_func_name(func):
    def wrapper():
        # 需要增加的功能
        print(func.__name__)
        # 传入的功能
        return func()
    return wrapper

# 已有代码
def say_hello():
    print("hello")

def say_goodbye():
    print("goodbye")

# say_hello 得到的是内嵌函数(需要增加的功能 + say_hello功能)
say_hello = print_func_name(say_hello)
say_goodbye = print_func_name(say_goodbye)

say_hello()
say_goodbye()
"""

"""
def print_func_name(func):
    def wrapper(): 
        # 需要增加的功能
        print(func.__name__)
        # 传入的功能
        return func()
    return wrapper

# 目的：拦截对被装饰方法的调用
@print_func_name # say_hello = print_func_name(say_hello)
def say_hello():
    print("hello")

@print_func_name # say_goodbye = print_func_name(say_goodbye)
def say_goodbye():
    print("goodbye")

say_hello()
say_goodbye()
"""

def print_func_name(func):
    def wrapper(*args,**kwargs):
        # 需要增加的功能
        print(func.__name__)
        # 传入的功能
        return func(*args,**kwargs)
    return wrapper

# 目的：拦截对被装饰方法的调用
@print_func_name # say_hello = print_func_name(say_hello)
def say_hello(name):
    print(name,"hello")

@print_func_name # say_goodbye = print_func_name(say_goodbye)
def say_goodbye(name,age):
    print(name,age,"goodbye")

say_hello("李四")
say_goodbye("李四",25)
"""
    提供功能的模块
"""

# 当前模块被导入时执行
print("module01模块")

def fun01():
    print("module01 -- fun1")

# 隐藏成员：当前模块内使用的成员
def _fun02():
    print("module01 -- _fun2")

class MyClass01:
    def fun02(self):
        print("MyClass01 -- fun02")

print(__name__)

# __name__ 属性是当前模块名称 module01
# 如果程序从当前模块运行，则名称改为 __main__

# 作用：在if代码块中定义，只能从当前模块开始执行，才调用的代码。
if __name__ == "__main__":
    fun01()












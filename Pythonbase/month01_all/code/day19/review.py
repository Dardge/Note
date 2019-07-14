"""
    day18 复习
    1.  包
       -- 作用：将模块以文件夹的形式进行分组管理
       -- 导入：import 包
               from 包 import 模块
               from 包.子包 import 模块
               备注：从项目根目录开始计算包路径

               from 包 import *
               备注：在包的__init__.py模块中，设置__all__属性.

    2. 异常处理
        -- 异常现象：程序不再向下执行，而是转到函数的调用者。
        -- 处理：异常转换为正常流程。
        -- 语法：try:
                    ....
                except 异常类型1:
                    ....
                except 异常类型2:
                    ....
                except Exception:
                    ....
        -- 人为抛出异常：raise 异常类型
                       传递错误信息比较困难时使用
           自定义异常：封装错误信息

"""
# python 程序结构
# 包 package     将模块以文件夹的形式进行分组管理
#     模块.py          将类有逻辑的组织在一起
#            class MyClass:      将方法有逻辑的定义在一起
#                 def print_hello(self):   将语句有逻辑的定义在一起
#                        print("hello world")
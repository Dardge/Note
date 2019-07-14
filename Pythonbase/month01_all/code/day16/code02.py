"""
    类与类关系
"""


# 泛化  --- 做成父子
# class A: # 交通工具
#     pass
#
#
# class B(A):# 火车
#     pass

# 关联 ---  做成成员变量
# class A:# 员工
#     def __init__(self,b):
#         self.b = b# 岗位
#
#
# class B:
#     pass
#
# a01 = A(B())

# 依赖  ----   做成参数
class A:# 人 回家 使用 交通工具
    def fun1(self, b):
        pass

class B:
    pass


a01 = A()
a01.fun1(B())

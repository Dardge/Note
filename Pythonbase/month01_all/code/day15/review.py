"""
    day15 复习
    10:35 上课
"""

class XXXModel:
    pass


class XXXView:
    def __init__(self):
        # 1. 视图类 创建 控制器 对象
        self.__controller = XXXController()

    def __input_students(self):
        # 2. 视图类 调用 控制器 方法
        stu = XXXModel()
        self.__controller.add_student()

    def fun1(self):
        self.__input_students()

class XXXController:
    def add_student(stu):
        pass

v = XXXView()
v.fun1()



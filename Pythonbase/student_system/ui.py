"""
    学生管理系统表示层
"""

from bll import *
from models import *

class StudentManagerView:
    """
        界面视图类
    """

    def __init__(self):
        # 创建逻辑控制类对象
        self.__controller = StudentManagerController()

    def __display_menu(self):
        """
            显示菜单
        :return:
        """
        print("---------------------")
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩降序显示")
        print("---------------------")

    def __select_menu(self):
        """
            选择菜单
        :return:
        """
        number = input("请输入选项：")
        if number == "1":
            self.__input_students()
        elif number == "2":
            self.__output_students(self.__controller.list_stu)
        elif number == "3":
            self.__delete_student()
        elif number == "4":
            self.__modify_student()
        elif number == "5":
            self.__output_students_by_score()

    def main(self):
        """
            学生管理器入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_int(self,msg):
        while True:
            try:
                return int(input(msg))
            except:
                print("输入有误")

    def __input_students(self):  # 17:15
        """
            录入学生信息
        :return:
        """
        while True:
            stu = StudentModel()
            stu.name = input("请输入姓名：")
            # while True:
            #     try:
            #         stu.age = int(input("请输入年龄："))
            #         break
            #     except:
            #         print("输入有误")
            # stu.age = int(input("请输入年龄："))
            # while True:
            #     try:
            #         stu.score = int(input("请输入成绩："))
            #         break
            #     except:
            #         print("输入有误")
            # stu.score = int(input("请输入成绩："))
            stu.age = self.__input_int("请输入年龄：")
            stu.score = self.__input_int("请输入成绩：")
            # 调用逻辑控制类的添加学生方法
            self.__controller.add_student(stu)
            if input("按y键继续") != "y":
                break

    def __output_students(self, list_stu):
        """
            在控制台中输出所有学生信息
        :param list_stu: 需要显示的学生列表
        :return:
        """
        for item in list_stu:
            print("%d | %s | %d | %d" % (item.id, item.name, item.age, item.score))

    def __delete_student(self):
        # id = int(input("请输入需要删除的学生编号："))
        id = self.__input_int("请输入需要删除的学生编号：")
        result = self.__controller.remove_student(id)
        if result:
            print("删除成功")
        else:
            print("删除失败")


        # 调用：self.__output_students(self.__controller.list_stu)
        # 练习：删除指定id的学生 __delete_student()
        #      在控制台中获取id，然后调用逻辑控制类的remove_student方法

        # 定义界面修改学生的方法__modify_student()
        # 在控制台中获取需要修改的学生信息(编号/....)
        # 创建学生对象，调用逻辑控制类 update_student()

    def __modify_student(self):
        stu = StudentModel()
        # stu.id = int(input("请输入编号："))
        stu.id = self.__input_int("请输入编号：")
        stu.name = input("请输入姓名：")
        # stu.age = int(input("请输入年龄："))
        stu.age =self.__input_int("请输入年龄：")
        # stu.score = int(input("请输入成绩："))
        stu.score = self.__input_int("请输入成绩：")
        # 调用逻辑控制类的修改学生方法
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    # 按照成绩降序显示学生
    def __output_students_by_score(self):
        result = self.__controller.order_by_score()
        self.__output_students(result)
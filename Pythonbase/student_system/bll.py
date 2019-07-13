"""
    学生管理系统业务逻辑层
    Busines
    Logic
    Layer
"""
from dal import TextDao

def sava_data(func):
    def wrapper(*args,**kwargs):# 被装饰方法(实例方法)
        result = func(*args,**kwargs)
        # TextDao.save_student_list(self.__list_stu)
        # args[0] 就是self
        # 因为在类外访问私有变量，所以必须使用_类名__变量名
        TextDao.save_student_list(args[0]._StudentManagerController__list_stu)
        return result
    return wrapper

class StudentManagerController:
    __slots__ = ("__list_stu")
    """
        逻辑控制类
    """

    def __init__(self):
        """
            创建学生管理器对象
        """
        # self.__list_stu = []
        # 从文件中读取 之前存储过的学生列表
        self.__list_stu = TextDao.load_student_list()

    @property
    def list_stu(self):
        return self.__list_stu

    def __generate_id(self):
        # 生成编号策略：在最后一个学生编号基础上增加1
        #             如果是第一个学生，则设置为1
        # if语句的真值表达式
        return 1 if len(self.__list_stu) == 0 else self.__list_stu[-1].id + 1

    @sava_data  # add_student = sava_data(add_student)
    def add_student(self, stu):
        """
            添加学生对象
        :param stu: 需要添加的学生对象(在界面中输入的信息)
        :return:
        """
        # stu.id = len(self.__list_stu) +1
        stu.id = self.__generate_id()
        self.__list_stu.append(stu)
        # TextDao.save_student_list(self.__list_stu)

    @sava_data
    def remove_student(self, id):
        for item in self.__list_stu:
            if item.id == id:
                self.__list_stu.remove(item)
                # TextDao.save_student_list(self.__list_stu)
                return True  # 表达删除成功
        return False  # 表达删除失败

    @sava_data
    def update_student(self, stu_info):
        # 需要修改的学生编号： stu_info.id
        # 需要修改的信息：stu_info.name  stu_info.age  .....
        for item in self.list_stu:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                # TextDao.save_student_list(self.__list_stu)
                return True
        return False

    def order_by_score(self):
        # 由于不允许改变self.__list_stu，所以通过切片生成一个新列表
        new_list = self.__list_stu[:]
        for r in range(len(new_list) - 1):
            for c in range(r + 1, len(new_list)):
                if new_list[r].score < new_list[c].score:
                    new_list[r], new_list[c] = new_list[c], new_list[r]
        return new_list
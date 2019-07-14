"""
    dal.py
    Data 数据
    Access 访问
    Layer 层
"""
# 1. 保存学生列表(由bll层的添加/删除/修改方法调用)
# 2. 加载学生列表(bll层的Controller类构造函数)
# 备注：参照day21/exercise03完成  15:45 上课
# 常量：不允许修改的数值
FILE_PATH = "list_stu.txt"
from models import StudentModel
import os

class TextDao:
    @staticmethod
    def save_student_list(list_stu):
        with open(FILE_PATH, "w", encoding="utf-8") as stu_file:
            for stu in list_stu:
                stu_file.write(stu.__repr__() + "\n")

    @staticmethod
    def load_student_list():
        list_stu = []
        # 如果文件不存  则退出
        if not os.path.isfile(FILE_PATH):
            return list_stu

        with open(FILE_PATH, "r", encoding="utf-8") as stu_file:
            for line in stu_file:
                # 读取数据 并 创建对象
                stu = eval(line)
                list_stu.append(stu)
        return list_stu


# 测试...............
# from models import StudentModel
#
# list_stu = [StudentModel(101, "zs1", 20, 100), StudentModel(102, "zs2", 25, 60)]
# TextDao.save_student_list(list_stu)
# for item in TextDao.load_student_list():
#     print(item)

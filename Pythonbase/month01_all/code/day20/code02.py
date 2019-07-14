"""
    使用工具类操作学生列表
"""


class StudentModel:
    def __init__(self, id=0, name="", age=0, score=0):
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return "StudentModel(%d,'%s',%d,%d)" % (self.id, self.name, self.age, self.score)


studs = [
    StudentModel(101, "z01", 18, 85),
    StudentModel(102, "z02", 26, 55),
    StudentModel(103, "z03", 27, 75),
    StudentModel(104, "z04", 35, 90),
]
# -------------------------------------------------
from common.list_tools import ListHelper

def condition01(item):
    return item.age > 25

# 查找年龄大于25的所有学生对象
# re01 = ListHelper.find_all(studs, condition01)
# for item in re01:
#     print(item)

#练习1：将通用的查找所有对象方法，定义到common/list_tools.py/ListHelper
#练习2：ListHelper类中，定义通用的查找单个对象方法。
#     例如：查找年龄小于30的单个(第一个)学生对象
#     例如：查找姓名是z03的单个(第一个)学生对象

def condition01(item):
    return item.age < 30
def condition02(item):
    return item.name == "z03"
# def get_student01(list_stu):
#     for item in list_stu:
#         if item.age < 30:
#             return item
# def get_student02(list_stu):
#     for item in list_stu:
#         if item.name == "z03":
#             return item
re01 = ListHelper.first(studs,condition02)
print(re01)

# 练习：通用的计算满足某个条件的对象数量
# 例如：查找成绩大于80的学生数量
# 例如：查找姓名是z01的学生数量

def condition03(item):
    return item.score > 80

def condition04(item):
    return item.name == "z01"

# def get_count01(list_stu):
#     int_count = 0
#     for item in list_stu:
#         if item.score > 80:
#             int_count += 1
#     return int_count
#
# def get_count02(list_stu):
#     int_count = 0
#     for item in list_stu:
#         if item.name == "z01":
#             int_count += 1
#     return int_count

re01 = ListHelper.count(studs,condition04)
print(re01)












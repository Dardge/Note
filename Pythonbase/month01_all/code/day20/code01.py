"""
    将函数作为参数传递
"""

class StudentModel:
    def __init__(self, id=0, name="", age=0, score=0):
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return "StudentModel(%d,'%s',%d,%d)"%(self.id,self.name,self.age,self.score)


studs = [
    StudentModel(101,"z01",18,85),
    StudentModel(102,"z02",26,55),
    StudentModel(103,"z03",27,75),
    StudentModel(104,"z04",35,90),
]
#------------------以下为封装思想------------------------
# 传统
# def get_students01(list_stu):
#     for item in list_stu:
#         if item.age > 25:
#             yield item

# def get_students02(list_stu):
#     for item in list_stu:
#         if item.score > 60:
#             yield item

# def get_students03(list_stu):
#     for item in list_stu:
#         if item.score < 90:
#             yield item
# 提取变化：
def condition01(item):
    return item.age > 25

# 直接调用变化：
def get_students01(list_stu):
    for item in list_stu:
        if condition01(item):
            yield item

# -- 计算所有成绩大于60的学生。
def condition02(item):
    return item.score > 60


def get_students02(list_stu):
    for item in list_stu:
        if condition02(item):
            yield item

# -- 计算所有成绩小于90的学生。
def condition03(item):
    return item.score < 90

def get_students03(list_stu):
    for item in list_stu:
        if condition03(item):
            yield item
#------------------将调用多个条件，抽象为调用一个方法-------------------

# 通用的查找学生方法
# 用参数 func_condition 抽象(代表) condition01   condition02  condition03
def get_students(list_stu,func_condition):
    for item in list_stu:
        if func_condition(item):
            yield item

# 不要加入小括号(不要调用函数)
# get_students(condition01())
# 将函数传递到get_students方法中
re02 = get_students(studs,condition01)
for item in re02:
    print(item)

re03 = get_students(studs, condition02)
for item in re02:
    print(item)







"""
    内置高阶函数
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
    StudentModel(102, "z02", 26, 150),
    StudentModel(103, "z03", 27, 75),
    StudentModel(104, "z04", 35, 90),
]
# -------------------------------------------------
from common.list_tools import ListHelper

# 查找成绩大于90的所有学生
# re01 = ListHelper.find_all(studs,lambda static:static.score > 90)
# 根据条件选择 类似：find_all
re02 = filter(lambda s:s.score > 90,studs )
# for item in re02:
#     print(item)


# 获取所有学生的成绩
# re01 = ListHelper.select(studs,lambda static:static.score)
re02 = map(lambda s:s.score,studs)
# for item in re02:
#     print(item)


# re01 = ListHelper.order_by(studs,lambda static:static.score)

# for item in sorted(studs,key = lambda static:static.score):
#     print(item)

for item in sorted(studs,key = lambda s:s.score,reverse=True):
    print(item)

# print(ListHelper.get_max(studs,lambda static:static.age))
print(max(studs,key =lambda s:s.age ))








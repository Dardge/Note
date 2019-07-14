"""
    lambda 表达式
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

# def condition01(item):
#     return item.age > 25
#
# def condition02(item):
#     return item.name == "z03"
#
# def condition03(item):
#     return item.score > 80
#
# def condition04(item):
#     return item.name == "z01"

# re01 = ListHelper.find_all(studs,condition01)
# lambda 参数:方法体

# 查找年龄大于25的所有学生
re01 = ListHelper.find_all(studs,lambda item:item.age > 25)
# for item in re01:
#     print(item)

# 查找名字是z03的学生
re02 = ListHelper.first(studs,lambda s:s.name == "z03")
print(re02)

# 查找成绩大于80的学生数量
re03 = ListHelper.count(studs,lambda stu:stu.score > 80)
print(re03)

# 练习1：查找编号是101的单个学生对象
# print(ListHelper.first(studs,lambda stu:stu.id == 101))

# 练习2：查找成绩小于60的所有学生对象
# for item in ListHelper.find_all(studs,lambda element:element.score < 60):
#     print(item)

# 练习3：查找年龄大于20并且成绩大于60的所有学生
# for item in ListHelper.find_all(studs,lambda e:e.age>20 and e.score >60):
#     print(item)

# 需求：查找年龄最大的学生对象
#      查找成绩最高的学生对象
# 练习：定义通用的查找最大值方法

# def get_max01(list_stu):
#     value_max = list_stu[0]
#     for i in range(1,len(list_stu)):
#         if value_max.age <  list_stu[i].age:
#             value_max = list_stu[i]
#     return value_max
#
# def get_max02(list_stu):
#     value_max = list_stu[0]
#     for i in range(1,len(list_stu)):
#         if value_max.score <  list_stu[i].score:
#             value_max = list_stu[i]
#     return value_max

# def condition01(item):
#     return item.score

print(ListHelper.get_max(studs,lambda item:item.age))

# 需求：
# 累加所有学生的成绩
# 累加所有学生的年龄
# 练习：定义通用的累加方法
# def get_scores(list_stu):
#     value_sum = 0
#     for item in list_stu:
#         value_sum += item.score
#     return value_sum
#
# def get_ages(list_stu):
#     value_sum = 0
#     for item in list_stu:
#         value_sum += item.age
#     return value_sum

print(ListHelper.sum(studs,lambda item:item.score))

# 需求：
# 获取所有学生的成绩
# 获取所有学生的姓名
# 练习：定义通用的筛选对象方法
# def get_scores(list_stu):
#     for item in list_stu:
#         yield item.score
#
# def get_names(list_stu):
#     for item in list_stu:
#         yield item.name

for item in ListHelper.select(studs,lambda s:s.score):
    print(item)

# 需求：按照成绩对学生列表进行升序
# 需求：按照年龄对学生列表进行升序
# 练习：定义通用的升序排列方法
# def order_by(list_target):
#     for r in range(len(list_target) - 1):
#         for c in range(r+1,len(list_target)):
#             if list_target[r].score > list_target[c].score:
#                 list_target[r],list_target[c] = list_target[c],list_target[r]

ListHelper.order_by(studs,lambda s:s.age)
for item in studs:
    print(item)












"""
    day19 复习
     生成器
        -- 生成器函数
        def 函数:
            ..
            yield 数据
            ..

        for item in 函数():
            语句
        -- 生成器表达式
          (表达式 for 变量 in 可迭代对象)
"""
# 练习：定义学生类,分别使用生成器函数/生成器表达式/列表推导式实现。
# -- 计算所有年龄大于25的学生。
# -- 计算所有成绩大于60的学生。
# -- 计算所有成绩大于90的学生。

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
# -- 计算所有年龄大于25的学生。
# 传统方式实现
def get_students01(list_stu):
    result = []
    for item in list_stu:
        if item.age > 25:
            result.append(item)
    return result

re01 = get_students01(studs)
for item in re01:
    print(item)

# 生成器函数实现
def get_students01(list_stu):
    for item in list_stu:
        if item.age > 25:
            yield item
re01 = get_students01(studs)

for item in re01:
    print(item)

# 列表推导式实现
re01 = [item for item in studs if item.age > 25]
for item in re01:
    print(item)

# 生成器表达式实现
re01 = (item for item in studs if item.age > 25)
for item in re01:
    print(item)

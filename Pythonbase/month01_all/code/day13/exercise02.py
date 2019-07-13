"""
    1. 定义学生类(姓名，成绩)

    2. 定义根据名称，查找学生对象的方法。
       def xxx(list_stu,stu_name):
          ......

    3. 创建3个学生对象并加入到列表中，指定不同的名字与成绩。
       再调用第二步的方法
"""


class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    # 方法：是面向对象的叫法。
    def print_self(self):
        print(self.id, self.name, self.score)


s01 = Student(1, "zs", 11)
s01.name = "ls"


# 函数：是面向过程的叫法。
def get_student_by_name(list_stu, stu_name):
    for item in list_stu:
        if item.name == stu_name:
            return item
            # return None


def get_student_by_id(list_stu, stu_id):
    # 遍历学生列表
    for item in list_stu:
        # 判断每个学生对象的编号 是否与 需要查找的编号相同
        if item.id == stu_id:
            # 返回学生对象
            return item


list_stu = [
    Student(101, "zs", 86),
    Student(104, "ww", 90),
    Student(102, "ls", 100),
    Student(103, "ww", 90),
]


# stu = get_student_by_name(list_stu, "ww")
# if stu != None:
#     stu.print_self()
# else:
#     print("查无此人")


# 练习：查找成绩大于等于90的学生对象
def get_students_by_score(list_stu, score):
    result = []
    for item in list_stu:
        if item.score >= score:
            item.print_self()
            result.append(item)
    return result


# result = get_students_by_score(list_stu, 90)
# for item in result:
#     item.print_self()

# 练习2:查找列表中成绩最高的学生  17:10
def get_max_by_score(list_stu):
    # 假设第一个元素就是最大值
    max = list_stu[0]
    # 依次与后面元素进行比较
    for i in range(1, len(list_stu)):
        if max.score < list_stu[i].score:
            # 如果发现还有更大的，则替换假设的最大值
            max = list_stu[i]
    return max


# stu = get_max_by_score(list_stu)
# stu.print_self()


# 练习3：查找列表中id最小的学生。
def get_min_by_id(list_stu):
    min = list_stu[0]
    for i in range(1, len(list_stu)):
        if min.id > list_stu[i].id:
            min = list_stu[i]
    return min


# 练习4：在列表中查找指定姓名的学生(同名学生全部查找出来)17:29
def get_students_by_name(list_stu, stu_name):
    result = []
    for item in list_stu:
        if item.name == stu_name:
            result.append(item)
    return result


# result = get_students_by_name(list_stu,"ww")
# for item in result:
#     item.print_self()

# 练习5：将学生列表按照成绩做降序(高-->低)排列
def order_by_score(list_stu):
    for r in range(len(list_stu) - 1):
        for c in range(r + 1, len(list_stu)):
            if list_stu[r].score < list_stu[c].score:
                list_stu[r], list_stu[c] = list_stu[c], list_stu[r]


order_by_score(list_stu)
for item in list_stu:
    item.print_self()







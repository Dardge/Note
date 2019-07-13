class Employee:
    def __init__(self, name,job_object):
        self.name = name
        self.job_object = job_object

    def get_salary(self):
        # 员工不要计算工资，将计算工资的算法，交给job负责。
        # 员工要选择job。
        return self.job_object.calculate_salary()

class Job:
    def __init__(self,base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Programmer(Job):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus
        # print("程序员计算薪资")
        # pass
        # return super().base_salary + self.bonus

class Tester(Job):
    def __init__(self,base_salary, bug_count):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def calculate_salary(self):
        return super().calculate_salary() + self.bug_count * 5


class Salesmen(Job):
    def __init__(self, base_salary, sale_value):
        super().__init__(base_salary)
        self.sale_value = sale_value

    def calculate_salary(self):
        return super().calculate_salary() + self.sale_value * 0.05


"""
s01 = Salesmen("小王",3000,500)
print(s01.calculate_salary())
# 转岗 程序员
# 重新招聘程序员"小王",开除销售"小王"
s01 = Programmer("小王",8000,10000)
print(s01.calculate_salary())
# 问题：员工转岗时，必须销毁所有变量。
# 目标：让对象部分改变，而不是整体改变。
"""

s01 = Employee("小王",Salesmen(3000,500))
print(s01.get_salary())

# 转岗
s01.job_object = Programmer(8000,10000)

print(s01.get_salary())





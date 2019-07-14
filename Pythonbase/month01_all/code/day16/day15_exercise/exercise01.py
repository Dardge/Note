"""
    一家公司有如下几种岗位，
    程序员：底薪 + 项目分红
    软件测试：底薪 + Bug数 * 5
    销售：底薪 + 销售额*5%
            定义员工管理器，记录所有员工，计算所有员工的总薪资。
    要求：增加新的岗位，员工管理器满足开闭原则。
         画出架构图，写出体现依赖倒置原则、开闭原则的点。
"""

class Employee:
    def __init__(self,base_salary):
        self.base_salary = base_salary


    def calculate_salary(self):
        """
            计算薪资
        :return:
        """
        # raise NotImplementedError()
        return self.base_salary

class Programmer(Employee):
    def __init__(self,base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # return super().base_salary + self.bonus
        return super().calculate_salary() + self.bonus

class Tester(Employee):
    def __init__(self,base_salary,bug_count):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def calculate_salary(self):
        return super().calculate_salary() + self.bug_count * 5

class Salesmen(Employee):
    def __init__(self, base_salary, sale_value):
        super().__init__(base_salary)
        self.sale_value = sale_value

    def calculate_salary(self):
        return super().calculate_salary() + self.sale_value * 0.05


class EmployeeManager:
    def __init__(self):
        self.__total_employee = []

    def add_employee(self,emp):
        # 可以添加的对象，必须是员工
        if not isinstance(emp,Employee):
            return
        self.__total_employee.append(emp)

    def get_total_salary(self):
        sum = 0
        for item in self.__total_employee:
            # 调用的是：员工类 Employee 的方法
            # 执行的是：具体员工(程序员/测试员)的方法
            sum += item.calculate_salary()
        return sum

# 测试
# 能否正确添加员工
# 能否正确计算工资
manager = EmployeeManager()
manager.add_employee(Programmer(8000,1000000))
manager.add_employee(Tester(5000,100))
manager.add_employee(Salesmen(3000,300000))
manager.add_employee("你大爷")
total_salary = manager.get_total_salary()
print(total_salary)









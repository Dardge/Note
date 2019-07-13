"""
使用代码描述一下场景
张三 教 李四 学王者荣耀。
李四 教 张三 学Python
李四 上班赚了 5000元钱
最后输出张三具有的技能，李四具有的技能，以及他们的钱。
"""
class Person:
    # skills 是列表，属于可变对象。作为默认参数后，每次传递的都是同一个列表对象。
    # 结论：不要给可变数据定义默认参数。

    # def __init__(self,name,skills = [],money = 0):
    #     self.name = name
    #     self.skills = skills
    #     self.money = money

    def __init__(self,name,money = 0):
        self.name = name
        # 每次创建一个新列表
        self.skills = []
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def skills(self):
        return self.__skills

    @skills.setter
    def skills(self,value):
        self.__skills = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self,value):
        self.__money = value

    # 张三 教 李四 学王者荣耀。
    def teach(self,person_other,str_skill):

        person_other.skills.append(str_skill)
        print(self.name + "教"+person_other.name + str_skill)

    # 李四工作挣了5000元钱
    def work(self,money):
        self.money += money
        print("%s上班,挣了%d钱"%(self.name,money))



# 张三 教 李四 学王者荣耀。
zs = Person("张三")
ls = Person("李四")
# zs.teach(zs,"王者荣耀")

zs.teach(ls,"王者荣耀")

# 李四 教 张三 学Python
# ls.teach(ls,"python")
ls.teach(zs,"python")

# 李四 上班赚了 5000元钱
ls.work(5000)
# 最后输出张三具有的技能，李四具有的技能，以及他们的钱。

print(zs.skills,zs.money)
print(ls.skills,ls.money)








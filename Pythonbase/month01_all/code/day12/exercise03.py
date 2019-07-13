"""
    练习：小明在招商银行取钱。
"""

class Person:
    def __init__(self,name,money):
        self.name = name
        self.money = money


class Bank:
    def __init__(self,name,money):
        self.name = name
        self.total_money = money

    def draw_money(self,value,person):
        if self.total_money >= value:
            self.total_money -= value
            person.money += value
        else:
            raise  ValueError("没钱啦")


xm = Person("小明",0)
bank = Bank("招商银行",100000)
bank.draw_money(1000,xm)

print("取完钱之后的小明：",xm.money)
print("取完钱之后的银行：",bank.total_money)





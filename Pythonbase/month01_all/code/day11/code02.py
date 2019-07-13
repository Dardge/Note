"""
    类成员
"""

class ICBC:
    # 类变量：类的,被所有对象共享的数据。
    moneys = 10000000
    # classmethod 指的是类方法
    @classmethod
    def get_total_moneys(cls):
        # cls 指的是调用当前方法的类
        print(cls.moneys)

    def __init__(self,name,money):
        # 实例变量：对象的
        self.name = name
        self.money = money
        # 从总行中扣除当前支行消耗的钱
        ICBC.moneys -= money

i01 = ICBC("广渠门支行",100000)
ICBC.get_total_moneys()
i02 = ICBC("中关村支行",200000)
ICBC.get_total_moneys()











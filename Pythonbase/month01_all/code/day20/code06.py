"""
    函数内部 定义函数
"""

# 压岁钱
def give_gift_money(money):
    print("获得%d压岁钱"%money)

    def child_buy(target,price):
        nonlocal money
        if money >= price:
            money -= price
            print("购买%s成功,剩余%d钱。"%(target,money))
        else:
            print("压岁钱花完啦")

    # 返回内部方法(此时没有调用内部方法)
    return child_buy
    # child_buy()

cb = give_gift_money(10000)


cb("九阳神功",9000)
# cb("乾坤大挪移",9000)
cb("一阳指",500)
cb("一阳指",500)
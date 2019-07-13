"""
    在控制台中购买彩票
	一注彩票：7个球(整数)
	6个红球：1 --- 33  【不能重复】
	1个蓝球：1 – 16
"""

ticket = []
# 输入6个红球
while len(ticket) < 6:
    number = int(input("请输入第%d红球号码：" % (len(ticket) + 1)))
    if number < 1 or number > 33:
        print("不在范围内")
    elif number in ticket:
        print("号码已经存在")
    else:
        ticket.append(number)
ticket.sort()

while True:
    number = int(input("请输入蓝球号码："))
    if 1 <= number <= 16:
        ticket.append(number)
        break
    else:
        print("输入有误")

print(ticket)

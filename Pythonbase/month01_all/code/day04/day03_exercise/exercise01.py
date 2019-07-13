"""
输入一个季度，打印该季度的月份。
"""
season = input("请输入季度：")
if season == "春天":
    print("１，２，３月")
elif season == "夏天":
    print("４，５，６月")
elif season == "秋天":
    print("７，８，９月")
elif season == "冬天":
    print("１０，１１，１２月")
else:
    print("输入有误")

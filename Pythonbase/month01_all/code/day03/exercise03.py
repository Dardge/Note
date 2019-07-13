"""
    练习３：输入月份，返回天数
    2 月 28天　　　１　３　５　７　８　１０　１２　月３１
    4  6  9  11 月　３０天
"""
month = int(input("请输入月份："))
if 1 <= month <= 12:
    if month == 2:
        print("28天")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("30天")
    else:
        print("３１天")
else:
    print("输入有误")

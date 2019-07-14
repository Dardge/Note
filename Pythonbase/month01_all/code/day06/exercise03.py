"""
    # 练习2：输入月份，显示天数。
"""
# month = int(input("请输入月份："))
# if 1 <= month <= 12:
#     if month == 2:
#         print("28天")
#     # elif month == 4 or month == 6 or month == 9 or month == 11:
#     elif month in (4,6,9,11):
#         print("30天")
#     else:
#         print("３１天")
# else:
#     print("输入有误")


month = int(input("请输入月份："))
if 1 <= month <= 12:
    day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    print(day_of_month[month-1])
else:
    print("输入有误")

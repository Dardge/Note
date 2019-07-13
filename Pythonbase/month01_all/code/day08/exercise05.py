"""
练习：定义方法，根据月份，返回天数。  16:20
     2月的闰年 29天    平年 28天
"""
# def get_day_by_month(year,month):
#     if month<1 or month >12:
#         return 0
#
#     if month == 2:
#         if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
#             return 29
#         else:
#             return  28
#
#     if month in (4,6,9,11):
#         return  30
#
#     return 31

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def get_day_by_month(year, month):
    if month < 1 or month > 12:
        return 0
    if month == 2:
        # if is_leap_year(year):
        #     return 29
        # else:
        #     return 28
        return  29 if is_leap_year(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


print(get_day_by_month(2000,2))
# 练习：定义函数，将列表中0元素，移动到末尾。[2,0,2,0]   -->  [2,2,0,0]
# [0,4,2,0]   -->  [4,2,0,0]   17:10






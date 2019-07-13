"""
    元组练习1：在控制台中输入月，日，计算是这一年的第几天。
    例如：3月5日
         1月31天    2月28天   5天
    提示：将每月的天数，存在元组中.
    （31,28,31，..........）

    元组应用1：字符串格式化
            "..%static..%d.." % (变量1，变量2)
    变量交换：
           a,b = b,a
"""
month = int(input("请输入月："))
day = int(input("请输入日："))
# 使用元组存储每月天数
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

# # 累加前几个月的天数
# total_day = 0
# for i in range(month-1):
#     total_day += day_of_month[i]

# 通过切片获取前几个月的天数，再利用内建函数sum求和
total_day = sum(day_of_month[:month - 1])
# 累加当月天数
total_day += day
print(total_day)

# 例如：3月
# 取出前两个元素
# 0 1
# for i in range(2):

# 例如：5月
# 取出前四个元素
# 0 1 2 3
# for i in range(4):


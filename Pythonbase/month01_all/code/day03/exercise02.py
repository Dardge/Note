"""
练习２：在控制台中获取一个月份，
    　　打印春(１--3)　夏(4--6)　秋(7--9)　冬(10--12)	　
"""
month = int(input("请输入月份："))

# 不建议 if month >= 1 and month <= 3:
# if 1 <= month <= 3:
#     print("春天")
# elif 4 <= month <= 6:
#     print("夏天")
# elif 7 <= month <= 9:
#     print("秋天")
# elif 10 <= month <= 12:
#     print("冬天")
# else:
#     print("输入有无")

# 上一个条件不满足，才判断下一个条件。
if 1 <= month <= 12:
    if month <= 3:
        print("春天")
    elif month <= 6:
        print("夏天")
    elif month <= 9:
        print("秋天")
    else:
        print("冬天")
else:
    print("输入有误")










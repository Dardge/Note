"""
    判断闰年，如果是闰年输出29天，
	否则输出28天。
"""

year = 2000
day = None
# if year %  4 == 0  and year %  100 != 0 or year % 400 ==0:
if not year % 4 and year % 100 or not year % 400:
    day = 29
else:
    day = 28

day = 29 if not year % 4 and year % 100 or not year % 400 else 28


x = None
if False:
    x = 10 # 满足条件赋值
else:
    x = 20 # 不满足条件赋值

# 条件表达式：有选择性的为变量进行赋值
# 变量 = 满足条件的结果 if 条件 else 不满足条件的结果
y = "yes" if False else "no"
print(x,y) # no











"""
     3.	在控制台中输入总秒数，计算几小时零几分钟零几秒钟。
"""
total_second = int(input("请输入秒数："))
# second 除以　60   商是分钟　余数是秒
s = total_second % 60
m = total_second // 60 % 60
h = total_second // 60 // 60
print(h, m, s)
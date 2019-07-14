"""
    小时／分钟／秒　　－－> 总秒数
"""
str_hour = input("请输入小时数：")
hour = int(str_hour)

minute = int(input("请输入分钟数："))

second = int(input("请输入秒数："))

result = hour * 3600 + minute * 60 + second
print(result)

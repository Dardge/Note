"""
    练习１：在控制台中获取两个整数，作为循环开始和结束的点。
    5(包括)        10(包括)
"""
begin = int(input("请输入开始数："))
end = int(input("请输入结束数："))

# 包含
while begin < end:
    print(begin)
    begin +=1

# 不包含
# while begin < end-1:
#     begin +=1
#     print(begin)

# 16:12 上课







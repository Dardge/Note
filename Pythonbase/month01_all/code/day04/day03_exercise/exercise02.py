"""
一个球从100m的高度落下，
每次弹回原高度的一半。
计算：
1. 总共经过？次最终落地(可以弹起的最小高度0.01m)。
2. 记录总共经过？米。
"""

hight = 100
count = 0
# 记录初始１００米的距离
distance = hight
# 如果可以弹起　则执行循环体
while hight / 2 >= 0.01:
    # 弹起
    hight /= 2
    count += 1
    #　累加当前弹起高度
    distance += hight * 2
    print(count, hight)
print("总共弹起次数:",count)
print("总共经过距离:",round(distance))















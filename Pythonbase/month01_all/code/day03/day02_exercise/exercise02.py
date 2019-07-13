"""
 2.	在控制台中获取圆形的半径，
    输出面积(3.14 * r 的平方)与周长(2 * 3.14 * r)
"""

radius = int(input("请输入半径："))
area = 3.14 * radius ** 2
# length = 2 * 3.14 * radius
length = round(2 * 3.14 * radius,2)
result = "周长是:" + str(length) + ",面积是：" + str(area) + "."
print(result)

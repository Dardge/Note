"""
练习3：在控制台中循环输入整数，存入列表，当输入-1时退出。
		要求：整数不能相同。
        计算：最大值、最小值。第二个最大值
"""

list_number = []
while True:
    number = int(input("请输入整数："))
    if number == -1:
        break
    # 判读列表中是否存在number
    if number not in list_number:
        list_number.append(number)
    else:
        print("已经存在")

print("最大值：", max(list_number))
print("最小值：", min(list_number))
# 从小到大    升序排列
list_number.sort()  # 修改原列表
list_number02 = list_number[::-1]  # 倒叙列表（不修改原列表，生成新列表）

print(list_number)
print("第二个最大的：", list_number[-2], list_number02)

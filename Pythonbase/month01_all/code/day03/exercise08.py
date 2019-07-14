"""
    练习３：猜数字游戏1.0 版本
    让用户在控制台中重复猜测。如果没有猜对，提示：大了，小了。
    如果猜对了，提示正确，并显示猜了多少次。
    猜数字游戏２.0 版本
    最多只能猜６次。
"""
import random
# 生成随机数(包含两端)
random_number = random.randint(1, 100)

count = 0
# while True:
#     count+=1z
#     input_number = int(input("请输入："))
#     if input_number > random_number:
#         print("大了")
#     elif input_number < random_number:
#         print("小了")
#     else:
#         print("正确，猜了"+str(count)+"次")
#         break

while count < 10:
    count+=1
    input_number = int(input("请输入："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("正确，猜了"+str(count)+"次")
        break
else:
    # 如果执行ｂｒｅａｃｋ语句，不会进入ｅｌｓｅ语句。
    print("没机会了")










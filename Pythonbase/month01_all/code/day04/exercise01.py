"""
    在控制台中输入一个整数，判断是否为素数。
"""
number = int(input("请输入整数："))# 9
if number < 2:
    print("不是素数")
else:
    # 依次生成２　　－－－　number - 1 之间的整数
    for i in range(2, number):# 2 3 4 5 6 7 8
        if number % i == 0:# 9  %  3
            print("不是素数")
            # 如果有了结论，后续数字不用再判断
            break
    else:
        print("是素数")
        # 没有执行ｂｒｅａｋ





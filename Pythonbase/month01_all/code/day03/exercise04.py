"""
    在可控制台中获取一个整数
    打印奇数或者偶数
"""
number = int(input("请输入整数："))

# if number % 2 ==1:
if number % 2:  # bool(number % 2)
    print("奇数")
else:
    print("偶数")

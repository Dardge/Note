"""
    在控制台中获取一个4位整数，
		计算每位相加和。
"""

number = int(input("输入４位整数"))
unit01 = number % 10  # 个位
unit02 = number // 10 % 10  # 十位　1234 // 10 --> 123
unit03 = number // 100 % 10  # 百位　1234 //100 ->12
unit04 = number // 1000 + "a"
result = unit01 + unit02 + unit03 + unit04
print(result)
# 调试
# 1.	加断点(程序运行到本行停止，没有执行本行)
# 2.	开始调试shift+alt+f9
# 3.	逐行执行 F7
# 4.	停止调试ctrl + f2

"""
练习3：在控制台中输入一个整数，打印一个矩形。
		例如：4
 		****
		*  *
        *  *
        ****
提示：* 乘以 4
	   中间输出4 - 2空格
"""
# number = int(input("请输入："))
number = 4

# 输出头
print("*" * number)
# 输出中间部分
for i in range(number - 2):
    print("*" + " " * (number - 2) + "*")
# 输出尾
if number > 1:
    print("*" * number)








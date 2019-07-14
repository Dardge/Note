"""
    编码练习
"""

# １．在控制台中输入一个字符串，打印该字符串的每个字符编码。
str_input = input("请输入字符：")
for item in str_input:
    print(ord(item))


# ２．循环输入编码值，显示字符。　待输入负数时，退出。
while True:
    number = int(input("请输入编码值："))
    if number < 0:
        break
    print(chr(number))
# 15:24 上课













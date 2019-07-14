"""
练习2：输入一个字符串，打印如下内容。
(1)	打印字符串第一个字符
(2)	打印字符串最后一个字符串
(3)	如果长度是奇数，则打印字符串中间的字符串
len(字符串) 返回长度
"""

# str_input=input("请输入：")
str_input = "abcde"
# (1)	打印字符串第一个字符
print(str_input[0])
# (2)	打印字符串最后一个字符串
print(str_input[-1])
print(str_input[len(str_input) - 1])
# (3)	如果长度是奇数
if len(str_input) % 2 == 1:
    print(str_input[len(str_input)//2])





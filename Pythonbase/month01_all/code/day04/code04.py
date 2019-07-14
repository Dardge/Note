"""
    字符串常用操作
"""

# 数学运算符
# 拼接
str01 ="孙悟空" + "孙大圣"
# 重复生成字符串
print(str01 *2)
# +=    *=
# 比较运算：比较编码值
str02 = "abc"
str03 = "aaD"
print(str02 > str03)

str01 = "abcdef"
print(str01[1:4]) #bcd
print(str01[0:5]) #abcde
print(str01[:5]) #abcde
print(str01[:]) #abcdef
print(str01[1:1]) #空
print(str01[4:2]) #空
print(str01[:5:2]) #空ace
print(str01[::-1]) #fedcba
print(str01[-2:-5:-1]) #edc
print(str01[:-5:-1]) #fedc
print(str01[-2::-1]) #edcba
print(str01[-2:])# ef
















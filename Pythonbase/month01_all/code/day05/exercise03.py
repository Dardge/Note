"""
练习1：在控制台中循环输入字符串，待输入q时退出。
      显示一个新的字符串。
"""

list_result = []
while True:
    str_input = input("请输入：")
    if str_input =="q":
        break
    list_result.append(str_input)

str_result = "+".join(list_result)
print(str_result)
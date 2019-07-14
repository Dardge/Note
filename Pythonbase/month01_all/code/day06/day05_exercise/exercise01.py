"""
作业1：单词反转
”How are you”  --> “you are How”
"""

str01 = "How are you"
list_result = str01.split(" ")
# # 将列表进行反转
# list_result.reverse()
# str_result  =" ".join(list_result)
# print(str_result)

# 通过切片反转列表，只是获取了一个新列表，并没有改变原有列表

str_result  =" ".join(list_result[::-1])
print(str_result)












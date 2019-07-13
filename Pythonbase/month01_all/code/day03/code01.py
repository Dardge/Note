"""
    选择语句　if  else
"""

sex = input("请输入性别：")
# # 如果满足条件
# if sex == "男":
#     print("您好，先生")
# # 否则(不满足条件执行)
# else:
#     print("您好，女士")

# 如果满足条件
if sex == "男":
    print("您好，先生")
# 否则　如果满足条件
elif sex == "女":
    print("您好，女士")
else:
    print("性别未知")

# [错误]如果男的
# if sex == "男":
#     print("您好，先生")
# # 如果女的
# if sex == "女":
#     print("您好，女士")
# # 否则
# else:
#     print("性别未知")






"""
    for   range
"""

for item in "我爱python":
    print(item)

for i in range(10):
    print(i)


#  5 4  3   2   1  0
for i in range(5,-1,-1):
    print(i)

# 练习1：累加１(包含)　－－　１００(包含)之间的整数
# 练习2：累加１(包含)　－－　１００(包含)之间的偶数
#
# sum = 0
# for i in range(1,101):
#     if i % 2 == 0:
#        sum += i
# print(sum)

sum = 0
for i in range(1,101):
    # 如果是偶数　则累加
    # if i % 2 == 0:
    # 如果是奇数则跳过
    if i % 2 != 0:
        continue
    sum += i
print(sum) # 2550

























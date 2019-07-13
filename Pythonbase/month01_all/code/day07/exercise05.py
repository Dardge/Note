"""
    for  for 嵌套
    16:40 上课
"""
# ****
# 外层循环控制行
for r in range(3):  # 0  1  2
    # 内层循环控制列
    for c in range(4):  # 0123    0123    0123
        print("*", end="")
    print()  # 换行

print("---------------------------------------")
"""
练习1：  4行    5列
*****
#####
*****
#####
"""
for r in range(4):
    # 内层循环控制列
    for c in range(5):
        if r % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
    print()  # 换行
print("---------------------------------------")
"""
练习2:4行   0      1       2      3
*          0
**                01
***                       012
****                            0123 
"""
for r in range(4):  #
    for c in range(r + 1):  # 01
        print("*", end="")
    print()
"""
练习3:
****    空格0个   星号4个
 ***        1        3
  **        2        2
   *        3        1
17:32 
"""
print("---------------------------------------")
for r in range(4):  # 0      1     2     3
    for c in range(r):  # 0     01
        print(" ", end="")
    for c in range(4 - r):  # 0123    012   01    0
        print("*", end="")
    print()

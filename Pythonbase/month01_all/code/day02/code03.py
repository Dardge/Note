"""
    算数运算符
"""

# 算数运算符
num01 = 6
num02 = 2
# ／　结果是ｆｌｏａｔ类型
re01 = num01 / num02
print(re01) # 2.5
# //　商向下取整数
re01 = num01 // num02
print(re01) # 2
# ％　取余数
re01 = num01 % num02
print(re01) # 1
# 作用１：一个数能否被另外一个数整除
# num01  num02
re01 = num01 % num02  ==  0
print(re01)
# 作用２：求整数的个位
num03 = 15
re01 = num03 % 10
print(re01)  # 5
re01 = num03 // 10
print(re01) # 1

# 5 * 5
print( 5 ** 2) # 25
# 5 * 5 * 5
print( 5 ** 3) # 125










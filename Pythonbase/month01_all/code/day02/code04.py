"""
    增强运算符
"""

a = 5
b = a + 1
print(a) # 5
# a = a + 1 # 6
a += 1

# 累加　个位　十位　百位　．．．
number = int(input("输入４位整数"))
result = number % 10 # 个位
result += number // 10 % 10 # 十位　1234 // 10 --> 123
result += number // 100 % 10  # 百位　1234 //100 ->12
result +=  number // 1000

print(result)









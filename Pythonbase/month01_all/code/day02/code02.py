"""
    数据类型
"""

# 1. 整形
# 二进制　0 1 2 3 4
print(0b0,0b1,0b10,0b11, 0b100)
# 八进制　0 7 8 9
print(0o0,0o7,0o10,0o11)
# 十六进制　0 10 161
print(0x0,0xa,0xa1)

# ２. 浮点型
# 1.5 --> 150.0
print(1.5e2)
# 1.5 -->0.015
print(1.5e-2)

# 3. 字符串
str01 = '我爱python'
str01 = "我爱python"
str01 = '''我爱python'''
str01 = """我爱python"""

# 类型转换
a = 10
re1 = "变量是："+str(a)
t1 = type(a)
t2 = type(re1)
print(t1,t2)

print(re1)















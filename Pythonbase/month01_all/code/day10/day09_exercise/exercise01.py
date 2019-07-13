"""
    定义数值累加函数。
"""
def numbers_add(*args):
    return sum(args)


print(numbers_add(1,2,3))
print(numbers_add(1,2))
print(numbers_add(1,2,3,2,4,56,78))
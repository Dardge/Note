"""
扩展作业：定义方法，计算指定范围内的素数。
		1  -- 100
"""

def is_prime(number):
    if number < 2:
        return  False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        else:
            return True

def get_prime(begin,end):
    # result = []
    # for number in range(begin,end):
    #    if  is_prime(number):
    #        result.append(number)
    return [number for number in range(begin,end) if  is_prime(number)]


print(get_prime(1,100))
print(get_prime(6,20))










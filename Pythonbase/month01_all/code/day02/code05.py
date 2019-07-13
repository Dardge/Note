"""
    逻辑运算符
    与(并且)　　或(或者)　　非(not)
"""

# 一假俱假
re = True and  True # True
re = False and  True # False
re = True and  False # False
re = False and False # False

# 一真则真
re = True  or True # True
re = False or  True # True
re = True  or False # True
re = False or False # False

# 取反
re = True
re = not re
print(re) # False


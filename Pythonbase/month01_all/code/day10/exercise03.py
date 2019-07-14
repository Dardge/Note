"""
    画图
    可变类型传参2.0
"""

def fun3(a,b):
    # a[0] = 100
    a = [100]
    b = {"b",200}


list02 = [1]
dict02 = {"a":1}
fun3(list02,dict02)
print(list02,dict02)
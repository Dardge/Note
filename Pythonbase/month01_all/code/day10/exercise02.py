"""
    画图
    可变类型传参1.0
"""

def fun2(a,b):
    a[0] = 100
    b["b"] = 200


list01 = [1]
dict01 = {"a":1}
fun2(list01,dict01)
print(list01,dict01)
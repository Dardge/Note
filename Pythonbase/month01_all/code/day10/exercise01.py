"""
    画图
    不可变类型传参
"""
def fun1(a,b,c,d,e):
    a = 100
    b = 1500
    c = False
    d = "ABC"
    e = (100,200)

g_a = 1
g_b = 1.5
g_c = True
g_d = "abc"
g_e = (10,20)

fun1(g_a,g_b,g_c,g_d,g_e)
print(g_a,g_b,g_c,g_d,g_e)



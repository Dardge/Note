"""
    元组 基础操作
"""

# 1. 创建空元组
t01 = ()
t01 = tuple()
# 2. 创建具有默认值的元组
t01 = (1, 2, 3)
t03 = 1, 2, 3
print(t03)
t01 = tuple("abc")

t02 = (1,2,[3,4])
print(t01)

# 3. 元组的元素不能修改
# t01[0] = 1  错误
# 修改的是列表元素
t02[2][0] = "a"
print(t02)

# 4. 获取
t03 = (1,2,3,4,5)
# 通过索引
print(t03[0])
# 通过切片
print(t03[1:-1])
# 获取每个元素
for item in t03:
    print(item)
# 根据索引获取元素
for i in range(0,len(t03),2):
    print(t03[i])

t04 = ("a","b","c")
t05 = t04
t04 += (1,2) # 产生新元组对象，并绑定t04
print(t05) # ('a', 'b', 'c')
print(t04) # ('a', 'b', 'c', 1, 2)

list04 = ["a","b","c"]
list05 = list04
list04 +=[1,2]  # 在原有列表中添加元素
print(list05) # ['a', 'b', 'c', 1, 2]
print(list04) # ['a', 'b', 'c', 1, 2]












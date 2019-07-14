"""
    迭代器 -- 使用
"""

list01 = [1,2133,345,5,6]
# for item in list01:
#     print(item)


# for 循环原理：
#  1. 获取迭代器对象
#  2. 循环获取下一个元素
#  3. 遇到StopIteration停止迭代

# 可以被for的条件（什么是可迭代对象）：
# 可以获取迭代器对象(具有__iter__方法)


"""
#1. 获取迭代器对象
iterator =  list01.__iter__()
#2. 获取下一个元素
item = iterator.__next__()
print(item)
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
#3. 直到错误 StopIteration 停止
print(iterator.__next__()) 
"""
iterator =  list01.__iter__()
while True:
    try:
        print(iterator.__next__())
    except StopIteration:
        break # 跳出循环

#练习1：("悟空","八戒","唐僧","沙僧","女儿国国王")
# 使用while + 迭代器 获取元组所有元素
tuple01 = ("悟空","八戒","唐僧","沙僧","女儿国国王")
iterator01 = tuple01.__iter__()
while True:
    try:
        print(iterator01.__next__())
    except:
        break


#练习2：{"悟空":2000,"八戒":3000,"唐僧":1000,"沙僧":2800}
# 不使用for，获取字典所有元素
dict01 = {"悟空":2000,"八戒":3000,"唐僧":1000,"沙僧":2800}
iterator02 = dict01.__iter__()
while True:
    try:
        key = iterator02.__next__()
        value = dict01[key]
        print(key,value)
    except:
        break








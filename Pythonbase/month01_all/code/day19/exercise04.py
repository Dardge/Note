"""
    # 练习：my_zip
    # zip：将多个可迭代对象的元素组合成一个个元组。  16:45
    list02 = ["A", "B", "C"]
    for item in zip(list01, list02):
        print(item)
"""

def my_zip(target01,target02):# *args
    for i in range(len(target01)):
        yield (target01[i],target02[i])

list01 = ["a", "b", "c"]
list02 = ["A", "B", "C"]

for item in my_zip(list01, list02):
    print(item)

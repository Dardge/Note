"""
作业1：实现两个列表元素的全排列
[“香蕉”,”苹果”,”哈密瓜”, ”草莓”]
[“牛奶”,”咖啡”,”雪碧”]
"""
list01 = ["香蕉","苹果","哈密瓜", "草莓"]
list02 = ["牛奶","咖啡","雪碧"]
result01 = []

for r in list01:
    for c in list02:
        result01.append(r + c)

result02 = [r + c for r in list01 for c in list02]
print(result01)
print(result02)


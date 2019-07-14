"""
    练习:定义list排序的方法,升序  14:16
    取出前几个元素
        依次与后面的元素进行比较
            如果 前面的元素 >  后面的元素
                交换
"""

"""
def order_by(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] > list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]
    return  list_target

list01 = [2, 8, 6, 1]
print(order_by(list01))
"""

def order_by(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] > list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]

list01 = [2, 8, 6, 1]
# 对于可变类型对象,无需通过返回值,返回结果.(前提,修改对象,而不是修改变量)
order_by(list01)
print(list01)

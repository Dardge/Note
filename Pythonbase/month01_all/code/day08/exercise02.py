# 练习1：定义判断列表是否具有相同元素的函数 14:30
def is_repeating(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r+1,len(list_target)):
            if list_target[r] == list_target[c]:
                return True
    return False

state = is_repeating([1,2,1,6])
if state:
    print("具有相同元素")
else:
    print("没有相同元素")

print(is_repeating([3,434,5,7]))










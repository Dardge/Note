"""
扩展作业:设计一个算法，判断列表中是否具有相同元素。
  	  [1,4,7,5,1,9,8]

  	核心思想：
        取出前几个元素（不要最后一个）
            依次与后面比较

    重点：列表中两两元素进行比较
"""
list01 = [1,4,7,5,2,9,8]

# 假设没有相同元素
state = False
# 取出元素
for r in range(len(list01) - 1):
    # 作比较
    # r + 1  取出元素的下一个元素索引
    for c in range(r+1,len(list01)):
        if list01[r] == list01[c]:
            state = True

if state:
    print("具有相同元素")
else:
    print("没有相同元素")











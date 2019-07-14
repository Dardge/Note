list01 = ["a", "b", "c"]
list02 = ["A", "B", "C"]

result = []
for r in list01:
    for c in list02:
        result.append(r + c)

print(result)

result = [r + c for r in list01 for c in list02]
print(result)

# 练习：列表中元素，两两组合，找出所有组合
list = [1, 2, 3, 4, 5, 6]

# for i in list:
#     for c in list:
#         new_list.append(str(i) + str(c))
new_list = [str(i) + str(c) for i in list for c in list]  # 列表推导式
new_list = [i for i in new_list if i not in ['11', '22', '33', '44', '55', '66']]
print(new_list)

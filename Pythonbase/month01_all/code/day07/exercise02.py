# 练习2：房间号码：[101,102,103]
#       房客姓名：["zs","ls","ww"]
#       合二为一：{101:"zs",102:"ls",103:"ww"}

list01 = [101, 102, 103]
list02 = ["zs", "ls", "ww"]
# result = {}
# for i in range(len(list01)):  # 0  1 2
#     result[list01[i]] = list02[i]
# print(result)

# result02 = {list01[i]: list02[i] for i in range(len(list01))}
# print(result02)

b = 1
a = [(b+i,b+i+1) for i in range(1, 7, 3)]
c = [{b+i:b+i+1} for i in range(1, 7, 3)]
print(a,c)

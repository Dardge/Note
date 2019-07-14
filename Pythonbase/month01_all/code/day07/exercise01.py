# 练习1：有一个字符串列表 ["zs","wlw","tarena"]
#       生成字典:{"zs":2,"wlw":3,"tarena":6}
list01 = ["zs", "wlw", "tarena"]
result01 = {}
for item in list01:
    result01[item] = len(item)

result02 = {item: len(item) for item in list01}
print(result02)
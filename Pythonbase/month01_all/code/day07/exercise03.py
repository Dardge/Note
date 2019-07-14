"""
    集合练习1：在控制台中循环输入内容.如果录入空字符串，则退出。
             统计输入次数，打印不重复的内容。
             “a"  "b"   "a"
             3次    a   b  a
"""
set01 = set()
count = 0
while True:
    str_input = input("请输入：")
    # if not str_input:
    if str_input == "":
        break
    set01.add(str_input)
    count += 1
print("总共输入：%d次" % (count))
for item in set01:
    print(item)

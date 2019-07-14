"""
作业2：在控制台中录入学生信息name,age,score
	   将每个学生输出到控制台(一个学生一行)
数据结构：
[
    {
        “name”:”zs”,
        ”age”:25,
        ”score”:100,
    },
    {
        “name”:”ls”,
        ”age”:35,
        ”score”:80,
    }
 ]
"""
# 1,录入信息
list_student_info = []
while True:
    dict_student_info = {}
    dict_student_info["name"] = input("请输入姓名:")
    dict_student_info["age"] = int(input("请输入年龄:"))
    dict_student_info["score"] = int(input("请输入成绩:"))
    list_student_info.append(dict_student_info)
    if input("按y继续：") != "y":
        break

# 2,读取信息
# 遍历列表
for dict_student in list_student_info:
    # 遍历字典
    for key,value in dict_student.items():
            print("%s--%s"%(key,value),end = "#")
    print()









"""
    练习2：在控制台中录入学生成绩
	  先输入：学生总数
      再依次录入成绩。
	  计算总分
"""
# 提示输入学生总数：
count = int(input("请输入学生总数："))

stu_list = []
# 循环预定次数，完成成绩录入
for i in range(count):
    score = int(input("请输入成绩："))
    stu_list.append(score)

sum_value = 0
for item in stu_list:
    sum_value += item

print("总分：", sum_value)
print("总分：", sum(stu_list))
print("最高分：", max(stu_list))
print("最低分：", min(stu_list))












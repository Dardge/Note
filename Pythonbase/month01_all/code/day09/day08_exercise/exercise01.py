"""
作业4：定义方法,根据成绩判断等级。
       0---100   优秀  良好  及格  不及格
"""


def get_score_level(int_score):
    if int_score < 0 or int_score > 100:
        return None
    if int_score < 60:
        return "不及格"
    if int_score < 70:
        return "及格"
    if int_score < 80:
        return "良好"
    return "优秀"


print(get_score_level(100))

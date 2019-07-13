# 练习2：定义方法，根据月份返回季度。14:57
# def get_season(month):
#     if 1 <= month <= 12:
#         if month <= 3:
#             return "春天"
#         elif month <= 6:
#             return "夏天"
#         elif month <= 9:
#             return "秋天"
#         else:
#             return "冬天"
#     else:
#         return None
#15:35 上课
def get_season(month):
    if  month <1 or month > 12:
        return None

    if month <= 3:
        return "春天"
    if month <= 6:
        return "夏天"
    if month <= 9:
        return "秋天"

    return "冬天"

print(get_season(12))
print("结束")





"""
    练习：根据天/分钟/小时，计算总秒数。
    16:52 上课
"""


def get_total_second(day=0, hour=0, minute=0):
    return day * 24 * 60 * 60 + hour * 60 * 60 + minute * 60


print(get_total_second(1, 1, 1))
# 1 天
print(get_total_second(1))
# 1 小时
print(get_total_second(hour=1))
# 1 分钟
print(get_total_second(minute=1))
# 1 分钟
print(get_total_second(0, 0, 1))

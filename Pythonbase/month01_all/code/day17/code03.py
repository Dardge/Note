"""
    时间模块
"""

import time
# 1. 时间戳 (1970年后到当前经过的秒数)
# 1553073239.4967241
print(time.time())
# 2. 时间元组(年份 月份 日 小时 分钟 秒  一周的第几天 一年中的第几天  夏令时  )
# 时间戳  -->  时间元组
print(time.localtime(1553073239))
# 3. 时间元组 -->  时间戳
t01 = time.localtime(1553073239)
print(time.mktime(t01))
# 4.  格式化时间元组（时间元组 -- > 字符串）
print(time.strftime("%y   %m   %d   %H  %M   %S",time.localtime()))
# 5. 字符串 --> 时间元组
print(time.strptime("2019/03/20 17:32","%Y/%m/%d %H:%M"))

















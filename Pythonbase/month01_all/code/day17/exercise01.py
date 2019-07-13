"""
  练习:定义方法，根据年月日，计算星期。17:45
"""

import time

def get_week(year,month,day):
    # 时间元组
    time_tuple  = time.strptime("%d/%d/%d"%(year,month,day),"%Y/%m/%d")
    # if  time_tuple[6] == 0:
    #     return "星期一"
    # if  time_tuple[6] == 1:
    #     return "星期二"
    # ...
    # weeks = {
    #     0:"星期一",
    #     1:"星期二",
    # }
    # return weeks[time_tuple[6]]
    weeks = ("星期一","星期二","星期三","星期四","星期五","星期六","星期日")
    return weeks[time_tuple[6]]

print(get_week(2019,3,19))
"""
    技能(编号、名称、法力消耗、冷却时间)
    1.	查找指定编号的技能
    2.	查找法力消耗大于10的所有技能
    -----------------------------------------------------------
    3.	查找技能冷却时间最小的技能
    4.	根据法力消耗降序排列
    5.	删除冷却时间大于10的技能
"""
from common.list_tools import ListHelper

class SkillData:

    def __init__(self, id=0, name="", cost_sp=0, cool_time=0):
        self.id = id
        self.name = name
        self.cost_sp = cost_sp
        self.cool_time = cool_time

    def __repr__(self):
        return "SkillData(%d,'%s',%d,%d)"%(self.id,self.name,self.cost_sp,self.cool_time)

skills = [
    SkillData(101,"乾坤大挪移",50,5),
    SkillData(102,"天下无狗",10,10),
    SkillData(103,"凌波微步",5,0),
    SkillData(104,"如来神掌",70,60),
]
# 1.查找指定编号的技能
# print(ListHelper.first(skills,lambda e:e.id == 103))
# 2.查找法力消耗大于10的所有技能
# for item in ListHelper.find_all(skills,lambda e:e.cost_sp > 10):
#     print(item)
# 3.查找技能冷却时间最小的技能
# print(ListHelper.get_min(skills,lambda e:e.cool_time))

# 4.根据法力消耗降序排列
# ListHelper.order_by_descending(skills,lambda e:e.cost_sp)
# for item in skills:
#     print(item)

# 5.删除冷却时间大于10的技能
print(ListHelper.delete_all(skills,lambda e:e.cool_time > 0))
for item in skills:
    print(item)


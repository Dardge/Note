class SkillData:
    def __init__(self, id=0, name="", cost_sp=0, cool_time=0):
        self.id = id
        self.name = name
        self.cost_sp = cost_sp
        self.cool_time = cool_time

    @property
    def cool_time(self):
        return self.__cool_time

    @cool_time.setter
    def cool_time(self, value):
        self.__cool_time = value

    @property
    def cost_sp(self):
        return self.__cost_sp

    @cost_sp.setter
    def cost_sp(self, value):
        self.__cost_sp = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def print_self(self):
        print(self.id, self.name, self.cost_sp, self.cool_time)


# 作业1：在技能数据列表中，查找指定名称的技能对象。
def get_skill_by_name(list_skill, skill_name):
    for item in list_skill:
        if item.name == skill_name:
            return item


list_skill = [
    SkillData(101, "惩戒", 80, 30),
    SkillData(102, "闪现", 20, 2),
    SkillData(103, "点燃", 1, 80),
]


# skill = get_skill_by_name(list_skill,"闪现")
# skill.print_self()

# 作业2：查找冷却时间大于5的所有技能对象。
def get_skills_by_cool_time(list_skill, time):
    result = []
    for item in list_skill:
        if item.cool_time > time:
            result.append(item)
    return result

# result =get_skills_by_cool_time(list_skill,5)
# for item in result:
#     item.print_self()

# 作业3：查找技能数据列表中，消耗法力最小的技能。
def get_min_by_sp(list_skill):
    min = list_skill[0]
    for i in range(1, len(list_skill)):
        if min.cost_sp > list_skill[i].cost_sp:
            # min.cost_sp = list_skill[i].cost_sp
            min = list_skill[i]
    return min

# skill = get_min_by_sp(list_skill)
# skill.print_self()


# 作业4：查找技能数据列表中，冷却时间最大的技能。
def get_max_by_cool_time(list_skill):
    max = list_skill[0]
    for i in range(1, len(list_skill)):
        if max.cool_time < list_skill[i].cool_time:
            max = list_skill[i]
    return max


# 作业5：根据冷却时间，对技能列表进行升序(小到大)排列。
def order_by_cool_time(list_skill):
    for r in range(len(list_skill) - 1):
        for c in range(r + 1, len(list_skill)):
            if list_skill[r].cool_time > list_skill[c].cool_time:
                list_skill[r], list_skill[c] = list_skill[c], list_skill[r]














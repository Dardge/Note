"""
    定义技能数据类(技能编号，技能名称，消耗法力，冷却时间，动画名称)，
	    使用属性进行封装，使用__slots__。
"""


class SkillData:
    __slots__ = ("__id","__name","__cost_sp","__cool_time","__animation_name")

    def __init__(self, id=0, name="", cost_sp=0, cool_time=0, animation_name=""):
        self.id = id
        self.name = name
        self.cost_sp = cost_sp
        self.cool_time = cool_time
        self.animation_name = animation_name

    @property
    def animation_name(self):
        return self.__animation_name

    @animation_name.setter
    def animation_name(self, value):
        self.__animation_name = value

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


data01 = SkillData(101, "降龙十八掌")
data01.cost_sp = 80
data01.cool_time = 60
data01.animation_name = "anim01"
print(data01.id)
print(data01.name)

# data01.qtx = 100
# print(data01.qtx)









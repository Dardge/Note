"""
    迭代器
"""


class Skill:
    pass


class SkillIterator:
    """
        技能迭代器
    """

    def __init__(self, target):
        self.target = target
        self.index = 0

    # def __next__(self):
    #     item = self.target[self.index]
    #     self.index += 1
    #     return item

    def __next__(self):
        # 如果索引越界  则停止迭代
        if self.index >= len(self.target):
            raise StopIteration()

        item = self.target[self.index]
        self.index += 1
        return item


class SkillManager:
    def __init__(self, skills):
        self.skills = skills

    def __iter__(self):
        # 1. 创建迭代器对象
        # 2. 传递需要迭代的数据
        return SkillIterator(self.skills)


manager = SkillManager([Skill(), Skill(), Skill()])
# for item in manager:
#     print(item)


iterator = manager.__iter__()
# 使用迭代器获取manager中的技能列表
while True:
    try:
        item = iterator.__next__()
        print(item)
    except:
        break

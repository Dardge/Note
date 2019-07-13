"""
    迭代器 --> yield
"""


class Skill:
    pass


# class SkillIterator:
#
#     def __init__(self, target):
#         self.target = target
#         self.index = 0
#
#     def __next__(self):
#         # 如果索引越界  则停止迭代
#         if self.index >= len(self.target):
#             raise StopIteration()
#         item = self.target[self.index]
#         self.index += 1
#         return item


class SkillManager:
    def __init__(self, skills):
        self.skills = skills

    def __iter__(self):# 15:30 上课
        # SkillIterator(self.skills)
        # 本质：
        #     解释器检测到yield关键字，就会生成迭代器对象。
        # 自动生成迭代器的大致规则：
        #     1. yield 关键字以前的代码会放到__next__方法中
        #     2. yield 关键字后面的数据会作为__next__方法的返回值
        # 现象：
        #     调用当前方法时，不执行。
        #     当调用__next__方法时，才执行。
        #     执行到 yield 关键字，暂时离开。
        #     当再次调用__next__方法时，继续执行。
        #     执行到 yield 关键字，暂时离开。
        #     .....

        # print("我的第一次")
        # yield self.skills[0]
        #
        # print("我的第二次")
        # yield self.skills[1]
        #
        # print("我的第三次")
        # yield self.skills[2]

        for i in range(len(self.skills)):
            yield  self.skills[i]


manager = SkillManager([Skill(), Skill(), Skill()])
# for item in manager:
#     print(item)

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except Exception as e:
        print(type(e))
        break






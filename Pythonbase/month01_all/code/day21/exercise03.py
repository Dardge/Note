
class SkillData:

    def __init__(self, id=0, name="", cost_sp=0, cool_time=0):
        self.id = id
        self.name = name
        self.cost_sp = cost_sp
        self.cool_time = cool_time

    def __repr__(self):
        return "SkillData(%d,'%s',%d,%d)"%(self.id,self.name,self.cost_sp,self.cool_time)

s01 = SkillData(101,"乾坤大挪移",20,60)
# 将s01写入到文件中
def save_skill(skill_target):
    with open("file_demo/skill.txt","w",encoding="utf-8") as skill_file:
        skill_file.write(skill_target.__repr__())

# 将文件中存储的内容读取到程序中，再创建SkillData对象。
def load_skill(file_path):
    with open(file_path,"r",encoding="utf-8") as skill_file:
        # str_skill = skill_file.readline()
        # return eval(str_skill)
        for line in skill_file:
            yield eval(line)

# save_skill(s01)
# s02 = load_skill("file_demo/skill.txt")
# print(s02.id)
for item in load_skill("file_demo/skill.txt"):
    print(item)

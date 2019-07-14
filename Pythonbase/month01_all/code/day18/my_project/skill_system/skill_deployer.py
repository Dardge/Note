print("sKill_deployer 被导入")

# from skill_data import  SKillBaseData
from skill_system.skill_data import SKillBaseData

from common import *

class SKillDeployer:
    def deployer(self):
        print("释放技能")
        s01 =  SKillBaseData(101)
        print(s01.id)
        list_helper.ListHelper.find_all()
        double_list_helper.DoubleListHelper.get_elements()


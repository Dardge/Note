# from skill_system import skill_deployer
# s01 = skill_deployer.SKillDeployer()
# s01.deployer()

from skill_system.skill_deployer import SKillDeployer
# 创建对象
s01 = SKillDeployer()
# 调用实例方法
s01.deployer()

# from common import list_helper
# list_helper.ListHelper.find_all()

from common.list_helper import ListHelper
# 通过类名调用静态方法
ListHelper.find_all()

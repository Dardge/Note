"""
游戏：      石头    剪刀   布
在控制台中获取：0    1    2，代表石头剪刀布。
根据游戏规则，显示：平局、胜利、失败。
提示： import  random
      random.randint(0,2)
	  将胜利策略存入元组
	  (
          (“石头”,”剪刀”),
          (“剪刀,”布”),
          (“布”,”石头”)
	  )

核心思路：将用户输入的与系统生成的结果形成元组
        将所有胜利策略存入大元组
       （用户输入，系统生成）in 胜利策略
"""
import random

items = ("石头", "剪刀", "布")
# 胜利策略
wins = (
    ("石头", "剪刀"),
    ("剪刀", "布"),
    ("布", "石头")
)
# (1)系统生成的随机数 0  1  2
sys_input_index = random.randint(0, 2)
sys_input = items[sys_input_index]
# print(sys_input)  # 测试，打印电脑的随机出牌
# (2)用户输入的0 1 2
user_input_index = int(input("请输入:"))
user_input = items[user_input_index]
# (3)构建输入项 用于在胜利列表中查找
item_input = (user_input, sys_input)
if user_input == sys_input:  # (4) 逻辑处理
    print("平局")
elif item_input in wins:
    print("赢啦")
else:
    print("输啦")
# 练习：实现循环输入 胜利2次   或者   输了2次

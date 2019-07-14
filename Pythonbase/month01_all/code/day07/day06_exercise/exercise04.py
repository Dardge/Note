"""
游戏：石头  剪刀   布   2.0
增加：三局两胜退出
"""
import random

items = ("石头", "剪刀", "布")
# 胜利策略
wins = (
    ("石头", "剪刀"),
    ("剪刀", "布"),
    ("布", "石头"),
)

# 胜利次数     失败次数
win_count = defeat_count = 0
while True:
    # (1)系统生成的随机数 0  1  2
    sys_input_index = random.randint(0, 2)
    sys_input = items[sys_input_index]
    print(sys_input)  # 测试，打印系统随机出牌
    # (2)用户输入的0 1 2
    user_input_index = int(input("请输入:"))
    user_input = items[user_input_index]
    # (3)构建输入项 用于在胜利列表中查找
    item_input = (user_input, sys_input)
    if user_input == sys_input:  # (4) 逻辑处理
        print("平局")
    elif item_input in wins:
        print("赢啦")
        win_count += 1
    else:
        print("输啦")
        defeat_count += 1

    # 如果胜利2次   或者   输了2次
    if win_count == 2 or defeat_count == 2:
        break

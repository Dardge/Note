"""
    游戏界面模块
"""
from bll import GameCore
from models import Direction
import os



class GameConsoleView:
    def __init__(self):
        # 创建核心类对象
        self.__core = GameCore()

    def start(self):
        """
            游戏开始
            随机在地图上生成两个数字（2或者4）
            并打印地图
        :return:
        """
        self.__core.generate_number()
        self.__core.generate_number()
        self.print_atlas()

    def print_atlas(self):
        """
            打印地图
        :return:
        """
        # 清空控制台
        os.system('clear')
        # os.system('cls')
        for r in range(len(self.__core.atlas)):
            for c in range(len(self.__core.atlas[r])):
                print(self.__core.atlas[r][c], end=" ")
            print()

    def move_atlas(self):
        """
            移动地图
        :return:
        """
        dir = input("请输入移动方向：")
        if dir == "w":
            self.__core.move(Direction.up)
        if dir == "s":
            self.__core.move(Direction.down)
        if dir == "a":
            self.__core.move(Direction.left)
        if dir == "d":
            self.__core.move(Direction.right)

    def update(self):
        """
            更新游戏
        :return:
        """
        while True:
            # 移动地图
            self.move_atlas()
            # 如果地图有更新
            if self.__core.is_change:
                self.__core.generate_number()
                self.print_atlas()
                if self.__core.is_game_over():
                    print("游戏结束")
                    break

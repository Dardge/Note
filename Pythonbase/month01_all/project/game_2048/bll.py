"""
    2048 逻辑模块
"""
from models import Vector2, Direction
import random
import copy


class GameCore:
    """
        2048 核心类
    """

    def __init__(self):
        self.__list_merge = []
        # self.__atlas = [[0] * 4] * 4
        self.__atlas = [
            [0] * 4,
            [0] * 4,
            [0] * 4,
            [0] * 4,
        ]

        self.__list_empty_pos = []
        self.is_change = False

    @property
    def is_change(self):
        return self.__is_change

    @is_change.setter
    def is_change(self, value):
        self.__is_change = value

    @property
    def atlas(self):
        return self.__atlas

    def __move_up(self):
        """
        地图向上移动
        :param atlas:
        :return:
        """
        for c in range(4):
            for r in range(4):
                self.__list_merge.append(self.__atlas[r][c])
            self.__merge()
            for r in range(4):
                self.__atlas[r][c] = self.__list_merge[r]
            self.__list_merge.clear()

    def __move_down(self):
        """
        地图向下移动
        :param atlas:
        :return:
        """
        for c in range(4):
            for r in range(3, -1, -1):  # 从下往上遍历第c列的元素
                self.__list_merge.append(self.__atlas[r][c])
            self.__merge()
            for r in range(3, -1, -1):
                self.__atlas[r][c] = self.__list_merge[3 - r]
            self.__list_merge.clear()

    def __move_left(self):
        """
        地图向左移动
        :param atlas:
        :return:
        """
        for r in range(4):
            for c in range(4):
                self.__list_merge.append(self.__atlas[r][c])
            self.__merge()
            for c in range(4):
                self.__atlas[r][c] = self.__list_merge[c]
            self.__list_merge.clear()

    def __move_right(self):
        """
        地图向右移动
        :param atlas:
        :return:
        """
        for r in range(4):
            for c in range(3, -1, -1):
                self.__list_merge.append(self.__atlas[r][c])
            self.__merge()
            for c in range(3, -1, -1):
                self.__atlas[r][c] = self.__list_merge[3 - c]
            self.__list_merge.clear()

    def move(self, direction):
        """
            地图移动
        :param direction: 方向
        :return:
        """
        original_atlas = copy.deepcopy(self.atlas)
        if direction == Direction.up:
            self.__move_up()
        elif direction == Direction.down:
            self.__move_down()
        elif direction == Direction.left:
            self.__move_left()
        elif direction == Direction.right:
            self.__move_right()

        self.is_change = self.__equal_atlas(original_atlas)  # 修改is_change的value

    def __equal_atlas(self, original):  # 判断地图是否发生变化
        for r in range(len(original)):
            for c in range(len(original[r])):
                if original[r][c] != self.atlas[r][c]:
                    return True  # 发生变化
        return False  # 没有发生变化

    def __merge(self):
        """
        合并列表
        2 0 2 2 --> 4 2 0 0
        :param list_target:
        :return:
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] != 0 and self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                self.__list_merge[i + 1] = 0
        self.__zero_to_end()

    def __zero_to_end(self):
        """
        将列表中为零的元素移动至末尾
        2 0 2 0 --> 2 2 0 0
        :param list_target:
        :return:
        """
        temp_list = [e for e in self.__list_merge if e]  # if e (如果e不为0)
        for i in range(self.__list_merge.count(0)):
            temp_list.append(0)
        self.__list_merge[:] = temp_list[:]  # 将移动后的新的列表切片给__list_merge

    def __calculate_empty(self):
        """
            计算空白位置
        :return:
        """
        self.__list_empty_pos.clear()
        for r in range(4):
            for c in range(4):
                if self.atlas[r][c] == 0:
                    self.__list_empty_pos.append(Vector2(r, c))

    def generate_number(self):
        """
        生成数字
        :return:
        """
        self.__calculate_empty()
        # 如果没有空位置 则退出(不再产生新数字)
        if (len(self.__list_empty_pos)) == 0:
            return
        # 在列表中随机选择一个元素
        pos = random.choice(self.__list_empty_pos)
        # 90% 的概率生成2  10% 的概率产生 4
        self.atlas[pos.x][pos.y] = 4 if random.randint(1, 10) == 1 else 2  # ***********************
        # 因为该位置存储了新数字，所以不再作为空位置。
        self.__list_empty_pos.remove(pos)

    def is_game_over(self):
        """
            游戏是否结束
        :return:
        """
        # 如果有空位置
        if len(self.__list_empty_pos) > 0:
            return False

        # # 如果水平方向 具有相同元素
        # for r in range(4):
        #     for c in range(3):
        #         if self.atlas[r][c] == self.atlas[r][c+1]:
        #             return False
        #
        # # 垂直方向
        # for c in range(4):
        #     for r in range(3):
        #         if self.atlas[r][c] == self.atlas[r+1][c]:
        #             return False

        for r in range(4):
            for c in range(3):
                if self.atlas[r][c] == self.atlas[r][c + 1] or self.atlas[c][r] == self.atlas[c + 1][r]:
                    return False
        return True

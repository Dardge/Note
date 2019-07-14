"""
    数据模块
"""


class Vector2:
    """
        向量类 表示位置
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Direction:
    up = 0
    down = 1
    left = 2
    right = 3

# print(Direction.right)  # 3


# from enum import Enum, unique
#
# @unique
# class Direction(Enum):
#     up = 0
#     down = 1
#     left = 2
#     right = 3
#
# def enum_test(dir):
#     if dir == Direction.left:
#         print("左边")
#     if dir == Direction.right:
#         print("右边")
#
# enum_test(Direction.right)

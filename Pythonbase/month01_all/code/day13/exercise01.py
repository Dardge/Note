"""
玩家(具有攻击力)攻击敌人，敌人(具有血量)受伤后掉血，还可能死亡。
敌人攻击玩家，玩家受伤后掉血并碎屏，还可能死亡(游戏结束)。
"""

class Player:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp

    def attack(self, enemy):
        print("玩家攻击敌人")
        enemy.damage(self.atk)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            self.__death()
        print("咔嚓~ 碎屏啦")

    # 私有成员（变量  方法） 类外无法调用
    def __death(self):
        print("游戏结束")


class Enemy:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp

    def attack(self, player):
        player.damage(self.atk)
        print("敌人攻击玩家啦")

    def damage(self, value):
        print("敌人受伤啦")
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("敌人死亡喽")















p01 = Player(50,100)
e01 = Enemy(5,50)
e01.attack(p01)

p01.attack(e01)










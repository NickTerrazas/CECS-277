#Extends from entity class.
import entity
import random


class Troll(entity.Entity):
    #randomize hp
    def __init__(self):
        super().__init__("Hard Troll", random.randint(10, 14))

    #randomize damage
    def melee_attack(self, enemy):
        enemy.take_damage(random.randint(8, 12))
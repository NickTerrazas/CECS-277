#Extends from entity class.
import entity
import random


class EasyTroll(entity.Entity):
    #randomize hp based on table.
    def __init__(self):
        super().__init__("Easy Troll", random.randint(6, 9))

    #randomize damage based on table.
    def melee_attack(self, enemy):
        enemy.take_damage(random.randint(5, 9))
#Extends from entity class.
import entity
import random


class EasyGoblin(entity.Entity):
    #randomize hp
    def __init__(self):
        super().__init__("Easy Goblin", random.randint(5, 7))

    #randomize damage
    def melee_attack(self, enemy):
        enemy.take_damage(random.randint(4, 6))
#Extends from entity class.
import entity
import random


class Goblin(entity.Entity):
    #randomize hp
    def __init__(self):
        super().__init__("Hard Goblin", random.randint(6, 10))

    #randomize damage
    def melee_attack(self, enemy):
        enemy.take_damage(random.randint(5, 8))
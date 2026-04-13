#Extends from entity class.
import entity
import random


class Ogre(entity.Entity):
    #randomize hp
    def __init__(self):
        super().__init__("Hard Ogre", random.randint(8, 12))

    #randomize damage
    def melee_attack(self, enemy):
        enemy.take_damage(random.randint(6, 10))
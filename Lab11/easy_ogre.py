#Extends from entity class.
import entity
import random


class EasyOgre(entity.Entity):
    #randomize hp
    def __init__(self):
        super().__init__("Easy Ogre", random.randint(7, 8))

    #randomize damage
    def melee_attack(self, enemy):
        enemy.take_damage(random.randint(5, 8))
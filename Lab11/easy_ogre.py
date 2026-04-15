#Extends from entity class.
import entity
import random


class EasyOgre(entity.Entity):
    #randomize hp
    def __init__(self):
        super().__init__("Weak Ogre", random.randint(7, 8))

    #randomize damage
    def melee_attack(self, enemy):
        damage = random.randint(5, 8)
        enemy.take_damage(damage)
        return(f"{self._name} smashes {enemy._name} for {damage} damage!")
#Extends from entity class.
import entity
import random


class EasyGoblin(entity.Entity):
    #randomize hp
    def __init__(self):
        super().__init__("Baby Goblin", random.randint(5, 7))

    #randomize damage
    def melee_attack(self, enemy):
        damage = random.randint(4, 6)
        enemy.take_damage(damage)
        return(f"{self._name} bites {enemy._name} for {damage} damage!")
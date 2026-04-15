#Extends from entity class.
import entity
import random


class Goblin(entity.Entity):
    #randomize hp
    def __init__(self):
        super().__init__("Hard Goblin", random.randint(6, 10))

    #randomize damage
    def melee_attack(self, enemy):
        damage = random.randint(5, 8)
        enemy.take_damage(damage)
        return(f"{self._name} bites {enemy._name} for {damage} damage!")
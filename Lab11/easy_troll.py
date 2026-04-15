#Extends from entity class.
import entity
import random


class EasyTroll(entity.Entity):
    #randomize hp based on table.
    def __init__(self):
        super().__init__("Tiny Troll", random.randint(6, 9))

    #randomize damage based on table.
    def melee_attack(self, enemy):
        damage = random.randint(5, 9)
        enemy.take_damage(damage)
        return(f"{self._name} kicks {enemy._name} for {damage} damage!")
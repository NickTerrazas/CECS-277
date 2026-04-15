#Extends from entity class.
import entity
import random


class Troll(entity.Entity):
    #randomize hp
    def __init__(self):
        super().__init__("Foul Troll", random.randint(10, 14))

    #randomize damage
    def melee_attack(self, enemy):
        damage = random.randint(8, 12)
        enemy.take_damage(damage)
        return(f"{self._name} kicks {enemy._name} for {damage} damage!")
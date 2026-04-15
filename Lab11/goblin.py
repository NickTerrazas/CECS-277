#Extends from entity class.
import entity
import random


class Goblin(entity.Entity):
    """
        Initializes the hard goblin with a name and health points.
    """
    def __init__(self):
        super().__init__("Ghoulish Goblin", random.randint(6, 10))

    """
        Method for the hard goblin's melee attack. Deals 5-8 damage to the enemy.
        Parameters:
            enemy (Entity): The enemy to attack.
        Returns:
            str: A string describing the attack.
    """
    def melee_attack(self, enemy):
        damage = random.randint(5, 8)
        enemy.take_damage(damage)
        return(f"{self._name} bites {enemy._name} for {damage} damage!")
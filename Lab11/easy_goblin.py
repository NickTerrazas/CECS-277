#Extends from entity class.
import entity
import random


class EasyGoblin(entity.Entity):
    """
        Initializes the easy goblin with a name and health points.
    """
    def __init__(self):
        super().__init__("Baby Goblin", random.randint(5, 7))

    """
        Method for the easy goblin's melee attack. Deals 4-6 damage to the enemy.
        Parameters:
            enemy (Entity): The enemy to attack.
        Returns:
            str: A string describing the attack.
    """
    def melee_attack(self, enemy):
        damage = random.randint(4, 6)
        enemy.take_damage(damage)
        return(f"{self._name} bites {enemy._name} for {damage} damage!")
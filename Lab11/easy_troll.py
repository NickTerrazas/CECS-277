#Extends from entity class.
import entity
import random


class EasyTroll(entity.Entity):
    """
        Initializes the easy troll with a name and health points.
    """
    def __init__(self):
        super().__init__("Tiny Troll", random.randint(6, 9))

    """
        Method for the easy troll's melee attack. Deals 5-9 damage to the enemy.
        Parameters:
            enemy (Entity): The enemy to attack.
        Returns:
            str: A string describing the attack.
    """
    def melee_attack(self, enemy):
        damage = random.randint(5, 9)
        enemy.take_damage(damage)
        return(f"{self._name} kicks {enemy._name} for {damage} damage!")
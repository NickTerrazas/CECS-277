#Extends from entity class.
import entity
import random


class Troll(entity.Entity):
    """
        Initializes the hard troll with a name and health points.
    """
    def __init__(self):
        super().__init__("Foul Troll", random.randint(10, 14))

    """
        Method for the hard troll's melee attack. Deals 8-12 damage to the enemy.
        Parameters:
            enemy (Entity): The enemy to attack.
        Returns:
            str: A string describing the attack.
    """
    def melee_attack(self, enemy):
        damage = random.randint(8, 12)
        enemy.take_damage(damage)
        return(f"{self._name} kicks {enemy._name} for {damage} damage!")
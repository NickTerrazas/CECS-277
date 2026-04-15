#Extends from entity class.
import entity
import random


class EasyOgre(entity.Entity):
    """
        Initializes the easy ogre with a name and health points.
    """
    def __init__(self):
        super().__init__("Weak Ogre", random.randint(7, 8))

    """
        Method for the easy ogre's melee attack. Deals 5-8 damage to the enemy.
        Parameters:
            enemy (Entity): The enemy to attack.
        Returns:
            str: A string describing the attack.
    """
    def melee_attack(self, enemy):
        damage = random.randint(5, 8)
        enemy.take_damage(damage)
        return(f"{self._name} smashes {enemy._name} for {damage} damage!")
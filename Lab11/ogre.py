#Extends from entity class.
import entity
import random


class Ogre(entity.Entity):
    """
        Initializes the hard ogre with a name and health points.
    """
    def __init__(self):
        super().__init__("Muscular Ogre", random.randint(8, 12))

    """
        Method for the hard ogre's melee attack. Deals 6-10 damage to the enemy.
        Parameters:
            enemy (Entity): The enemy to attack.
        Returns:
            str: A string describing the attack.
    """
    def melee_attack(self, enemy):
        damage = random.randint(6, 10)
        enemy.take_damage(damage)
        return(f"{self._name} smashes {enemy._name} for {damage} damage!")
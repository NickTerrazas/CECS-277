import entity
import random

class Hero(entity.Entity):
    """The user's character, extends from Entity."""

    def __init__(self, name):
        """Calls super and sets name and default hp of 25."""
        super().__init__(name, 25)

    def melee_attack(self, enemy):
        """The hero's melee attack. Rolls 2 six-sided dice and deals damage based on the result.
        Parameters:
            enemy (Entity): The enemy that the hero is attacking.
        Returns:
            str: A string describing the attack and the damage dealt.
        """
        #Roll 2 six-sided dice for the damage and adds the result.
        damage = random.randint(1, 6) + random.randint(1, 6)
        enemy.take_damage(damage)
        return(f"{self._name} strikes the {enemy._name} with a sword for {damage} damage")
    
    def ranged_attack(self, enemy):
        """The hero's ranged attack. Rolls 1 twelve-sided die and deals damage based on the result.
        Parameters:
            enemy (Entity): The enemy that the hero is attacking.
        Returns:
            str: A string describing the attack and the damage dealt.
        """
        #Roll 1 twelve-sided die for the damage.
        damage = random.randint(1, 12)
        enemy.take_damage(damage)
        return(f"{self._name} pierces the {enemy._name} with an arrow for {damage} damage")
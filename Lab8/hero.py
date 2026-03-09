import entity
import random

class Hero(entity.Entity):
    """
    A hero has two attacks: sword and arrow.
    The sword attack rolls 2 six-sided dice and adds the results together to determine the damage dealt to the dragon.
    The arrow attack rolls a twelve-sided die to determine the damage dealt to the dragon.
    """

    def sword_attack(self, dragon):
        """
        Rolls 2 six-sided dice and adds the results together to determine the damage dealt to the dragon.
        Parameters:
            dragon (Dragon): The dragon to attack.
        Returns:
            A string with the description of the attack.
        """
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        damage = d1 + d2
        dragon.take_damage(damage)
        return f"You slash the {dragon.name} with your sword for {damage} damage."
    
    def arrow_attack(self, dragon):
        """
        Rolls a twelve-sided die to determine the damage dealt to the dragon.
        Parameters:
            dragon (Dragon): The dragon to attack.
        Returns:
            A string with the description of the attack.
        """
        damage = random.randint(1, 12)
        dragon.take_damage(damage)
        return f"You hit the {dragon.name} with an arrow for {damage} damage."
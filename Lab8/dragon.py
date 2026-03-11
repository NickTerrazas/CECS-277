import entity
import random

class Dragon(entity.Entity):
    """
    Dragons are a type of entity that have a name and health points. 
    They can take damage and have two types of attacks: a basic tail attack and a special claw attack.
    
    The basic attack can be used an unlimited number of times, while the special attack can only be 
    used a limited number of times based on the dragon's health.
    """
    #Basic tail attack. Deals random damage between 2 and 5
    def basic_attack(self, hero):
        damage = random.randint(2, 5)
        print(f"The dragon whips its tail at you for {damage} damage")
        hero.take_damage(damage)

    #Claw attack. Deals random damage between 3 and 7
    def special_attack(self, hero):
        damage = random.randint(3, 7)
        print(f"The dragon slashes you with its claws for {damage} damage")
        hero.take_damage(damage)
import entity
import random

class Dragon(entity.Entity):

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
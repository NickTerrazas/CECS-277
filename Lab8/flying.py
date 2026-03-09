import dragon
import random

class FlyingDragon(dragon.Dragon):

    #Calls super and sets name and hp; also assigns a default number of swoops(2 or 3)
    def __init__(self, name, hp):
        super().__init__(name, hp)
        #Adjusts the number of swoops based on the hp.
        self.swoops = 2 if hp < 20 else 3
    
    #Overriden swoop attack. Deals random damage between 5 and 8, and can be used a limited number of times.
    def special_attack(self, hero):
        if self.swoops > 0:
            damage = random.randint(5, 8)
            print(f"The flying dragon swoops at you for {damage} damage")
            hero.take_damage(damage)
            self.swoops -= 1
        else:
            print("The flying dragon is out of swoops and uses a basic attack instead.")
            super().basic_attack(hero)

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} \n   It has {self.swoops} swoops left."
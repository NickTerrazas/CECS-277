import dragon
import random

class FireDragon(dragon.Dragon):
    """
    FireDragon is a subclass of Dragon that creates a new type of dragon with a special fire attack.
    The fire attack can only be used a limited number of times.
    """

    #Calls super and sets name and hp; also assigns a default number of fire shots(2 or 3)
    def __init__(self, name, hp):
        super().__init__(name, hp)
        #Adjusts the number of fire shots based on the hp.
        self.fire_shots = 2 if hp < 20 else 3
    
    #Overriden fire attack. Deals random damage between 6 and 9, and can be used a limited number of times.
    def special_attack(self, hero):
        if self.fire_shots > 0:
            damage = random.randint(6, 9)
            print(f"The fire dragon breathes fire at you for {damage} damage")
            hero.take_damage(damage)
            self.fire_shots -= 1
        else:
            print("The fire dragon is out of fire shots and uses a basic attack instead.")
            super().basic_attack(hero)

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} \n   It has {self.fire_shots} fire shots left."
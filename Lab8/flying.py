import dragon
import random

class FlyingDragon(dragon.Dragon):
    """
    FlyingDragon is a subclass of Dragon that creates a new type of dragon with a special swoop attack.
    The swoop attack can only be used a limited number of times.
    """

    #Calls super and sets name and hp; also assigns a default number of swoops(2 or 3)
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.swoops = 3
    
    #Overriden swoop attack. Deals random damage between 5 and 8, and can be used a limited number of times.
    def special_attack(self, hero):
        if self.swoops > 0:
            damage = random.randint(5, 8)
            print(f"{self._name} swoops at you for {damage} damage")
            hero.take_damage(damage)
            self.swoops -= 1
        else:
            print(f"{self._name} tries to swoop at you but is all out of swoops.")

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} \n   It has {self.swoops} swoops left."
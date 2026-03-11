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
        self.fire_shots = 2

    #Overriden fire attack. Deals random damage between 6 and 9, and can be used a limited number of times.
    def special_attack(self, hero):
        if self.fire_shots > 0:
            damage = random.randint(6, 9)
            print(f"{self._name} breathes fire at you for {damage} damage")
            hero.take_damage(damage)
            self.fire_shots -= 1
        else:
            print(f"{self._name} tries to spit fire at you but is all out of fire shots.")

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} \n   It has {self.fire_shots} fire shots left."
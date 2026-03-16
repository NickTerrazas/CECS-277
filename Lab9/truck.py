import vehicle
import random


class Truck(vehicle.Vehicle):
    """
    
    """

    def special_move(self, obs_loc):
        """

        """
        #Determine if the truck has enough energy.
        if super()._energy >= 15:
            super()._energy -= 15
            distance = round(super().speed * 2) + random.randint(-1, 1)
            super()._position += distance
            #Determine if the truck rams through an obstacle
            if (super()._position + distance) >= obs_loc:
                return str(super()._name) + " rams through an obstacle and moves " + str(distance) + " units."
            else:
                return str(super()._name) + " moves " + str(distance) + " units."
        else:
            super()._position += 1
            return str(super()._name) + " did not have enough energy for a nitro boost and only moves 1 unit."
import vehicle
import random


class Car(vehicle.Vehicle):
    """
    
    """

    def special_move(self, obs_loc):
        """
        
        """
        #Determine if the car has enough energy.
        if super()._energy >= 15:
            super()._energy -= 15
            distance = round(super().speed * 1.5) + random.randint(-1, 1)
            #Determine if the car hits an obstacle
            if (super()._position + distance) >= obs_loc:
                super()._position = obs_loc
                return str(super()._name) + " crashes into an obstacle."
            else:
                return str(super()._name) + " uses nitro boost and moves " + str(distance) + " units."
        else:
            super()._position += 1
            return str(super()._name) + " did not have enough energy for a nitro boost and only moves 1 unit."
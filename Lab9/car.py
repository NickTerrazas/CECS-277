import vehicle
import random


class Car(vehicle.Vehicle):
    """
    
    """

    def special_move(self, obs_loc):
        """
        
        """
        #Determine if the car has enough energy.
        if super().energy >= 15:
            super().energy -= 15
            distance = round(super().speed * 1.5) + random.randint(-1, 1)
            #Determine if the car hits an obstacle
            if (super().position + distance) >= obs_loc:
                super().position = obs_loc
                return str(super().name) + " crashes into an obstacle."
            else:
                return str(super().name) + " uses nitro boost and moves " + str(distance) + " units."
        else:
            super().position += 1
            return str(super().name) + " did not have enough energy for a nitro boost and only moves 1 unit."
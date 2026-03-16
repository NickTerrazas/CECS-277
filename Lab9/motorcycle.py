import vehicle
import random


class Motorcycle(vehicle.Vehicle):
    """
    
    """

    def slow(self, obs_loc):
        """

        """
        distance = round(super()._speed * 0.75) + random.randint(-1, 1)
        if (super()._position + distance) >= obs_loc:
            return str(super()._name) + " slowly dodges the obstacle and moves " + str(distance) + " units."
        else:
            return str(super()._name) + " slowly moves " + str(distance) + " units."


    def special_move(self, obs_loc):
        """
        
        """
        #Determine if the motorcycle has enough energy.
        if super()._energy >= 15:
            super()._energy -= 15
            #Determine if the motorcycle will fall over.
            if random.randint(1, 4) == 1:
                super()._position += 1
                return str(super()._name) + " fell over while trying to pop a wheelie and only moves 1 unit."
            else:
                distance = round(super().speed * 1.5) + random.randint(-1, 1)
                #Determine if the motorcycle hits an obstacle
                if (super()._position + distance) >= obs_loc:
                    super()._position = obs_loc
                    return str(super()._name) + " crashes into an obstacle."
                else:
                    return str(super()._name) + " pops a wheelie and moves " + str(distance) + " units."
        else:
            super()._position += 1
            return str(super()._name) + " did not have enough energy for a nitro boost and only moves 1 unit."
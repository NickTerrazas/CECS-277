import vehicle
import random


class Car(vehicle.Vehicle):

    def special_move(self, obs_loc):
        """
        Nitro Boost
        If the car has enough energy it will move 1.5 times it's speed + or - 1, unless it hits an obstacle.
        Parameters:
            obs_loc (int): The location of the next obstacle.
        Returns:
            A string describing how the car will move.
        """
        #Determine if the car has enough energy.
        if super()._energy >= 15:
            super()._energy -= 15
            distance = round(super().speed * 1.5) + random.randint(-1, 1)
            #Determine if the car hits an obstacle
            if (super()._position + distance) >= obs_loc:
                super()._position = obs_loc
                return f"{super()._name} crashes into an obstacle."
            else:
                return f"{super()._name} uses nitro boost and moves {distance} units."
        else:
            super()._position += 1
            return f"{super()._name} did not have enough energy for a nitro boost and only moves 1 unit."
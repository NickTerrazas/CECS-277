import vehicle
import random


class Truck(vehicle.Vehicle):

    def special_move(self, obs_loc):
        """
        Ram
        Truck moves at double speed + or - 1, and will ram through any obstacles it comes across.
        Parameters:
            obs_loc (int): The location of the next obstacle.
        Returns:
            A string representing how the truck moves.
        """
        #Determine if the truck has enough energy.
        if super()._energy >= 15:
            super()._energy -= 15
            distance = round(super().speed * 2) + random.randint(-1, 1)
            super()._position += distance
            #Determine if the truck rams through an obstacle
            if (super()._position + distance) >= obs_loc:
                return f"{super()._name} rams through an obstacle and moves {distance} units."
            else:
                return f"{super()._name} moves {distance} units."
        else:
            super()._position += 1
            return f"{super()._name} did not have enough energy for a nitro boost and only moves 1 unit."
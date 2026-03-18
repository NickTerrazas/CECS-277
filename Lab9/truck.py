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
        if self._energy >= 15:
            self._energy -= 15
            distance = round(self._speed * 2) + random.randint(-1, 1)
            self._position += distance
            #Determine if the truck rams through an obstacle
            if (self._position + distance) >= obs_loc:
                return f"{self._name} rams through an obstacle and moves {distance} units."
            else:
                self._position += distance
                return f"{self._name} moves {distance} units."
        else:
            self._position += 1
            return f"{self._name} did not have enough energy for a ram and only moves 1 unit."
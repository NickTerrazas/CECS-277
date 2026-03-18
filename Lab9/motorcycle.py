import vehicle
import random


class Motorcycle(vehicle.Vehicle):

    def slow(self, obs_loc):
        """
        Custom slow movement
        Will travel at 0.75 times speed + or - 1.
        Parameters:
            obs_loc (int): The location of the next obstacle.
        Returns:
            A string representing how the motorcycle moves.:
        """
        distance = int(self._speed * 0.75) + random.randint(-1, 1)
        if (self._position + distance) >= obs_loc:
            self._position += distance
            return f"{self._name} slowly dodges the obstacle and moves {distance} units."
        else:
            self._position += distance
            return f"{self._name} slowly moves {distance} units."


    def special_move(self, obs_loc):
        """
        Wheelie
        Has a 75% chance to travel double its speed + or - 1, unless it hits an obstacle, or a 25% chance to fall over
        Parameters:
            obs_loc (int): The location of the next obstacle.
        Returns:
            A string representing how the motorcycle moves.
        """
        #Determine if the motorcycle has enough energy.
        if self._energy >= 15:
            self._energy -= 15
            #Determine if the motorcycle will fall over.
            if random.randint(1, 4) == 1:
                self._position += 1
                return f"{self._name} fell over while trying to pop a wheelie and only moves 1 unit."
            else:
                distance = int(self._speed * 2) + random.randint(-1, 1)
                #Determine if the motorcycle hits an obstacle
                if (self._position + distance) >= obs_loc:
                    self._position = obs_loc
                    return f"{self._name} crashes into an obstacle."
                else:
                    self._position += distance
                    return f"{self._name} pops a wheelie and moves {distance} units."
        else:
            self._position += 1
            return f"{self._name} did not have enough energy for a wheelie and only moves 1 unit."
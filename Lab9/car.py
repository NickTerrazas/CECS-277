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
        if self._energy >= 15:
            self._energy -= 15
            distance = int(self._speed * 1.5) + random.randint(-1, 1)

            if (self._position + distance < obs_loc) and self._position < 99:
                self._position += distance
                if self._position >= 99:
                    self._position = 99
                    return f"{self._name} has reached the end of the track."
                else:
                    return f"{self._name} uses nitro boost and moves {distance} units."
            elif self._position == 99:
                return
            else:
                self._position = obs_loc
                return f"{self._name} crashed into the obstacle!"
        else:
            self._position += 1
            if self._position >= 99:
                return f"{self._name} has reached the end of the track."
            else:
                return f"{self._name} did not have enough energy for a nitro boost and only moves 1 unit."
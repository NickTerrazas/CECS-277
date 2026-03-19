import abc
import random

class Vehicle:
    """
    A class representing a vehicle in a racing game. 
    The vehicle has attributes for its name, initial speed, current position, and energy level. 
    """

    def __init__(self, name, initial, speed):
        """
        Set the attributes using the parameters, assign 0 to position and 100 to energy
        Parameters: 
            name (str): The name of the vehicle
            initial (str): The initial of the vehicle
            speed (int): The initial speed of the vehicle
        """
        self._name = name
        self._initial = initial
        self._speed = speed
        self._position = 0
        self._energy = 100

    def fast(self, obs_loc):
        """
        Move the vehicle fast, consuming energy and potentially crashing into an obstacle.
        Parameters:
            obs_loc (int): The location of the next obstacle
        """
        if self._energy >= 5:
            distance = self._speed + random.randint(-1, 1)
            self._energy -= 5
            if (self._position + distance < obs_loc) and self._position < 99:
                self._position += distance
                if self._position >= 99:
                    self._position = 99
                    return f"{self._name} has reached the end of the track."
                else:
                    return f"{self._name} moved {distance} spaces."
            elif self._position >= 99:
                return
            else:
                self._position = obs_loc
                return f"{self._name} crashed into the obstacle!"
        else:
            self._position += 1
            if self._position >= 99:
                return f"{self._name} has reached the end of the track."
            else:
                return f"{self._name} tried to go fast but didn't have enough energy and only moves 1 unit!"


    def slow(self, obs_loc):
        """
        Move the vehicle slow, consuming less energy and allowing it to maneuver around obstacles.
        Parameters:
            obs_loc (int): The location of the next obstacle
            
        """
        distance = int(self._speed * 0.5) + random.randint(-1, 1)
        if (self._position + distance < obs_loc) and self._position < 99:
            self._position += distance
            if self._position >= 99:
                self._position = 99
                return f"{self._name} has reached the end of the track."
            else:
                return f"{self._name} slowly moves {distance} spaces."
        elif self._position == 99:
            return
        else:
            self._position += distance
            if self._position >= 99:
                return f"{self._name} has reached the end of the track."
            else:
                return f"{self._name} slowly dodges the obstacle and moves {distance} units."


    def __str__(self):
        """
        Returns: a string of vehicle's name, position and energy    
        """
        return f"{self._name}: Position {self._position}, Energy {self._energy}"
    
   
    @abc.abstractmethod
    def special_move(self, obs_loc):
        """
        Abstract method - overridden in the subclasses.
        Parameters:
            obs_loc (int): The location of the next obstacle
        """
        pass

        

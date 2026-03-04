#Nicholas Terrazas and Devin Heinemann
#03/02/2026

import random

class Die: 
    """
    Represents a single die. 
    The die is created and can be rolled. The die can be compared to other dice or the difference can be found. A string can be reutned with the value of a roll.
    """
    def __init__(self, sides=6):
        """
        Creates a die with a specified number of sides.
        Parameters: sides represents the number of sides on the die (default is 6).
        """
        self._sides = sides
        self._value = 0

    def roll(self):
        """
        Generates a random numebr between 1 nand the number of sides. Returns the value.
        Parameters: self._sides represents the number of sides on the die.
        Returns: self._value represents the value of the die after rolling.
        """
        self._value = random.randint(1, self._sides)
        return self._value
    
    def __str__(self):
        """
        Returns a string representation of the value of the current roll of the die.
        """
        return f"{self._value}"
    
    def __lt__(self, other):
        """
        Compares itself to another die to see if its value is less than the other die's value.
        Parameters: other represents another die object.
        Returns: True if self._value is less than other._value, False otherwise.
        """
        return self._value < other._value

    def __eq__(self, other):
        """
        Compares itself to another die to see if the values are equal.
        Parameters: other represents another die object.
        Returns: True if self._value is equal to other._value, False otherwise.
        """
        return self._value == other._value

    def __sub__(self, other):
        """
        Subtracts the value of another die from the value of this die.
        Parameters: other represents another die object.
        Returns: The difference between self._value and other._value.
        """
        return abs(self._value - other._value)
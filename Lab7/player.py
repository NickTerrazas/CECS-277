#Nicholas Terrazas and Devin Heinemann
#03/02/2026

import die

class Player:
    """
    This class represents a player in the game. 
    This class creates 3 dice objects from the die class and keeps track of the player's score and the dice they have rolled.
    The point of the player class is to keep track of the player's score and the dice they have rolled.
    """
    def __init__(self):
        self.dice_list = [die.Die() for c in range(3)]
        self.score = 0
    
    def points(self):
        """
        Sets the player's score to the current score and returns it.
        Parameters: self represents the player object.
        Returns: The player's score.
        """

        return self.score
    
    def roll_dice(self, dice_list):
        """
        Rolls the dice and sets the values of each die into a list of die objects. It then sorts
        the list of objects.
        Parameters: self, dice_list represents the list of dice objects that the player has rolled.
        """
        #Call roll method from die class to roll the dice and update the player's dice list
        for i in range(len(dice_list)):
            dice_list[i].roll()
            self.dice_list[i] = dice_list[i]
        self.dice_list.sort()

    def has_pair(self):
        """
        Checks if the player has a pair of dice with the same value. If the player has a pair, 
        it increments the player's score by 1 and returns True. Otherwise, it returns False.
        Parameters: self represents the player object.
        Returns: True if the player has a pair, False otherwise.
        """
        if self.dice_list[0] == self.dice_list[1] or self.dice_list[0] == self.dice_list[2] or self.dice_list[1] == self.dice_list[2]:
            self.score += 1
            return True
        else:
            return False
    
    def has_three_of_a_kind(self):
        """
        Checks if the player has three dice with the same value. If the player has three of a kind, 
        it increments the player's score by 2 plus the score from has_pair and returns True. Otherwise, it returns False.
        Parameters: self represents the player object.
        Returns: True if the player has three of a kind, False otherwise.
        """
        if self.dice_list[0] == self.dice_list[1] and self.dice_list[0] == self.dice_list[2]:
            #Incremeting score by 2 because has_pair will already increment score by 1 giving a total of 3 points.
            self.score += 2
            return True
        else:
            return False
    
    def has_series(self):
        """
        Checks if the player has a series of three consecutive dice. If the player has a series, 
        it increments the player's score by 2 and returns True. Otherwise, it returns False.
        Parameters: self represents the player object.
        Returns: True if the player has a series, False otherwise.
        """
        die1 = self.dice_list[0]
        die2 = self.dice_list[1]
        die3 = self.dice_list[2]


        if (die1 -die2) == 1 and (die2 - die3) == 1:
            self.score += 2
            return True
        else:
            return False
        
    def __str__(self):
        print("\nD1 = " + str(self.dice_list[0]) + ", D2 = " + str(self.dice_list[1]) + ", D3 = " + str(self.dice_list[2]))

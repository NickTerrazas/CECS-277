#Nicholas Terrazas and Devin Heinemann
#03/02/2026

import die

class Player:
    """
    This class represents a player in the game. 
    This class creates 3 dice objects from the die class and keeps track of the player's score and the dice they have rolled.
    The point of the player class is to keep track of the player's score and the dice they have rolled.
    """
    def __init__(self, dice_list):
        self.dice_list = dice_list
        self.score = 0
    
    def points(self):
        """
        This method calculates the player's score based on the dice they have rolled.
        """
        self.score = sum(self.dice_list)
        return self.score
    
    def roll_dice(self, dice_list):
        """
        """
        #Call roll method from die class to roll the dice and update the player's dice list
        #Waiting until die class is complete to test this method
        for i in range(len(dice_list)):
            dice_list[i].roll()
            self.dice_list[i] = dice_list[i].get_value()

    def has_pair(self):
        """
        """
        if self.dice_list[0] == self.dice_list[1] or self.dice_list[0] == self.dice_list[2] or self.dice_list[1] == self.dice_list[2]:
            return True
        else:
            return False
    
    def has_three_of_a_kind(self):
        """
        """
        if self.dice_list[0] == self.dice_list[1] and self.dice_list[0] == self.dice_list[2]:
            return True
        else:
            return False
    
    def has_series(self):
        """
        """
        if sorted(self.dice_list) == [1, 2, 3] or sorted(self.dice_list) == [2, 3, 4] or sorted(self.dice_list) == [3, 4, 5] or sorted(self.dice_list) == [4, 5, 6]:
            self.score += 2
            return True
        else:
            return False
        
    def __str__(self):
        print("D1 =" + str(self.dice_list[0]) + ", D2 = " + str(self.dice_list[1]) + ", D3 = " + str(self.dice_list[2]) + ", Score: " + str(self.score))

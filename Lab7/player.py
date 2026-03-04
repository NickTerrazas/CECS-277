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
        This method calculates the player's score based on the dice they have rolled.
        """

        return self.score
    
    def roll_dice(self, dice_list):
        """
        """
        #Call roll method from die class to roll the dice and update the player's dice list
        for i in range(len(dice_list)):
            dice_list[i].roll()
            self.dice_list[i] = dice_list[i]
        self.dice_list.sort()

    def has_pair(self):
        """
        """
        if self.dice_list[0] == self.dice_list[1] or self.dice_list[0] == self.dice_list[2] or self.dice_list[1] == self.dice_list[2]:
            self.score += 1
            return True
        else:
            return False
    
    def has_three_of_a_kind(self):
        """
        """
        if self.dice_list[0] == self.dice_list[1] and self.dice_list[0] == self.dice_list[2]:
            #Incremeting score by 2 because has_pair will already increment score by 1 giving a total of 3 points.
            self.score += 2
            return True
        else:
            return False
    
    def has_series(self):
        """
        """
        die1 = self.dice_list[0]
        die2 = self.dice_list[1]
        die3 = self.dice_list[2]


        if (die1 -die2) == 1 and (die2 - die3) == 1:
            self.score += 2
            return True
        else:
            return False
        #TODO redo series test. This keeps giving errors. List is already sorted so no need to use 'sorted'
        

        '''if self.dice_list == [1, 2, 3] or self.dice_list == [2, 3, 4] or self.dice_list == [3, 4, 5] or self.dice_list == [4, 5, 6]:
            self.score += 2
            return True
        else:
            return False'''
        
    def __str__(self):
        print("D1 = " + str(self.dice_list[0]) + ", D2 = " + str(self.dice_list[1]) + ", D3 = " + str(self.dice_list[2]))

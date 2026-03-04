#Nicholas Terrazas and Devin Heinemann
#Lab 7
#03/02/2026
'''
A dice game that awards the user points for a pair, three-of-a-kind, or a series.
The program repeatedly rolls three dice and calculates any points based on the game rules.
The user can choose to continue or end the game and subsequently get the final score.

The game rules are as follows:
- A pair (two dice with the same value) awards 1 point.
- Three-of-a-kind (three dice with the same value) awards 3 points (1 point for the pair and an additional 2 points for the three-of-a-kind).
- A series (three consecutive values) awards 2 points.
- If none of the above combinations are rolled, the player scores 0 points for that turn.
'''

import player
import check_input

def take_turn(player):
    """
    Takes in a player object and rolls the dice for that player. Checks if the player has a pair, three of a kind, or a series of 3. Then calculates the player's score.
    Parameters: player represents a player object.
    """
    #Rolls the dice for the player and prints out the result.
    player.roll_dice(player.dice_list)
    player.__str__()
    #Checks for an winning combinations and prints out the result.
    if player.has_pair():
        if player.has_three_of_a_kind():
            print("You got 3 of a kind!")
        else:
            print("You got a pair!")
    elif player.has_series():
        print("You got a series of 3!")
    else: 
        print("You got nothing. :(")
    #Calculates the player's score and prints it out.
    print("Score: ", player.points())

def main():
    player1 = player.Player()
    play = True
    #Loop to take turns until the user chooses to end the game
    print("-Yahtzee-")
    while play:
        take_turn(player1)
        cont = check_input.get_yes_no("Play Again? (y/n): ")
        if cont == False:
            play = False
        
    print("\nGame Over.")
    print("Final Score = " + str(player1.score))

if __name__ == "__main__":
    main()
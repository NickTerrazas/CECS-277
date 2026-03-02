#Nicholas Terrazas and Devin Heinemann
#Lab 7
#03/02/2026

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


if __name__ == "__main__":
    main()
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
    player1 = player.Player()
    play = True
    #Loop to take turns until the user chooses to end the game
    while play:
        take_turn(player1)
        cont = check_input.get_yes_no("Do you want to continue? (y/n): ")
        if cont == False:
            play = False
        
    print("Game Over.")
    print("Final Score = " + str(player1.score))

if __name__ == "__main__":
    main()
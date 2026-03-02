#Nicholas Terrazas and Devin Heinemann
#Lab 7
#03/02/2026


import player
import check_input

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
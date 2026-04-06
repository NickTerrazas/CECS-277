#Nicholas Terrazas and Devin Heinemann
#Lab 10
#04/06/2026

# Description: This program is a maze game where the player controls a hero trying to reach the finish while avoiding a minotaur. 
# The maze is represented as a grid, and the player can move in four directions (WASD). The game continues until the hero reaches 
# the finish or runs into the minotaur.

from check_input import get_direction
import maze
import hero
import minotaur


def main():
    mazeObj = maze.Maze()
    heroObj = hero.Hero()
    minotaurObj = minotaur.Minotaur()

    print(mazeObj)
    while True:
        move = check_input.get_direction("Enter a direction to move (WASD): ")
        if move == 'W':
            result = hero.go_up()
        elif move == 'A':
            result = hero.go_left()
        elif move == 'S':
            result = hero.go_down()
        elif move == 'D':
            result = hero.go_right()
        
        if result == 'f':
            print("Congratulations! You reached the finish and won the game!")
            break
        elif result == 'M':
            print("Oh no! You ran into the Minotaur and lost the game!")
            break
        
        minotaurObj.move_minotaur(heroObj._row, heroObj._col)
        print(mazeObj)


if __name__ == "__main__":    
    main()
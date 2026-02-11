#Nicholas Terrazas and Devin Heinemann
#Lab 4
#02/09/2026
#Description: ___

import check_input

def read_maze():
    """Opens the maze.txt file and saves it as a 2d list.
    Parameters: None
    Returns: A 2d list representing the maze.
    """
    file = open("maze.txt", "r") #Not sure why this isn't opening the file.
    maze = [] 
    #Fills the maze as a 2d list from the maze.txt file.
    for line in file:
        row = [] 
        for char in line.strip(): 
            if char != '\n': 
                row.append(char)
        maze.append(row)
    file.close
    return maze


def find_start(maze):
    """Finds where an 's' is in the maze and returns its location as 2d coordinate list.
    Parameters: A 2d list representing the maze.
    Returns: A 2d list representing the coordinates of the 's' in the maze.
    """
    for i in range (len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 's':
                coordinates = [i, j]
                return coordinates


def display_maze(maze, loc):
    return


def main():
    location = find_start(read_maze)

main()
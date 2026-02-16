#Nicholas Terrazas and Devin Heinemann
#Lab 4
#02/09/2026
#Description: This program reads a maze from a file into a 2D list and allows the user 
#to navigate from the start ('s') to the finish ('f') while preventing movement through walls.

from check_input import get_int_range

def read_maze():
    """Opens the maze.txt file and saves it as a 2d list.
    Parameters: None
    Returns: A 2d list representing the maze.
    """
    file = open("maze.txt", "r")
    maze = [] 
    #Fills the maze as a 2d list from the maze.txt file.
    for line in file:
        row = [] 
        for char in line.strip(): 
            if char != '\n': 
                row.append(char)
        maze.append(row)
    file.close()
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
    """Displays the maze, showing 'X' at the user's current location.
    Parameters:
      maze: 2d list of chars
      loc: 1d list [row, col]
    Returns: None
    """
    locX = loc[0]
    locY = loc[1]

    for i in range (len(maze)):
        for j in range(len(maze[i])):
            if(i == locX):
                if(j == locY):
                    print('X', end="")
                    continue
            print(maze[i][j], end="")
        print('\n')


def main():
    maze = read_maze()
    location = find_start(maze)

    play = True
    choice = 0

    print("-Maze Solver-")

    while(play):
        currentX = location[0]
        currentY = location[1]

        display_maze(maze, location)

        print("1. Go North\n"+"2. Go South\n"+"3. Go East\n"+"4. Go West\n"+"5. Quit")
        choice = get_int_range("Enter choice: ", 1, 5)

        #Go North
        if(choice == 1):
            if(maze[currentX - 1][currentY] == '*'):
                print("You cannot move there.")
                continue
            location = [currentX - 1, currentY]

        #Go South
        if(choice == 2):
            if(maze[currentX + 1][currentY] == '*'):
                print("You cannot move there.")
                continue
            location = [currentX + 1, currentY]

        #Go East
        if(choice == 3):
            if(maze[currentX][currentY + 1] == '*'):
                print("You cannot move there.")
                continue
            location = [currentX, currentY + 1]

        #Go West
        if(choice == 4):
            if(maze[currentX][currentY - 1] == '*'):
                print("You cannot move there.")
                continue
            location = [currentX, currentY - 1]

        #Quit game
        if(choice == 5): 
            play = False

        #Checks for finish
        if maze[location[0]][location[1]] == 'f':
            display_maze(maze, location)
            print("Congratulations! You solved the maze!")
            play = False
    print("Thanks for playing!\n") 
main()
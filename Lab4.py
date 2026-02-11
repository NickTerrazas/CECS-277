#Nicholas Terrazas and Devin Heinemann
#Lab 4
#02/09/2026
#Description: ___

import check_input

def read_maze():
    file = open("maze.txt", "r")
    maze = []
    for line in file:
        row = []
        for char in line.strip():
            row.append(char)
        maze.append(row)
    file.close

    print(maze)


#def find_start(maze):
#def display_maze(maze, loc):

def main():
    #Test
    read_maze()

main()
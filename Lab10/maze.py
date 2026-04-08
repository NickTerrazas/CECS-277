# Singleton class Maze that reads a maze from a text file and provides methods to access and manipulate the maze data. 
# The class ensures that only one instance of the maze exists throughout the program.
class Maze:
    _instance = None
    _intialized = False

    #Checks if an instance of the class already exists; if not, creates one and returns it
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    #Creates a 2D list from the maze text file
    def __init__(self):
        if not Maze._intialized:
            self.maze = []
            with open("Lab10\\minomaze.txt", "r") as f:
                for line in f:
                    self.maze.append(list(line.strip()))
            Maze._intialized = True
    
    #Returns the specified row of the maze
    def __getitem__(self, row):
        return self.maze[row]

    #Returns the number of rows in the maze
    def __len__(self):
        return len(self.maze)

    #Returns the maze as a string in a grid format
    def __str__(self):
        maze_str = ""
        for row in self.maze:
            maze_str += "".join(row) + "\n"
        return maze_str
        
    #Returns the location of the specified character in the maze as a two-item 1d list
    def search_maze(self, ch):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == ch:
                    return [i, j]
        return None
import maze
import random

class Minotaur():
    """A class to represent a minotaur in a game."""

    def __init__(self):
        """init"""
        maze = maze.Maze()
        valid_start = False
        while not valid_start:
            rowstart = random.randint(0, len(maze) - 1)
            colstart = random.randint(0, len(maze[0]) - 1)
            if maze[rowstart][colstart] == ' ':
                maze[rowstart][colstart] = 'M'
                self._row = rowstart
                self._col = colstart
                valid_start = True

    def move_minotaur(self):
        """Move the minotaur in a random direction."""

        #determine possible moves.
        maze = maze.Maze()
        up = True
        if maze[self._row - 1][self._col] == '*' or maze[self._row - 1][self._col] == 'f':
            up = False
        down = True
        if maze[self._row + 1][self._col] == '*' or maze[self._row + 1][self._col] == 'f':
            down = False
        left = True
        if maze[self._row][self._col - 1] == '*' or maze[self._row][self._col - 1] == 'f':
            left = False
        right = True
        if maze[self._row][self._col + 1] == '*' or maze[self._row][self._col + 1] == 'f':
            right = False

        #move towards hero if possible, otherwise move randomly
        hero_loc = maze.Maze().search_maze('H')
        if hero_loc is not None:
            valid_move = False
            if abs(self._row - hero_loc[0]) > abs(self._col - hero_loc[1]):
                #move vertically
                if self._row > hero_loc[0]:
                    #move up
                    if up and not valid_move:
                        maze[self._row][self._col] = ' '
                        self._row -= 1
                        maze[self._row][self._col] = 'M'
                        valid_move = True
                else:
                    #move down
                    if down and not valid_move:
                        maze[self._row][self._col] = ' '
                        self._row += 1
                        maze[self._row][self._col] = 'M'
                        valid_move = True
            else:
                #move horizontally
                if self._col > hero_loc[1]:
                    #move left
                    if left and not valid_move:
                        maze[self._row][self._col] = ' '
                        self._col -= 1
                        maze[self._row][self._col] = 'M'
                        valid_move = True
                else:
                    #move right
                    if right and not valid_move:
                        maze[self._row][self._col] = ' '
                        self._col += 1
                        maze[self._row][self._col] = 'M'
                        valid_move = True

        #cant move towards hero, move randomly
        if not valid_move:
            valid_moves = []
            if up:
                valid_moves.append('up')
            if down:
                valid_moves.append('down')
            if left:
                valid_moves.append('left')
            if right:
                valid_moves.append('right')
            if len(valid_moves) > 0:
                move = random.choice(valid_moves)
                if move == 'up':
                    maze[self._row][self._col] = ' '
                    self._row -= 1
                    maze[self._row][self._col] = 'M'
                elif move == 'down':
                    maze[self._row][self._col] = ' '
                    self._row += 1
                    maze[self._row][self._col] = 'M'
                elif move == 'left':
                    maze[self._row][self._col] = ' '
                    self._col -= 1
                    maze[self._row][self._col] = 'M'
                elif move == 'right':
                    maze[self._row][self._col] = ' '
                    self._col += 1
                    maze[self._row][self._col] = 'M'
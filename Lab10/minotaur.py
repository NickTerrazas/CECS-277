import maze
import random

class Minotaur():
    """A minotaur inside the maze trying to catch the hero."""

    def __init__(self):
        """Finds a random valid starting location for the minotaur in the maze and places it there."""
        #super().__init__()
        mazeob = maze.Maze()
        valid_start = False
        while not valid_start:
            rowstart = random.randint(0, len(mazeob) - 1)
            colstart = random.randint(0, len(mazeob[0]) - 1)
            if mazeob[rowstart][colstart] == ' ':
                mazeob[rowstart][colstart] = 'M'
                self._row = rowstart
                self._col = colstart
                valid_start = True

    def move_minotaur(self):
        """Trys to move the minotaur closer to the player if possible, otherwise moves randomly. 
        The minotaur can only move in the four cardinal directions and cannot move through walls or the finish."""
        
        #determine possible moves.
        mazeob = maze.Maze()
        up = True
        if mazeob[self._row - 1][self._col] == '*' or mazeob[self._row - 1][self._col] == 'f':
            up = False
        down = True
        if mazeob[self._row + 1][self._col] == '*' or mazeob[self._row + 1][self._col] == 'f':
            down = False
        left = True
        if mazeob[self._row][self._col - 1] == '*' or mazeob[self._row][self._col - 1] == 'f':
            left = False
        right = True
        if mazeob[self._row][self._col + 1] == '*' or mazeob[self._row][self._col + 1] == 'f':
            right = False

        #move towards hero if possible.
        hero_loc = maze.Maze().search_maze('H')
        if hero_loc is not None:
            valid_move = False
            if abs(self._row - hero_loc[0]) > abs(self._col - hero_loc[1]):
                #move vertically
                if self._row > hero_loc[0]:
                    #move up
                    if up and not valid_move:
                        mazeob[self._row][self._col] = ' '
                        self._row -= 1
                        mazeob[self._row][self._col] = 'M'
                        valid_move = True
                else:
                    #move down
                    if down and not valid_move:
                        mazeob[self._row][self._col] = ' '
                        self._row += 1
                        mazeob[self._row][self._col] = 'M'
                        valid_move = True
            else:
                #move horizontally
                if self._col > hero_loc[1]:
                    #move left
                    if left and not valid_move:
                        mazeob[self._row][self._col] = ' '
                        self._col -= 1
                        mazeob[self._row][self._col] = 'M'
                        valid_move = True
                else:
                    #move right
                    if right and not valid_move:
                        mazeob[self._row][self._col] = ' '
                        self._col += 1
                        mazeob[self._row][self._col] = 'M'
                        valid_move = True

            #cant move towards hero, move randomly.
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
                        mazeob[self._row][self._col] = ' '
                        self._row -= 1
                        mazeob[self._row][self._col] = 'M'
                    elif move == 'down':
                        mazeob[self._row][self._col] = ' '
                        self._row += 1
                        mazeob[self._row][self._col] = 'M'
                    elif move == 'left':
                        mazeob[self._row][self._col] = ' '
                        self._col -= 1
                        mazeob[self._row][self._col] = 'M'
                    elif move == 'right':
                        mazeob[self._row][self._col] = ' '
                        self._col += 1
                        mazeob[self._row][self._col] = 'M'
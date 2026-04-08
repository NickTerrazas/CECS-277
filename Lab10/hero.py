import maze

class Hero():
    """The hero inside the maze trying to escape from the minotaur."""

    def __init__(self):
        """Locates the starting location and places the hero there."""
        #super().__init__()
        mazeob = maze.Maze()
        start = mazeob.search_maze('s')
        self._row = start[0]
        self._col = start[1]
        mazeob[self._row][self._col] = 'H'

    def go_up(self):
        """Move the hero up.
        Returns the character at the new location (space, finish, or minotaur) or None if the move is invalid.
        """
        mazeob = maze.Maze()
        if self._row > 0:
            new_loc = mazeob[self._row - 1][self._col]
            if new_loc != '*':
                mazeob[self._row][self._col] = ' '
                self._row -= 1
                mazeob[self._row][self._col] = 'H'
            if new_loc == '*':
                print("You ran into a wall!")
            return str(new_loc)

    def go_down(self):
        """Move the hero down.
        Returns the character at the new location (space, finish, or minotaur) or None if the move is invalid.
        """
        mazeob = maze.Maze()
        if self._row < len(mazeob) - 1:
            new_loc = mazeob[self._row + 1][self._col]
            if new_loc != '*':
                mazeob[self._row][self._col] = ' '
                self._row += 1
                mazeob[self._row][self._col] = 'H'
            if new_loc == '*':
                print("You ran into a wall!")
            return str(new_loc)

    def go_left(self):
        """Move the hero left.
        Returns the character at the new location (space, finish, or minotaur) or None if the move is invalid.
        """
        mazeob = maze.Maze()
        if self._col > 0:
            new_loc = mazeob[self._row][self._col - 1]
            if new_loc != '*':
                mazeob[self._row][self._col] = ' '
                self._col -= 1
                mazeob[self._row][self._col] = 'H'
            if new_loc == '*':
                print("You ran into a wall!")
            return str(new_loc)

    def go_right(self):
        """Move the hero right.
        Returns the character at the new location (space, finish, or minotaur) or None if the move is invalid.
        """
        mazeob = maze.Maze()
        if self._col < len(mazeob[0]) - 1:
            new_loc = mazeob[self._row][self._col + 1]
            if new_loc != '*':
                mazeob[self._row][self._col] = ' '
                self._col += 1
                mazeob[self._row][self._col] = 'H'
            if new_loc == '*':
                print("You ran into a wall!")
            return str(new_loc)
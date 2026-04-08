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
        """Move the hero up."""
        if self._row > 0:
            new_loc = maze[self._row - 1][self._col]
            if new_loc != '*':
                maze[self._row][self._col] = ' '
                self._row -= 1
                maze[self._row][self._col] = 'H'
            return str(new_loc)

    def go_down(self):
        """Move the hero down."""
        if self._row < len(maze) - 1:
            new_loc = maze[self._row + 1][self._col]
            if new_loc != '*':
                maze[self._row][self._col] = ' '
                self._row += 1
                maze[self._row][self._col] = 'H'
            return str(new_loc)

    def go_left(self):
        """Move the hero left."""
        if self._col > 0:
            new_loc = maze[self._row][self._col - 1]
            if new_loc != '*':
                maze[self._row][self._col] = ' '
                self._col -= 1
                maze[self._row][self._col] = 'H'
            return str(new_loc)

    def go_right(self):
        """Move the hero right."""
        if self._col < len(maze[0]) - 1:
            new_loc = maze[self._row][self._col + 1]
            if new_loc != '*':
                maze[self._row][self._col] = ' '
                self._col += 1
                maze[self._row][self._col] = 'H'
            return str(new_loc)
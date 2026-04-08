import maze

class Hero(maze.Maze):
    """The hero inside the maze trying to escape from the minotaur."""

    def __init__(self):
        """Locates the starting location and places the hero there."""
        super().__init__()
        rownum = 0
        for row in maze:
            colnum = 0
            for col in row:
                if col == 's':
                    maze[row][col] = 'H'
                    self._row = rownum
                    self._col = colnum
                colnum += 1
            rownum += 1

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
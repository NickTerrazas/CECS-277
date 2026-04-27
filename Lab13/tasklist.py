import task

class TaskList():
    """
    The TaskList class represents a list of tasks that can be added, marked as complete, and saved to a file. 
    It also supports iteration over the tasks in the list.
    The list is created by reading from a file called "tasks.txt", where each line represents a task.
    """
    def __init__(self):
        """
        Initialize the TaskList object by reading tasks from a file and storing them in a list.
        """
        file = open("tasklist.txt", "r")
        self.tasks = []
        for line in file:
            t = task.Task(line.strip().split(",")[0], line.strip().split(",")[1], line.strip().split(",")[2])
            self.tasks.append(t)
        file.close()

    def add_task(self, desc, date, time):
        """
        Adds a new task to the task list with the given description, date, and time. After adding the task, the list is sorted.
        Parameters:
            desc (str): The description of the task.
            date (str): The date of the task in the format "MM-DD-YYYY".
            time (str): The time of the task in the format "HH:MM".
        """
        string = str(desc) + "," + str(date) + "," + str(time)
        self.tasks.append(string)
        self.tasks.sort()
    
    def get_current_task(self):
        """
        Returns the first task in the task list.
        """
        return self.tasks[0]

    def mark_complete(self):
        """
        Removes and returns the current task in the task list, indicating that it has been completed.
        """
        task = self.get_current_task()
        self.tasks.remove(task)
        return task

    def save_file(self):
        """
        Write the contents of the tasklist back to the file using the Task's __repr__ method.
        """
        file = open("tasks.txt", "w")
        for t in self.tasks:
            file.write(t.__repr__(t))
        file.close()

    def __len__(self):
        """
        Returns the number of tasks currently in the task list.
        """
        return len(self.tasks)

    def __iter__(self):
        """
        Initialize the iterator attribute n and return self.
        """
        self._n = 0
        return self

    def __next__(self):
        """
        Iterates the interator one task at a time. 
        If at the end of the task list, raises a StopIteration exception. Otherwise, returns the current task.
        """
        if self._n < len(self.tasks):
            result = self.tasks[self._n]
            self._n += 1
            return result
        else:
            raise StopIteration
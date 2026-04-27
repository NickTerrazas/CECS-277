class Task:
    """
        Initializes a Task object with a description, due date, and due time.
        Parameters:
            desc (str): The description of the task.
            date (str): The due date of the task in the format MM/DD/YYYY.
            time (str): The due time of the task in the format HH:MM.
    """
    def __init__(self, desc, date, time):
        self.description = desc
        self.date = date
        self.time = time  

    """
        Method returns a string representation of the Task object, including its description, due date, and due time.
        Returns:
            str: A string representation of the Task object.
    """
    def __str__(self):
        return f"Task: {self.description}\nDue: {self.date} at {self.time}"
    
    """
        Method returns a detailed string representation of the Task object.
        Returns:
            str: A string representation of the Task object.
    """
    def __repr__(self):
        return f"Task(description='{self.description}', date='{self.date}', time='{self.time}')"
    
    """
        Method compares two Task objects based on their due date, time, and description.
        Parameters:
            other (Task): The other Task object to compare with.
        Returns:
            bool: True if this Task is less than the other Task, False otherwise.
    """
    def __lt__(self, other):
        if self.date != other.date:
            return self.date < other.date
        if self.time != other.time:
            return self.time < other.time
        return self.description < other.description
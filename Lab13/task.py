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
        return f"{self.description},{self.date},{self.time}"
    
    """
        Method compares two Task objects based on their due date, time, and description.
        Parameters:
            other (Task): The other Task object to compare with.
        Returns:
            bool: True if this Task is less than the other Task, False otherwise.
    """
    def __lt__(self, other):
        if self.date != other.date:
            #Breaks up the date into parts and compares them in order of year, month, day
            self_date_parts = self.date.split("/")
            other_date_parts = other.date.split("/")
            if self_date_parts[2] != other_date_parts[2]: #2 is the year
                return self_date_parts[2] < other_date_parts[2]
            if self_date_parts[0] != other_date_parts[0]: #0 is the month
                return self_date_parts[0] < other_date_parts[0]
            return self_date_parts[1] < other_date_parts[1] #1 is the day
        if self.time != other.time:
            #Breaks up the time into parts and compares them in order of hour, minute
            self_time_parts = self.time.split(":")
            other_time_parts = other.time.split(":")
            if self_time_parts[0] != other_time_parts[0]: #0 is the hour
                return self_time_parts[0] < other_time_parts[0]
            return self_time_parts[1] < other_time_parts[1] #1 is the minute
        return self.description < other.description
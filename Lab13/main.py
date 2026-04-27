#Nicholas Terrazas and Devin Heinemann
#Lab 13
#04/27/2026

#Description:
import tasklist
import check_input

tasks = tasklist.TaskList()
tasks.tasks.sort()

"""
    Print the main menu and get the user's choice.
    Returns:
        int: The user's menu choice.
"""
def main_menu():
    print("-Tasklist-")
    print(f"Tasks to complete: {len(tasks)}")
    print("1. Display current task")
    print("2. Display all tasks")
    print("3. Mark current task complete")
    print("4. Add new task")
    print("5. Search by date")
    print("6. Save and quit")
    choice = check_input.get_int_range("Enter choice: ", 1, 6)
    return choice

"""
    Prompts the user to enter a date (month, day, year) and returns it in the format MM/DD/YYYY.
    Returns:
        str: The date in MM/DD/YYYY format.
"""
def get_date():
    month = check_input.get_int_range("Enter month: ", 1, 12)
    day = check_input.get_int_range("Enter day: ", 1, 31)
    year = check_input.get_int_range("Enter year: ", 2000, 2100)

    if month < 10:
        month = f"0{month}"
    if day < 10:
        day = f"0{day}"

    return f"{month}/{day}/{year}"


"""
    Prompts the user to enter a time (hour, minute) and returns it in the format HH:MM.
    Returns:
        str: The time in HH:MM format.
"""
def get_time():
    hour = check_input.get_int("Enter hour: ", 0, 23)
    minute = check_input.get_int("Enter minute: ", 0, 59)

    if hour < 10:
        hour = f"0{hour}"
    if minute < 10:
        minute = f"0{minute}"

    return f"{hour}:{minute}"

def main():
    while True:
        choice = main_menu()
        #Display current task
        if choice == 1:
            if len(tasks) > 0:
                print(tasks.get_current_task())
            else:
                print("No tasks to complete.")
        #Display all tasks
        elif choice == 2:
            if len(tasks) > 0:
                for task in tasks:
                    print(task)
            else:
                print("No tasks to complete.")
        #Mark current task complete
        elif choice == 3:
            if len(tasks) > 0:
                completed_task = tasks.mark_complete()
                print(f"Marking current task as complete: {completed_task}")
                if len(tasks) > 0:
                    print(f"New current task is: {tasks.get_current_task()}")
            else:
                print("No tasks to complete.")
        #Add new task
        elif choice == 4:
            desc = input("Enter task description: ")
            date = get_date()
            time = get_time()
            new_task = tasks.Task(desc, date, time) #FIX IMPORT ONCE TASKLIST IS COMPLETE
            tasks.append(new_task) #FIX IMPORT ONCE TASKLIST IS COMPLETE
        #Search by date
        elif choice == 5:
            search_date = get_date()
            for task in tasks: #FIX IMPORT ONCE TASKLIST IS COMPLETE
                if task.date == search_date:
                    print(task)
        #Save and quit
        elif choice == 6:
            # Save tasks to file (not implemented yet)
            print("Saving list...")
            break


if __name__ == "__main__":
    main()

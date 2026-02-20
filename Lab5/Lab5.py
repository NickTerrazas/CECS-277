#Nicholas Terrazas and Devin Heinemann
#Lab 5
#02/16/2026
#Description: 

from question import Question
import check_input


def read_file_to_dictionary(filename: str) -> dict:
    """
    Description: Takes in the name of a file and puts the contents into a dictionary, with states as keys and capitals as values.
    
    Parameters: The name of the file to read from.

    Returns: A dictionary of {state: capital} pairs.
    """
    states = {}

    #Opens the file and puts each pair into the dictionary.
    file = open(filename, "r")
    for line in file:
        line = file.readline()
        pair = line.split(',')

        #The state is the key and the capital is the value.
        states[str(pair[0])] = str(pair[1].strip('\n'))
    file.close()

    return states


def get_user_choice(valid_options: list[str]) -> str:
    """
    Description: Takes in a list of strings as valid options and prompts the user to enter a choice until they enter a valid one.
    Automatically capitalizes the user's input.
    
    Parameters: A list of valid options.

    Returns: The valid choice entered by the user.
    """

    choice = str(input("Enter choice: ")).upper()
    
    #checks if the choice is valid, if not it prompts the user to enter a valid choice until they do.
    while choice not in valid_options:
        print("Invalid input. Enter " + valid_options[0] + "-" + valid_options[-1] + ".")
        choice = str(input("Enter choice: ")).upper()

    return choice


def ask_question(number: int, states: dict) -> int:
    """
    Description: Asks the user a question about state capitals and checks if their answer is correct. Prints the appropriate response and returns 1 if correct, else 0.

    Parameters: The number of the question being asked and a dictionary of {state: capital} pairs.

    Returns: 1 if the user answered correctly, 0 otherwise. Will be used to calculate the user's score at the end of the quiz.
    """
    q = Question(states)
    print(f"{number}. {q}")
    selection = get_user_choice(q.possible_choices)
    if q.check_correct(selection):
        print(q.correct_response())
        return 1
    else:
        print(q.incorrect_response())
        return 0



def main():
    print("- State Capitals Quiz -")
    states = read_file_to_dictionary("statecapitals.txt")

    score = 0
    question = 0
    while question < 10:
        question += 1
        score += ask_question(question, states)

    print("\nEnd of test. You got " + str(score) + " out of " + str(question) + " correct!\n")

main()
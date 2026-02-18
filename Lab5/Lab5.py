#Nicholas Terrazas and Devin Heinemann
#Lab 5
#02/16/2026
#Description: 

from question import Question
import check_input


def read_file_to_dictionary(filename: str) -> dict:
    """
    Takes in the name of a file and puts the contents into a dictionary, with states as keys and capitals as values.
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
    Prompt user for a choice, uppercase it, and keep reprompting until it's valid.
    """
    # TODO:
    # - build prompt that adapts to list (ex: "Enter choice: ")
    # - while selection not in valid_options:
    #     print error similar to example (ex: "Invalid input. Enter A-D.")
    # - return valid selection

    choice = str(input("Enter choice: ")).upper()
    while choice not in valid_options:
        print("Invalid input. Enter " + valid_options[0] + "-" + valid_options[-1] + ".")
        choice = str(input("Enter choice: ")).upper()
        
    return choice


def ask_question(number: int, states: dict) -> int:
    """
    Create a Question, print it, get user input, check correctness,
    print response, and return 1 if correct else 0.
    """
    # TODO:
    # - q = Question(states)
    # - print(f"{number}. {q}")  OR print number separately then q
    # - selection = get_user_choice(q.possible_choices)
    # - if q.check_correct(selection): print(q.correct_response()); return 1
    #   else: print(q.incorrect_response()); return 0

    print(str(number) + ") The capital of " + "___" + " is:" )

    return 0


def main():
    print("- State Capitals Quiz -")
    states = read_file_to_dictionary("CECS-277\\Lab5\\statecapitals.txt")

    score = 0
    question = 0

    while question < 10:
        question += 1
        ask_question(question, states)
        guess = get_user_choice(["A", "B", "C", "D"])

    # TODO: loop exactly 10 times and tally points

    # TODO: final summary line similar to example output

main()
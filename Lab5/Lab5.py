#Nicholas Terrazas and Devin Heinemann
#Lab 5
#02/16/2026
#Description: 

from question import Question
import check_input


def read_file_to_dictionary(filename: str) -> dict:
    """
    Each line is: state,capital
    Read the file and return a dict of {state: capital}.
    """
    states = {}

    # TODO:
    # - open file
    # - for each line: strip newline, split by ',', assign into dict
    # - return dict

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
    return ""


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
    return 0


def main():
    print("- State Capitals Quiz -")

    # TODO: read states dict
    # states = read_file_to_dictionary("statecapitals.txt")

    score = 0

    # TODO: loop exactly 10 times and tally points

    # TODO: final summary line similar to example output
main()
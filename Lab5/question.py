#Nicholas Terrazas and Devin Heinemann
#02/16/2026
#Description: Defines a Question object used to quiz the user on state capitals.


import random


class Question:
    """
    Represents a single multiple-choice question about a state's capital.

    Attributes: _state, _correct_capital, _possible_choices, _selections, _answer.
    """
    def __init__(self, states: dict):
        """
        states: dictionary of {state: capital} pairs.

        Steps required by spec (high level):
        - Choose a random state/capital pair
        - Set possible choices (A-D by default)
        - Build selections list with correct + incorrect
        - Shuffle selections
        - Determine the correct letter answer after shuffle
        """
        # 1) Pick random state/capital
        all_states = list(states.keys())
        rand_state = random.choice(all_states)
        self._state = rand_state
        self._correct_capital = states[rand_state]

        all_capitals = list(states.values())
        incorrects = [c for c in all_capitals if c != self._correct_capital]

        # 2) Set possible choices
        self._possible_choices = ["A", "B", "C", "D"]

        # 3) Build selections list (capitals user sees)
        self._selections = [self._correct_capital]
        while len(self._selections) < 4:    #Need it to automatically loop based on the number of letters as choices, as per rubric. Try len(self._possible_choices).
            incorrect = random.choice(incorrects)
            if incorrect not in self._selections:
                self._selections.append(incorrect)

        # 4) Shuffle selections
        random.shuffle(self._selections)

        # 5) Set answer to the correct letter
        self._answer = self._possible_choices[self._selections.index(self._correct_capital)]

    @property
    def possible_choices(self):
        return self._possible_choices

    def check_correct(self, selection: str) -> bool:
        return selection.upper() == self._answer

    def incorrect_response(self) -> str:
        return f"Sorry, the correct answer is {self._answer}.\n"

    def correct_response(self) -> str:
        return f"Correct! The capital of {self._state} is {self._correct_capital}.\n"

    def __str__(self) -> str:
        output = f"Which is the capital of {self._state}?\n"
        for i in range(len(self._selections)):
            output += f"{self._possible_choices[i]}. {self._selections[i]}\n"
        return output

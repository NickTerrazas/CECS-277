#Nicholas Terrazas and Devin Heinemann
#02/16/2026
#Description: Defines a Question object used to quiz the user on state capitals.


import random


class Question:
    """
    Represents a single multiple-choice question about a state's capital.

    Required attributes (do not rename): _state, _correct_capital, _possible_choices,
    _selections, _answer.
    """

    def __init__(self, states: dict):
        """
        states: dictionary of {state: capital} pairs.

        Steps required by spec (high level):
        - Choose a random state/capital pair
        - Set possible choices (A-D by default)
        - Build selections list with correct + incorrect (no duplicates)
        - Shuffle selections
        - Determine the correct letter answer after shuffle
        """
        # 1) Pick random state/capital
        self._state = ""             # TODO
        self._correct_capital = ""   # TODO

        # 2) Set possible choices (must be a list like ["A","B","C","D"])
        self._possible_choices = []  # TODO: set to A-D :contentReference[oaicite:4]{index=4}

        # 3) Build selections list (capitals user sees)
        self._selections = []        # TODO: include correct + random incorrects (unique) :contentReference[oaicite:5]{index=5}

        # 4) Shuffle selections
        # TODO: random.shuffle(self._selections) :contentReference[oaicite:6]{index=6}

        # 5) Set answer to the correct letter AFTER shuffle
        self._answer = ""            # TODO :contentReference[oaicite:7]{index=7}

    @property
    def possible_choices(self):
        return self._possible_choices

    def check_correct(self, selection: str) -> bool:
        # TODO: compare selection to self._answer
        return False

    def incorrect_response(self) -> str:
        # TODO: return formatted string like example output
        return ""

    def correct_response(self) -> str:
        # TODO: return formatted string like example output
        return ""

    def __str__(self) -> str:
        # TODO: build string using self._state, self._possible_choices, self._selections
        return ""

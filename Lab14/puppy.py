import state_asleep

class Puppy():
    def __init__(self):
        """Initializes the puppy with an asleep state and zero feeds and plays."""
        self._state = state_asleep.Asleep()
        self._feeds = 0
        self._plays = 0

    @property
    def feeds(self):
        return self._feeds

    @property
    def plays(self):
        return self._plays
    
    def change_state(self, new_state):
        """Changes the state of the puppy to the new state."""
        self._state = new_state

    def throw_ball(self):
        """Throws a ball for the puppy to play with."""
        self._state.play(self)

    def give_food(self):
        """Gives food to the puppy."""
        self._state.feed(self)

    def inc_feeds(self):
        """Increments the feed count for the puppy."""
        self._feeds += 1

    def inc_plays(self):
        """Increments the play count for the puppy."""
        self._plays += 1

    def reset(self):
        """Resets the feed and play counts for the puppy."""
        self._feeds = 0
        self._plays = 0
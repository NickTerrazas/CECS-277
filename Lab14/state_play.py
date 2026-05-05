import state_asleep
import random

class Play():
    def feed(self, puppy):
        return f"The puppy is too busy playing with the ball to eat right now."

    def play(self, puppy):
        if puppy._plays < random.randint(2, 3):
            puppy.inc_plays()
            return f"You throw the ball again and the puppy excitedly chases it."
        else:
            puppy.change_state(state_asleep.Asleep())
            puppy.reset()
            return f"The puppy played so much it fell asleep!"
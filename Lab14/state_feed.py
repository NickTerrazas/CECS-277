import state_asleep
import state_play
import random

class Feed():
    def feed(self, puppy):
        if puppy._feeds < random.randint(2, 3):
            puppy.inc_feeds()
            return f"The puppy continues to eat as you add another scoop of kibble to its bowl."
        else:
            puppy.change_state(state_asleep.Asleep())
            puppy.reset()
            return f"The puppy ate so much it fell asleep!"

    def play(self, puppy):
        puppy.change_state(state_play.Play())
        puppy.inc_plays()
        return f"The puppy looks up from its food and chases the ball you threw."
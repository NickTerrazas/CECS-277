import state_feed

class Asleep():
    def feed(self, puppy):
        puppy.change_state(state_feed.Feed())
        puppy.inc_feeds()
        return f"The puppy wakes up and comes running to eat."

    def play(self, puppy):
        return f"The puppy is asleep. It doesn't want to play right now."
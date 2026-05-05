import abc

class PuppyState(abc.ABC):
    @abc.abstractmethod
    def feed(self, puppy):
        """Defines the behavior of the puppy when it is fed."""
        pass

    @abc.abstractmethod
    def play(self, puppy):
        """Defines the behavior of the puppy when it is played with."""
        pass
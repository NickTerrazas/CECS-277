
import abc

class Spy(abc.ABC):
    @abc.abstractmethod
    def description(self):
        """Abstract - spy description."""
        pass

    @abc.abstractmethod
    def agility(self):
        """Abstract - agility stat."""
        pass

    @abc.abstractmethod
    def stealth(self):
        """Abstract - stealth stat."""
        pass

    @abc.abstractmethod
    def tech_ability(self):
        """Abstract - tech ability stat."""
        pass

    def __str__(self):
        """Returns a string representation of the spy, including its description and stats."""
        return f"{self.description()} (Agility: {self.agility()}, Stealth: {self.stealth()}, Tech Ability: {self.tech_ability()})"
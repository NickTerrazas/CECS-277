
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
        return f"\n{self.description()} \nAgility: {self.agility()}\nStealth: {self.stealth()}\nTech Ability: {self.tech_ability()}"
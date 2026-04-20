
import spy

class HackerSpy(spy.Spy):
    def description(self):
        """Returns the description of the spy"""
        return "Hacker Spy"

    def agility(self):
        """Returns spy's agility stat"""
        return 2

    def stealth(self):
        """Returns spy's stealth stat"""
        return 3

    def tech_ability(self):
        """Returns spy's tech ability stat"""
        return 5
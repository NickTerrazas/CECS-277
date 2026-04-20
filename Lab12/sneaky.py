
import spy

class SneakySpy(spy.Spy):
    def description(self):
        """Returns the description of the spy"""
        return "Sneaky Spy"

    def agility(self):
        """Returns spy's agility stat"""
        return 4

    def stealth(self):
        """Returns spy's stealth stat"""
        return 5

    def tech_ability(self):
        """Returns spy's tech ability stat"""
        return 1
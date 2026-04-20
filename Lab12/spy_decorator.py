
import abc
import spy

class SpyDecorator(spy.Spy, abc.ABC):
    def __init__(self, s):
        self._spy = s

    def description(self):
        return self._spy.description()

    def agility(self):
        return self._spy.agility()

    def stealth(self):
        return self._spy.stealth()

    def tech_ability(self):
        return self._spy.tech_ability()
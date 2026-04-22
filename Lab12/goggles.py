#Agility 
#Stealth +2
#Tech Ability +1

import spy_decorator

class Goggles(spy_decorator.SpyDecorator):
    def agility(self):
        """Returns spy's agility stat"""
        return (super().agility() + 0)

    def stealth(self):
        """Returns spy's stealth stat"""
        return (super().stealth() + 2)

    def tech_ability(self):
        """Returns spy's tech ability stat"""
        return (super().tech_ability() + 1)
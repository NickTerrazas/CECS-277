#Agility +2
#Stealth 
#Tech Ability +1

import spy_decorator

class Jetpack(spy_decorator.SpyDecorator):
    def agility(self):
        """Returns spy's agility stat"""
        return (super().agility() + 3)

    def stealth(self):
        """Returns spy's stealth stat"""
        return (super().stealth() - 1)

    def tech_ability(self):
        """Returns spy's tech ability stat"""
        return (super().tech_ability() + 1)
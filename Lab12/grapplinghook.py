#Agility +2
#Stealth +1
#Tech Ability 

import spy_decorator

class GrapplingHook(spy_decorator.SpyDecorator):
    def agility(self):
        """Returns spy's agility stat"""
        return (super().agility() + 2)

    def stealth(self):
        """Returns spy's stealth stat"""
        return (super().stealth() + 1)

    def tech_ability(self):
        """Returns spy's tech ability stat"""
        return (super().tech_ability() + 0)
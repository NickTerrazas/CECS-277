import abc

class Entity(abc.ABC):
    """Abstract class that the monsters and the hero extend from."""

    def __init__(self, name, hp):
        """Sets the name and hp.
        Parameters:
            name (str): The name of the entity.
            hp (int): The health points of the entity.
        """
        self._name = name
        self._hp = hp

    def take_damage(self, dmg):
        """Deals the damage the entity takes. Subtracts the dmg value from the entity's _hp. Does not let the hp go below 0.
        Parameters:
            dmg (int): The damage points to subtract from the entity's hp.
        """
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0

    def __str__(self):
        """Return a string with the entity's name and hp.
        Returns:
            str: A string with the entity's name and hp.
        """
        return f"{self._name} - HP: {self._hp}"

    @abc.abstractmethod
    def melee_attack(self, enemy):
        """Abstract method for the melee attack"""
        pass
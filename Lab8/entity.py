#
#

class Entity:
    """
    An entity is created with basic functionality. It will have a name and health. 
    The entity can take damage which will lower its health.
    The entity can be displayed as a string in the format “Name: hp/max_hp”.
    """

    def __init__(self, name, max_hp):
        """
        Creates an entity with a name and health points.
        Parameters: 
            name (str): The name of the entity. 
            max_hp (int): The maximum health points of the entity.
        """
        #TODO: name and hp properties – use decorators to get (not set) the values of _name and _hp.
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    def take_damage(self, dmg):
        """
        Takes damage from an attack. Will not allow the entity's health points to go below 0.
        Parameters:
            dmg (int): The amount of damage to take.
        """
        self._hp -= dmg
        #If health goes below 0, it gets set back to 0.
        if self._hp < 0:
            self._hp = 0

    def __str__(self):
        """
        Returns:
            the entity's name and hp in the format “Name: hp/max_hp”
        """
        return str(self._name + ": " + str(self._hp) + "/" + str(self._max_hp))
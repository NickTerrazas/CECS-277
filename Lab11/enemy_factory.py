#Interface template for all enemy factories.
import abc

class EnemyFactory(abc.ABC):
    '''
    Abstract method for creating a random enemy. Each factory will implement this method to create a 
    random enemy of the appropriate difficulty.
    '''
    @abc.abstractmethod
    def create_random_enemy(self):
        pass
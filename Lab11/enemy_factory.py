#Interface template for all enemy factories.

import abc

class EnemyFactory(abc.ABC):
    @abc.abstractmethod
    def create_random_enemy(self):
        pass
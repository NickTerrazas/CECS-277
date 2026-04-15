#Creates easy enemies, extends from EnemyFactory.

import enemy_factory
import random
import easy_goblin
import easy_ogre
import easy_troll

class BeginnerFactory(enemy_factory.EnemyFactory):
    """
        Creates easy enemies, extends from EnemyFactory.
        The create_random_enemy method randomly constructs and returns one of the easy enemies. 
        Easy Goblin, Easy Ogre or Easy Troll.
    """
    def create_random_enemy(self):
        enemy_type = random.choice(['goblin', 'ogre', 'troll'])
        if enemy_type == 'goblin':
            return easy_goblin.EasyGoblin()
        elif enemy_type == 'ogre':
            return easy_ogre.EasyOgre()
        elif enemy_type == 'troll':
            return easy_troll.EasyTroll()

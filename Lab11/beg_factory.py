#Creates easy enemies, extends from EnemyFactory.

import enemy_factory
import random

class BeginnerFactory(enemy_factory.EnemyFactory):
    #randomly constructs and returns one of the easy enemies. Easy goblin, Easy Ogre or Easy Troll.
    def create_random_enemy(self):
        enemy_type = random.choice(['goblin', 'ogre', 'troll'])
        if enemy_type == 'goblin':
            return EasyGoblin()
        elif enemy_type == 'ogre':
            return EasyOgre()
        elif enemy_type == 'troll':
            return EasyTroll()

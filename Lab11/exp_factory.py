import enemy_factory
import random
import goblin
import ogre
import troll

class ExpertFactory(enemy_factory.EnemyFactory):
    #randomly constructs and returns one of the expert enemies. Goblin, Ogre or Troll.
    def create_random_enemy(self):
        enemy_type = random.choice(['goblin', 'ogre', 'troll'])
        if enemy_type == 'goblin':
            return goblin.Goblin()
        elif enemy_type == 'ogre':
            return ogre.Ogre()
        elif enemy_type == 'troll':
            return troll.Troll()
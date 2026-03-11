#Nicholas Terrazas and Devin Heinemann
#Lab 8
#03/09/2026

# Description: This program is a simple text-based game where the player, as a hero, 
# must defeat 3 different types of dragons (regular, fire, and flying) using different attacks. 
# Each dragon has its own unique special attack and the player must strategically choose which 
# dragon to attack and which weapon to use. The game continues until the player defeats all the 
# dragons or is defeated by them.

from fire import FireDragon
from flying import FlyingDragon
from dragon import Dragon
from entity import Entity
from hero import Hero
import check_input
import random


def main():

    #Create a hero and a list of 3 dragons (1 regular, 1 fire, 1 flying)
    hero_name = input("What is your name, challenger? ")
    hero = Hero(hero_name, 50)
    dragons = [Dragon("Deadly Nadder", 10), FireDragon("Gronkle", 15), FlyingDragon("Timberjack", 20)]

    print(f"Welcome to dragon training, {hero_name}!\nYou must defeat 3 dragons!\n")

    #Main game loop. Continues until the hero's hp is 0 or all dragons are defeated.
    while hero._hp > 0 and len(dragons) > 0:
        print(hero.__str__())
        if len(dragons) > 0:
            print(" 1. Attack " + dragons[0].__str__())
        if len(dragons) > 1:
            print(" 2. Attack " + dragons[1].__str__())
        if len(dragons) > 2:
            print(" 3. Attack " + dragons[2].__str__())
        d_choice = check_input.get_int_range("Which dragon do you want to attack: ", 1, len(dragons))

        #Player selects their attack and the damage is calculated and applied to the dragon.
        print("Attack with:\n 1. Arrow (1 D12)\n 2. Sword (2 D6)")
        w_choice = check_input.get_int_range("Enter weapon: ", 1, 2)
        if w_choice == 1:
            print(hero.arrow_attack(dragons[d_choice - 1]))
        else:
            print(hero.sword_attack(dragons[d_choice - 1]))
        
        #If the dragon's hp is 0 or less, it is removed from the list of dragons.
        if dragons[d_choice - 1]._hp <= 0:
            print(f"{dragons[d_choice - 1]._name} has been defeated!")
            dragons.pop(d_choice - 1)

        #Similarly to above, a living dragon randomly selects an attack and applies damage to the hero.
        if(len(dragons) > 0):
            dragon_choice = random.choice(dragons)
            attack_choice = random.choice([1,2])

            if attack_choice == 1:
                dragon_choice.basic_attack(hero)
            else:
                dragon_choice.special_attack(hero)
            print()
        else:
            #Player wins if they defeat all 3 dragons.
            print("\nCongratulations! You have defeated all 3 dragons, you have passed the trials.\n")
            return

        #Player loses if they run out of health.
        if hero._hp <= 0:
            print("\nYou have been defeated! Game over.\n")
            return

if __name__ == "__main__":
    main()
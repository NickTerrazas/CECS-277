#Nicholas Terrazas and Devin Heinemann
#Lab 8
#03/09/2026

from fire import FireDragon
from flying import FlyingDragon
from dragon import Dragon
from entity import Entity
from hero import Hero
import check_input


def main():

    #Create a hero and a list of 3 dragons (1 regular, 1 fire, 1 flying)
    hero_name = input("What is your name, challenger? ")
    hero = Hero(hero_name, 50)
    dragons = [Dragon("Deadly Nadder", 10), FireDragon("Gronkle", 15), FlyingDragon("Timberjack", 20)]

    print(f"Welcome to dragon training, {hero_name}!\nYou must defeat 3 dragons!\n")

    while hero._hp > 0 and len(dragons) > 0:
        print(hero.__str__())
        if len(dragons) > 0:
            print(" 1. Attack " + dragons[0].__str__())
        if len(dragons) > 1:
            print(" 2. Attack " + dragons[1].__str__())
        if len(dragons) > 2:
            print(" 3. Attack " + dragons[2].__str__())
        d_choice = check_input.get_int_range("Which dragon do you want to attack: ", 1, len(dragons))

        print("Attack with:\n 1. Arrow (1 D12)\n 2. Sword (2 D6)")
        w_choice = check_input.get_int_range("Enter weapon: ", 1, 2)


if __name__ == "__main__":
    main()
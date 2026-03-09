#Nicholas Terrazas and Devin Heinemann
#Lab 8
#03/09/2026

from fire import FireDragon
from flying import FlyingDragon
from dragon import Dragon
from entity import Entity
from hero import Hero


def main():

    #Create a hero and a list of 3 dragons (1 regular, 1 fire, 1 flying)
    hero_name = input("What is your name, challenger? ")
    hero = Hero(hero_name, 50)
    dragons = [Dragon("Deadly Nadder", 10), FireDragon("Gronkle", 15), FlyingDragon("Timberjack", 20)]

    print(f"Welcome to dragon training, {hero_name}!\nYou must defeat 3 dragons!\n")

    print(hero.__str__())
    print("1. Attack " + dragons[0].__str__())
    print("2. Attack " + dragons[1].__str__())
    print("3. Attack " + dragons[2].__str__())


if __name__ == "__main__":
    main()
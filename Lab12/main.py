#Nicholas Terrazas and Devin Heinemann
#Lab 12
#04/20/2026

#Description: Spy Infiltration is a simple text-based game where the player chooses a base spy type and decorates it with gadgets.
#The player picks either a Sneaky Spy or a Hacker Spy, and decorates it with two of the five gadgets.
#The gadgets are: Grappling Hook, Night-Vision Goggles, Hacking Kit, Lockpick, and Jetpack.
#The player then faces four challenges to infiltrate the villain's lair.
#If all four challenges are passed, then the spy breaks into the villain’s lair and wins the game.

import check_input
import sneaky
import hacker


def main():
    print("=== Spy Infiltration: Villain's Lair ===\nChoose a spy, equip 2 gadgets, and infiltrate the lair.")
    
    #Player chooses a base spy type
    print("\nChoose your starting spy:\n 1. Sneaky Spy - agile and stealthy\n 2. Hacker Spy - tech expert")
    spy_choice = check_input.get_int_range("Spy Choice: ", 1, 2)
    if spy_choice == 1:
        spy = sneaky.SneakySpy()
    elif spy_choice == 2:
        spy = hacker.HackerSpy()
    print(spy)

    #Player adds two gadgets to their spy
    print("\nChoose 2 gadgets to equip your spy with:")
    gadgets = ["Grappling Hook", "Night-Vision Goggles", "Hacking Kit", "Lockpick", "Jetpack"]
    gadget_choices = []
    while len(gadget_choices) < 2:
        print("Available Gadgets:")
        for i, gadget in enumerate(gadgets, 1):
            print(f" {i}. {gadget}")
        gadget = check_input.get_int_range("Gadget Choice: ", 1, len(gadgets))
        gadget_choices.append(gadgets[gadget - 1])
        gadgets.pop(gadget - 1)
        print()
    print(spy)

    #Challenge 1: Cliffside Entry
    print("=== Cliffside Entry ===")
    print("The front gate is too heavily guarded. You approach from the outside cliff and must scale the rock wall to reach a hidden entrance.")

    #Challenge 2: Laser Grid Hallway
    print("=== Laser Grid Hallway ===")
    print("A dark corridor is filled with moving laser beams. You must slip through without touching the grid and alerting security.")

    #Challenge 3: Ventilation Shaft
    print("=== Ventilation Shaft ===")
    print("Inside the facility, a vertical vent shaft is the only path upward. You need enough climbing ability to move through it quickly and quietly.")

    #Challenge 4: Security Terminal
    print("=== Security Terminal ===")
    print("A locked security terminal controls the final blast door. You need to bypass its access system before reaching the inner chamber.")


if __name__ == "__main__":
    main()
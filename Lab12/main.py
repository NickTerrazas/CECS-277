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
import grapplinghook
import goggles
import hackingkit
import lockpick
import jetpack
import random
import os

def choose_spy():
    """
    Allows the player to choose a base spy type.
    Returns:
        spy (Spy): The chosen spy object.
    """
    print("\nChoose your starting spy:\n 1. Sneaky Spy - agile and stealthy\n 2. Hacker Spy - tech expert")
    spy_choice = check_input.get_int_range("Spy Choice: ", 1, 2)
    if spy_choice == 1:
        spy = sneaky.SneakySpy()
    elif spy_choice == 2:
        spy = hacker.HackerSpy()
    return spy


def choose_gadgets(spy):
    """
    Allows the player to choose 2 gadgets for their spy.
    Parameters:
        spy (Spy): The spy object to equip with gadgets.
    Returns:
        gadget_picks (list): A list of the chosen gadgets.
    """
    print("\nChoose 2 gadgets to equip your spy with:")
    gadgets = ["Grappling Hook", "Night-Vision Goggles", "Hacking Kit", "Lockpick", "Jetpack"]
    gadget_picks = []
    for i in range(2):
        print("Available Gadgets:")
        for i, gadget in enumerate(gadgets, 1):
            print(f" {i}. {gadget}")
        gadget_choice = check_input.get_int_range("Gadget Choice: ", 1, len(gadgets))
        g = gadgets[gadget_choice - 1]
        gadget_picks.append(g)
        gadgets.pop(gadget_choice - 1)
    return gadget_picks


def cliffside_entry(spy):
    """
    Spy must climb up the cliff. If agaility is 6 or higher, they automatically pass. 
    Otherwise, they have to play a guessing game to find the safe path up the cliff. 
    They have 3 tries to guess a random number between 1 and 5. If they guess correctly, they pass, otherwise they fail.
    Parameters:
        spy (Spy): The spy object attempting the challenge.
    Returns:
        bool: True if the challenge is passed, False otherwise.
    """
    print("\n=== Cliffside Entry ===")
    print("The front gate is too heavily guarded. You approach from the outside cliff and must scale the rock wall to reach a hidden entrance.")
    if int(spy.agility()) >= 6:
        #High enough agility is an automatic pass.
        print("With your impressive agility, you easily climb the cliff and reach the hidden entrance without any issues.")
        return True
    else:
        #Main challenge: player must choose the correct path to climb the cliff. 3 attempts allowed.
        print("Without enough climbing ability, the cliffside is dangerous.\nYou search for a stable handhold in the rock face.")
        print("Guess the correct ledge number from 1 to 5. You get 3 tries.")
        safe_path = random.randint(1, 5)
        for i in range(3):
            path_choice = check_input.get_int_range(f"Guess ({i + 1}/3): ", 1, 5)
            if path_choice == safe_path:
                print("You find the right foothold and pull yourself up.")
                return True
            else:
                print("The rock pulls loose. That wasn't it, try another one.")
        print("You have failed to climb the cliff.")
        return False


def laser_grid_hallway(spy):
    """
    Spy must navigate through a hallway filled with moving laser beams. If stealth is 6 or higher, they automatically pass.
    Otherwise, they must memorize a random sequence of 4 directions (Up, Down, Left, Right) and input it correctly to pass. If they input the wrong sequence, they fail.
    Parameters:
        spy (Spy): The spy object attempting the challenge.
    Returns:
        bool: True if the challenge is passed, False otherwise.
    """
    print("\n=== Laser Grid Hallway ===")
    print("A dark corridor is filled with moving laser beams. You must slip through without touching the grid and alerting security.")
    if int(spy.stealth()) >= 6:
        #High enough stealth is an automatic pass.
        print("Your exceptional stealth allows you to navigate through the laser grid undetected, avoiding all beams with ease.")
        return True
    else:
        #Main challenge: memorize a randomized sequence of 4 directions (U, D, L, or R)
        sequence = [random.choice(["U", "D", "L", "R"]) for _ in range(4)]
        print("You need to memorize the sequence of safe movements [(U)p, (D)own, (L)eft, (R)ight] to get through the laser grid.\n")
        print("Sequence:")
        for direction in sequence:
            print(direction, end=' ')
        input("\nPress Enter when you are ready to input the sequence...")
        os.system('cls' if os.name == 'nt' else 'clear') 
        for i in range(4):
            move = check_input.get_direction(f"Move {i + 1}: ")
            if move != sequence[i]:
                print("You triggered a laser beam! Security arrived to capture you.")
                return False
        print("You successfully navigated through the laser grid without triggering any alarms!")
        return True

def ventilation_shaft(spy):
    """
    Spy must climb up a vertical vent shaft. If agility is 6 or higher, they automatically pass. 
    Otherwise, they have to quickly tap the 'C' key 5 times to climb through the shaft.
    Parameters:
        spy (Spy): The spy object attempting the challenge.
    Returns:
        bool: True if the challenge is passed, False otherwise.
    """
    print("\n=== Ventilation Shaft ===")
    print("Inside the facility, a vertical vent shaft is the only path upward. You need enough climbing ability to move through it quickly and quietly.")
    
    if int(spy.agility()) >= 6:
        print("Your impressive agility allows you to climb through the ventilation shaft with ease, avoiding any noise or obstacles.")
        return True
    else:
        print("You wedge yourself inside and have to pull upward one section at a time.\n To make it through, press Enter 5 times to keep climbing.")
        for i in range(5):
            key = input(f"Pull {i + 1}/5: ")
            while key != '':
                key = input("Incorrect key. Press 'Enter' to climb: ")
        print("You successfully climbed through the ventilation shaft!")

    return True

def security_terminal(spy):
    """
    Spy must bypass a security terminal to open the blast door. If tech ability is 6 or higher, they automatically pass.
    Otherwise, they must guess a random pattern of 3 characters (X and O) to bypass the terminal. They have 3 tries to guess the correct pattern. 
    Parameters:
        spy (Spy): The spy object attempting the challenge.
    Returns:
        bool: True if the challenge is passed, False otherwise.
    """
    print("\n=== Security Terminal ===")
    print("A locked security terminal controls the final blast door. You need to bypass its access system before reaching the inner chamber.")

    if int(spy.tech_ability()) >= 6:
        print("Your abilities and gadgets easily allow you to hack the security terminal...")
        return True
    else:
        print("Your hacking abilities aren't good enough to bypass the terminal instantly.\nYou must crack the door's 3-symbol security code.")
        print("The code uses only X and O.\nYou have 3 tries.")
        pattern = [random.choice(['X', 'O']) for _ in range(3)]
        for i in range(3):
            guess = input(f"Attempt {i + 1}/3: ").upper()
            while len(guess) != 3 or any(c not in ['X', 'O'] for c in guess):
                guess = input("Invalid input. Enter your guess (3 characters of 'X' and 'O'): ").upper()
            correct_count = sum(1 for g, p in zip(guess, pattern) if g == p)
            if correct_count == 3:
                print("Access granted. The terminal unlocks the door.")
                return True
            else:
                print(f"Access denied. {correct_count} symbol(s) are in the correct position.")
        print("You failed to bypass the security terminal. Security has been alerted!")
        return False
    return True


def main():
    print("\n=== Spy Infiltration: Villain's Lair ===\nChoose a spy, equip 2 gadgets, and infiltrate the lair.")
    #Player chooses a base spy type
    spy = choose_spy()
    print(spy)
    #Player adds two gadgets to their spy
    gadgets = choose_gadgets(spy)
    for gadget in gadgets:
        if gadget == "Grappling Hook":
            spy = grapplinghook.GrapplingHook(spy)
        elif gadget == "Night-Vision Goggles":
            spy = goggles.Goggles(spy)
        elif gadget == "Hacking Kit":
            spy = hackingkit.HackingKit(spy)
        elif gadget == "Lockpick":
            spy = lockpick.Lockpick(spy)
        elif gadget == "Jetpack":
            spy = jetpack.Jetpack(spy)
    print(spy)
    print("\nYou approach the villain's lair and must face 4 challenges to infiltrate it.")
    game_active = True
    #Challenge 1: Cliffside Entry
    if game_active:
        game_active = cliffside_entry(spy)
    #Challenge 2: Laser Grid Hallway
    if game_active:
        game_active = laser_grid_hallway(spy)
    #Challenge 3: Ventilation Shaft
    if game_active:
        game_active = ventilation_shaft(spy)
    #Challenge 4: Security Terminal
    if game_active:
        game_active = security_terminal(spy)
    #Game outcome
    if game_active:
        print("\nMission Complete!\nYou have successfully infiltrated the villain's lair!")
    if not game_active:
        print("\nMission Failed. Better luck next time!")


if __name__ == "__main__":
    main()
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
        print("Without enough agility, you must be careful climbing the cliff.\nYou need to find the most stable path to prevent yourself from falling.")
        safe_path = random.randint(1, 5)
        for i in range(3):
            path_choice = check_input.get_int_range("Choose a path (1-5): ", 1, 5)
            if path_choice == safe_path:
                print("You found the safe path and successfully climbed the cliff!")
                return True
            else:
                print("That path was unstable! You slip and fall back down. Try again.")
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
        #Main challenge: memorize a randomized sequence of 4 directions (Up, Down, Left, or Right)
        sequence = [random.choice(["Up", "Down", "Left", "Right"]) for _ in range(4)]
        print("You need to memorize the sequence of safe movements to get through the laser grid.")
        print("Sequence:", sequence)
        input("Press Enter when you are ready to input the sequence...")
        os.system('cls' if os.name == 'nt' else 'clear') 
        for i in range(4):
            move = input(f"Move {i + 1}: ").capitalize()
            if move != sequence[i]:
                print("You triggered a laser beam! Security arrived to capture you.")
                return False
        print("You successfully navigated through the laser grid without triggering any alarms!")
        return True


def ventilation_shaft(spy):
    print("\n=== Ventilation Shaft ===")
    print("Inside the facility, a vertical vent shaft is the only path upward. You need enough climbing ability to move through it quickly and quietly.")
    #TODO
    return True


def security_terminal(spy):
    print("\n=== Security Terminal ===")
    print("A locked security terminal controls the final blast door. You need to bypass its access system before reaching the inner chamber.")
    #TODO
    return True


def main():
    print("=== Spy Infiltration: Villain's Lair ===\nChoose a spy, equip 2 gadgets, and infiltrate the lair.")
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
        print("\nCongratulations! You have successfully infiltrated the villain's lair!")
    if not game_active:
        print("\nMission Failed. Better luck next time!")


if __name__ == "__main__":
    main()
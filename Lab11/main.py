import check_input
import beg_factory
import exp_factory
import hero


def main():
    print("Monster Trials")

    #Ask user for their name and create a hero with that name.
    name = input("What is your name? ")
    Player = hero.Hero(name)
    print(f"Welcome, {name}, to the Monster Trials! You will be fighting against 3 monsters. Defeat them all to win!")

    #Ask user for the difficulty they want to play on. If they choose beginner, create a BegFactory. If they choose expert, create an ExpertFactory.
    difficulty = check_input.get_int_range("Choose your difficulty: \n1. Beginner\n2. Expert\n", 1, 2)
    if difficulty == 1:
        factory = beg_factory.BeginnerFactory()
    else:
        factory = exp_factory.ExpertFactory()

    #Use the factory to create a list of 3 random enemies and put them into a list.
    enemy_list = []
    for i in range(3):
        enemy_list.append(factory.create_random_enemy())

    play = True
    while(play):
        #Print the list of enemies.
        print("\nChoose an enemy to attack: ")
        for i, enemy in enumerate(enemy_list, 1):
            print(f"{i}. {enemy}")
        
        choice = check_input.get_int_range("Enter Choice: ", 1, len(enemy_list))

        print(f"\n{Player._name}'s HP: {Player._hp}")
        print("1. Melee Attack\n2. Ranged Attack")
        attack_choice = check_input.get_int_range("Enter Choice: ", 1, 2)
        print(attack_choice)

        if attack_choice == 1:
            print(Player.melee_attack(enemy_list[choice - 1]))
        if attack_choice == 2:
            print(Player.ranged_attack(enemy_list[choice - 1]))

        if enemy_list[choice - 1]._hp == 0:
            print(f"You have slain the {enemy_list[choice - 1]._name}")
            enemy_list.pop(choice - 1)
        elif(enemy_list[choice - 1]._hp > 0):
            print(enemy_list[choice - 1].melee_attack(Player))
            #test print players new hp after attack
            print(f"{Player._name}'s HP: {Player._hp}")


        if enemy_list == []:
            print("\nCongratulations! You have defeated all three monsters!\nGame Over\n")
            play = False
        elif Player._hp == 0:
            print("\nYou have been defeated by the monsters...\nGame Over\n")
            play = False


if __name__ == "__main__":
    main()
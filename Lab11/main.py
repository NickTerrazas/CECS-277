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
        for enemy in enemy_list:
            print(enemy)
        


if __name__ == "__main__":
    main()
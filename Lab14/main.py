#Nicholas Terrazas and Devin Heinemann
#Lab 14
#05/4/2026

# Description:


import puppy
import state_asleep
import state_play
import state_feed
import check_input

def main():
    Pup = puppy.Puppy()
    print("Congratulations on your new puppy!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed the puppy")
        print("2. Play with the puppy")
        print("3. Quit")
        choice = check_input.get_int("Enter your choice (1-3): ", 1, 3)

        if choice == 1:
            print(Pup.give_food())
        elif choice == 2:
            print(Pup.throw_ball())
        elif choice == 3:
            print("Your puppy falls asleep for the day. Thanks for playing with your puppy!")
            break

if __name__ == "__main__":
    main()

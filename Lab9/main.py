#Nicholas Terrazas and Devin Heinemann
#Lab 9
#03/16/2026

# Description: 
'''

'''

import abc
import random
from check_input import get_int_range
import car
import motorcycle
import truck

def main():
    c = car.Car("Lightning Car", "C", 7)
    b = motorcycle.Motorcycle("Swift Bike", "M", 8)
    t = truck.Truck("Behemoth Truck", "T", 6)

    track = [["_" for i in range(100)] for j in range(3)]
    for i in range(3):
        for j in range(2):
            obs_loc = random.randint(1, 98)
            track[i][obs_loc] = "O"
    

    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('O') or else you'll crash!")
    print("1. Lightning Car - a fast car. Speed: 7. Special: Nitro Boost (1.5x speed).")
    print("2. Swift Bike - a speedy motorcycle. Speed: 8. Special: Wheelie (2x speed but there's a chance you'll wipe out).")
    print("3. Behemoth Truck - a heavy truck. Speed: 6. Special: Ram (2x speed and it smashes through obstacles).")
    choice = get_int_range("Choose your vehicle (1-3): ", 1, 3)

    if choice == 1:
        p = car.Car("Lightning Car", "P", 7)
        b = motorcycle.Motorcycle("Swift Bike", "M", 8)
        t = truck.Truck("Behemoth Truck", "T", 6)
    elif choice == 2:
        c = car.Car("Lightning Car", "C", 7)
        p = motorcycle.Motorcycle("Swift Bike", "P", 8)
        t = truck.Truck("Behemoth Truck", "T", 6)
    else:
        c = car.Car("Lightning Car", "C", 7)
        b = motorcycle.Motorcycle("Swift Bike", "M", 8)
        p = truck.Truck("Behemoth Truck", "P", 6)

    

    for lane in track:
        print(" ".join(lane))





if __name__ == "__main__":
    main()
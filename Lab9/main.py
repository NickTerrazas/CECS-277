#Nicholas Terrazas and Devin Heinemann
#Lab 9
#03/16/2026

# Description: 

import abc
import random
from check_input import get_int_range
import vehicle
import car
import motorcycle
import truck

def main():
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('O') or else you'll crash!")
    print("1. Lightning Car - a fast car. Speed: 7. Special: Nitro Boost (1.5x speed).")
    print("2. Swift Bike - a speedy motorcycle. Speed: 8. Special: Wheelie (2x speed but there's a chance you'll wipe out).")
    print("3. Behemoth Truck - a heavy truck. Speed: 6. Special: Ram (2x speed and it smashes through obstacles).")
    choice = get_int_range("Choose your vehicle (1-3): ", 1, 3)




if __name__ == "__main__":
    main()
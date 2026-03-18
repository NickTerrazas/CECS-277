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

    #Constructs the tracks and randomly places 2 obstackes in each lane.
    track = [["_" for i in range(100)] for j in range(3)]
    for i in range(3):
        for j in range(2):
            obs_loc = random.randint(1, 98)
            track[i][obs_loc] = "O"
    
    #Information display for player to choose their vehicle.
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('O') or else you'll crash!")
    print("1. Lightning Car - a fast car. Speed: 7. Special: Nitro Boost (1.5x speed).")
    print("2. Swift Bike - a speedy motorcycle. Speed: 8. Special: Wheelie (2x speed but there's a chance you'll wipe out).")
    print("3. Behemoth Truck - a heavy truck. Speed: 6. Special: Ram (2x speed and it smashes through obstacles).")
    v_choice = get_int_range("Choose your vehicle (1-3): ", 1, 3)

    #Creates the vehicles in a list.
    vehicles = [car.Car("Lightning Car", "P", 7), motorcycle.Motorcycle("Swift Bike", "M", 8), truck.Truck("Behemoth Truck", "T", 6)]
    track[0][0] = "C"
    track[1][0] = "M"
    track[2][0] = "T"
    c = vehicles[0]
    m = vehicles[1]
    t = vehicles[2]
    
    #Sets the player and other vehicles

    #need to also assign variables for the other vehicles so they can be displayed in the status updates and track display.
    p = vehicles[v_choice - 1]
    if v_choice == 1:
        #Player is the car
        track[0][0] = "P"
        c = p
        op1 = vehicles[1]
        op2 = vehicles[2]
    elif v_choice == 2:
        #Player is the motorcycle
        track[1][0] = "P"
        m = p
        op1 = vehicles[0]
        op2 = vehicles[2]
    else:
        #Player is the truck
        track[2][0] = "P"
        t = p
        op1 = vehicles[0]
        op2 = vehicles[1]

    #Game Loop.
    p_finish = False
    op1_finish = False
    op2_finish = False
    while not p_finish:

        print("\nLightning Car [Position - " + str(c._position) + ", Energy - " + str(c._energy) + "]")
        print("Swift Bike [Position - " + str(m._position) + ", Energy - " + str(m._energy) + "]")
        print("Behemoth Truck [Position - " + str(t._position) + ", Energy - " + str(t._energy) + "]\n")

        #Displays the track.
        for lane in track:
            print(" ".join(lane))

        #Figures out where the next obstacle in the track is, otherwise automatically gets set to the end of the track.
        next_obs = 100
        loc_test = 99
        while loc_test > p._position:
            if track[v_choice - 1][loc_test] == "O":
                next_obs = loc_test
            loc_test -= 1

        #Player chooses their movement.
        move_choice = get_int_range("Choose action (1. Fast, 2. Slow, 3. Special Move): ", 1, 3)
        if move_choice == 1:
            print(p.fast(next_obs))
        elif move_choice == 2:
            print(p.slow(next_obs))
        elif move_choice == 3:
            print(p.special_move(next_obs))

        if not op1_finish:
            move_choice = random.randint(1, 3)
            if move_choice == 1:
                print(op1.fast(next_obs))
            elif move_choice == 2:
                print(op1.slow(next_obs))
            elif move_choice == 3:
                print(op1.special_move(next_obs))
        if not op2_finish:  
            move_choice = random.randint(1, 3)
            if move_choice == 1:
                print(op2.fast(next_obs))
            elif move_choice == 2:
                print(op2.slow(next_obs))
            elif move_choice == 3:
                print(op2.special_move(next_obs))
        
        #Makes sure no vehicle goes past the end of the track.
        if p._position >= 99:
            p._position = 99
        if op1._position >= 99:
            op1._position = 99
            op1_finish = True
        if op2._position >= 99:
            op2._position = 99
            op2_finish = True

        #Updates the display for all vehicles.
        for loc in range(len(track[v_choice - 1])):
            if track[v_choice - 1][loc] == "P":
                track[v_choice - 1][loc] = "*"
                track[v_choice - 1][p._position] = "P"
        
        #TODO
        #Check if the other vehicles have finished and stop them from making choices
        #Add individual obstavle detection for the other vehicles so they can also crash into them or dodge them in their own lane.
        #Currently all vehicles are just reacting to the player's next obstacle, but they should be able to react to their own obstacles as well. This will require some changes to the movement methods in the vehicle classes so they can take in a list of obstacles instead of just one, and then determine which one is the next one for that specific vehicle.


        #Updates the display for the other vehicles.
        for loc in range(len(track[0])):
            if track[0][loc] == "C":
                track[0][loc] = "*"
                track[0][c._position] = "C"
        for loc in range(len(track[1])):
            if track[1][loc] == "M":
                track[1][loc] = "*"
                track[1][m._position] = "M"
        for loc in range(len(track[2])):
            if track[2][loc] == "T":
                track[2][loc] = "*"
                track[2][t._position] = "T"

        #Player finish detection
        if (v_choice == 1 and track [0][99] == "P") or (v_choice == 2 and track [1][99] == "P") or (v_choice == 3 and track [2][99] == "P"):
            p_finish = True



    #Need another loop to make sure the rest of the vehicles finish the race.



if __name__ == "__main__":
    main()
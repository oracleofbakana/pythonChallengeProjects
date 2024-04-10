print("Welcome to Treasure Island game \nYour mission is to find the hidden treasure\n")
direction = input("Enter your direction. Left or Right\n").lower()

if direction == "left":
    direction = input("Swim or Wait. Enter Left or Right\n").lower()
    if direction == "left":
        direction = input("Which door? Red,Blue or Yellow\n").lower()
        if direction == "yellow":
            print("YOU WIN")
        elif direction == "red":
            print("Burned By fire. Game Over")
        elif direction == "blue":
            print("Eaten By Beasts. Game Over")
        else:
            print("You LOST. Game Over")
    else:
        print("Attacked by trout. Game Over")
else:
    print("Fall into a hole. Game Over")

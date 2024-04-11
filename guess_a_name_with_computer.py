import random

print("Welcome to the Guess Game with Computer\n")
computerNumber = random.randint(0, 100)
print("Guess a number between 1 and 100 \n")

userGuess = 1
playerNumbers = []

while userGuess <= 3:
    userNumber = int(input("Enter a number\n"))
    if computerNumber == userNumber:
        print(f"Congratulations!You chose the right numbers in {userGuess}x time")
        exit()
    elif computerNumber <= userNumber:
        playerNumbers.append(userNumber)
        print(f"The number is too low. You have {3 - userGuess} tries")
    else:
        playerNumbers.append(userNumber)
        print(f"The number is too high.You have {3 - userGuess} tries. You entered {playerNumbers}")
    userGuess += 1

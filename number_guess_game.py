import random
from art import number_guess
EASY_LEVEL = 10
HARD_LEVEL = 5


def random_pick():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
    user_guess = random.choice(numbers)
    return user_guess


def compare(number_picked, user_guess):
    if user_guess > 50:
        return 4
    elif user_guess == number_picked:
        return 1
    elif user_guess > number_picked:
        return 2
    elif user_guess < number_picked:
        return 3


def user_trial():
    trial = int(input(f"To play the game, enter a number: /n"))
    return trial


def set_difficulty():
    difficulty = str(input(f"Choose your difficulty level. Type 'hard' for hard and 'easy' for easy: \n"))
    if difficulty == 'hard':
        return HARD_LEVEL
    else:
        return EASY_LEVEL


def play_game():
    print(number_guess)
    computer_pick = random_pick()
    attempt = set_difficulty()

    while attempt >= 0:
        if attempt == 0:
            print("You have run out of guess. You lose.")
            play_game()
        else:
            user_pick = user_trial()
            result = compare(computer_pick, user_pick)

            if result == 1:
                print(f"You won the game. You picked the correct number")
                if input(f"Do you want to play again: Type 'y' to continue") == 'y': play_game()
            elif result == 2:
                print(f"Number is too high. You have {attempt - 1} left")
            elif result == 3:
                print(f"Number is too low. You have {attempt - 1} left")
            elif result == 4:
                print(f"Your guess should be between 1 and 50. You have {attempt - 1} left")
            attempt -= 1


while input(f"Type 'y' to play the number guess game and 'n' to exit:\n") == "y":
    play_game()

from art import higher_lower, vs
import random
from game_data import data

def format_data(account):
    """ Format the account data into printable format"""
    account_name = account["name"]
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user's guess and the followers count and check whether they got it right or wrong"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(higher_lower)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    guess = input(f"Who has more followers? A or B?.").lower()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
    else:
        print(f"Sorry that's wrong. Final score is {score}.")
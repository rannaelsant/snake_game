import random as rd
from data import data
from art import logo, vs
print(logo)
score = 0
game_should_continue = True
account_b = rd.choice(data)

"""Takes the account data and returns the printables format."""
def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}."


def check_answer(guess, a_followers, b_followers):
    """"Take the user guess and follower count and rerturns if they got it right"""
    #if a_followers > b_followers and guess == "a": or
    if a_followers > b_followers:
        """if guess == "a":
            return True
        else:
            return False"""
        return guess == "a" # if alternative is "a" be true, if "b" is false
    else:
        return guess == "b"

while game_should_continue:
    account_a = account_b
    account_b = rd.choice(data)
    if account_a == account_b:
        account_b = rd.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? 'A' or 'B':").lower()

    a_follower_count = account_a("follower_count")
    b_follower_count = account_b("follower_count")
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong! Final score: {score}")
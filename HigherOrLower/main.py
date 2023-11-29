from game_data import data
from art import logo, vs
from os import system

import random

SIZE = len(data) - 1

def structure_info_into_string(person):
    name = person["name"]
    description = person["description"]
    origin = person["country"]
    if description[0].lower() in ('a', 'e', 'i', 'o', 'u'):
        article = "an"
    else:
        article = "a"
    
    return f"{name}, {article} {description}, from {origin}"

def print_compare(first, second):
    print(f"Compare A: {structure_info_into_string(first)}.")
    print(vs)
    print(f"Against B: {structure_info_into_string(second)}.")

def check_user_guess(first, second, guess):
    if guess.lower() == "b":
        return second["follower_count"] > first["follower_count"]
    else:
        return first["follower_count"] > second["follower_count"]
    
def execute():
    final_score = 0
    failed = False
    while not failed:
        first = data[random.randint(0, SIZE)]
        second = data[random.randint(0, SIZE)]
        print_compare(first, second)
        user_guess = input("Who has more followers? Type 'A' or 'B': ")
        if not check_user_guess(first, second, user_guess):
            failed = True
            system("cls")
            print(logo)
            print(F"Sorry, that's wrong. Final score: {final_score}")
        else:
            final_score += 1
            system("cls")
            print(logo)
            print(f"You're right! Current score: {final_score}.")



def main():
    print(logo)
    print("Welcome to Higher or Lower game!")

    keepGoing = True
    while keepGoing:
        execute()
        shouldProceed = input("Would you want to try another round? (Y/N) ")
        if shouldProceed.lower() == "n":
            keepGoing = False
        else:
            system("cls")
            print(logo)

    print("It was a fun game. Bye!")

main()

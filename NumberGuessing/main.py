import random
from art import logo
from os import system

def play_game():
    system("cls")
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty.lower() == "easy":
        attempts_amount = 10
    else:
        attempts_amount = 5

    guessed_number = random.randint(1, 100)

    while attempts_amount > 0:
        print(f"You have {attempts_amount} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > guessed_number:
            print("Too high.")
            attempts_amount -= 1
        elif guess < guessed_number:
            print("Too low.")
            attempts_amount -= 1
        else:
            print("You got it!")
            return
        
    print("You've run out of attempts. Game over.")

def main():
    print("Welcome to the Number Guseeing Game!")
    while True:
        play_game()
        user_input = input("Would you like to try again? (Y/N) ")
        if user_input.lower() == "n":
            print("It was a fun game. Bye.")
            return

main()

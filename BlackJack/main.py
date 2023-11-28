############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################
 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The computer is the dealer.

import random
from art import logo
from os import system

def fill_in_the_deck():
    deck = []
    for value in range(2, 12):
        for sign in range(0, 4):
            deck.append(value)
    return deck

def draw_random_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def display_hand(hand, source):
    print(f"{source} hand is : {hand}")

def display_dealer_hand(hand):
    displayed_hand = []
    for index in range(0, len(hand)):
        if index == 0:
            displayed_hand.append(hand[index])
        else:
            displayed_hand.append("?")
    print(f"Dealer's hand is {displayed_hand}")

def calculate_score(hand):
    current_sum = sum(hand)
    if current_sum > 21 and 11 in hand:
        current_sum -= 10
    return current_sum

def compare_final_scores(dealer_hand, user_hand):
    dealer_score = calculate_score(dealer_hand)
    user_score = calculate_score(user_hand)

    display_hand(dealer_hand, "Dealer's")
    print(f"Dealer's score is {dealer_score}")
    display_hand(user_hand, "Your")
    print(f"Your score is {user_score}")

    if dealer_score > 21:
        print("You won. Congrats!")
        return
    
    if dealer_score > user_score:
        print("Dealer won. Game over.")
        return
    
    if user_score > dealer_score:
        print("You won. Congrats!")
        return
    
    print("Draw.")
    

def execute():
    system("cls")
    print(logo)
    print("Welcome to BlackJack game.")

    current_deck = fill_in_the_deck()

    dealer_hand = []
    user_hand = []

    dealer_hand.append(draw_random_card(current_deck))
    user_hand.append(draw_random_card(current_deck))

    dealer_hand.append(draw_random_card(current_deck))
    user_hand.append(draw_random_card(current_deck))

    display_dealer_hand(dealer_hand)
    display_hand(user_hand, "Your")

    dealer_score = calculate_score(dealer_hand)
    if dealer_score == 21:
        display_hand(user_hand, "Dealer's")
        print("The dealer has a BlackJack! Game over.")
        return
    
    user_score = calculate_score(user_hand)
    if user_score == 21:
        print("You have a BlackJack! Congrats.")
        return

    keepGoing = True
    while keepGoing:
        user_input = input("Would you like to draw another card? (Y/N) ")
        if user_input.lower() == "n":
            break
        
        user_hand.append(draw_random_card(current_deck))
        user_score = calculate_score(user_hand)
        
        display_hand(user_hand, "Your")

        if user_score > 21:
            print("You've lost. Game over.")
            return
        if user_score == 21:
            break
    
    dealer_score = calculate_score(dealer_hand)
    while dealer_score <= 16:
        dealer_hand.append(draw_random_card(current_deck))
        dealer_score = calculate_score(dealer_hand)

    compare_final_scores(dealer_hand, user_hand)

def main():
    
    keepGoing = True
    while keepGoing:
        execute()
        user_input = input("Would you like to try again? (Y/N) ")
        if user_input.lower() == "n":
            break
    
    print("It was a nice game. Bye.")

main()

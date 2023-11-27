from os import system
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bids = {}

shouldQuit = False
while not shouldQuit:
    name = input("What is you name? ")
    bid = input("What is your bid? $")
    bids[name] = int(bid)
    checkOthers = input("Are there any other bidders? Type 'yes' or 'no'.")
    if checkOthers.lower() == "no":
        shouldQuit = True
    else:
        system("cls")

max = 0
winner_name = ""
for bidder in bids:
    if bids[bidder] > max:
        max = bids[bidder]
        winner_name = bidder

print(f"The winner is {winner_name} with a bid of ${max}")

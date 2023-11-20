import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_choice < 0 or user_choice > 2:
    print("You typed wrong number. You loose!")
    exit(0)

print(choices[user_choice])

computer_choice = random.randint(0, 2)

print("Computer chose:")

print(choices[computer_choice])

match user_choice:
    case 0:
        if computer_choice == 1:
            print("You lost.")
        else:
            print("You won.")
    case 1:
        if computer_choice == 2:
            print("You lost.")
        else:
            print("You won.")
    case 2:
        if computer_choice == 0:
            print("You lost.")
        else:
            print("You won.")

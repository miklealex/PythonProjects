print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

can_proceed = False
while can_proceed == False:
    turn = input("You're currently on a crossroad. Would you like to turn left or right? (left/right)")
    if turn.upper() != "LEFT" and turn.upper() != "RIGHT":
        print("Unfortunately, no other path is available. You have to choose either right or left.\n Please, try again.")
        can_proceed = False
    elif turn.upper() == "RIGHT":
        print("You've faced a bear. He eats you. Game over.")
        exit(0)
    else:
        can_proceed = True

can_proceed = False

while can_proceed == False:
    choice = input("You've reached the river. Would you like to swim or wait for a boat?(swim/wait)")
    if choice.upper() != "SWIM" and choice.upper() != "WAIT":
        print("There is no other way to cross this river. You have to choose either swim or wait.\n Please, try again.")
        can_proceed = False
    elif choice.upper() == "SWIM":
        print("The river is full of snakes. They choke you. Game over.")
        exit(0)
    else:
        can_proceed = True

can_proceed = False

while can_proceed == False:
    print("You've crossed the river, found the mansion and standing in front of three doors - red, blue and green.")
    choice = input("Which one would you choose to open?(red/blue/green)")
    if choice.upper() != "RED" and choice.upper() != "BLUE" and choice.upper() != "GREEN":
        print("There are only these three colors. YOu have to pick among them.\n Please, try again.")
        can_proceed = False
    elif choice.upper() == "RED":
        print("You are opening the door and a hunter shoots you right away. Game over.")
        exit(0)
    elif choice.upper() == "GREEN":
        print("You are entering the room full of strange enormous plants. It appears, they'e venomous. They eat you. Game over.")
    else:
        can_proceed = True

print("You're entering a dark room. A single gleam of light falls onto a pedestal in the center of a room. There is a chest full of gold. You found a treasure!")
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins_reserve = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

def calculateCoins(coins):
    totalMoney = 0
    totalMoney += coins['quarters']*0.25
    totalMoney += coins['dimes']*0.1
    totalMoney += coins['nickels']*0.05
    totalMoney += coins['pennies']*0.01
    return totalMoney

def printReport():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${calculateCoins(coins_reserve)}")
    return True

def insertCoinsPrompt():
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))
    money = {"quarters" : quarters, "dimes": dimes, "nickels": nickels, "pennies": pennies}
    return money

def checkIfEnoughResources(drink):
    if drink not in MENU:
        return False, "ERROR"
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if item not in resources:
            return False, "ERROR"
        if resources[item] < ingredients[item]:
            return False, item
    return True, ""

def useResources(drink):
    if drink not in MENU:
        return
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]

def addCoinsToReserve(coins):
    for coin_type in coins:
        coins_reserve[coin_type] += coins[coin_type]

def getChange(amount):
    amount = round(amount, 2)
    if amount == 0:
        return True, 0
    current_value = 0
    while coins_reserve["quarters"] and amount - current_value >= 0.25:
        current_value += 0.25
        coins_reserve["quarters"] -= 1

    while coins_reserve["dimes"] and amount - current_value >= 0.1:
        current_value += 0.1
        coins_reserve["dimes"] -= 1

    while coins_reserve["nickels"] and amount - current_value >= 0.05:
        current_value += 0.05
        coins_reserve["nickels"] -= 1

    while coins_reserve["pennies"] and amount - current_value >= 0.01:
        current_value += 0.01
        coins_reserve["pennies"] -= 1

    if amount - current_value != 0:
        return False, current_value
    return True, current_value

def makeCoffe(drink):
    status, item = checkIfEnoughResources(drink)
    if not status:
        print(f"Sorry there is not enough {item}")
        return True

    inserted_money = insertCoinsPrompt()
    total_money = calculateCoins(inserted_money)
    if total_money < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return True

    useResources(drink)
    addCoinsToReserve(inserted_money)
    expected_change = total_money - MENU[drink]["cost"]
    if expected_change == 0:
        print(f"Here is your {drink}. Enjoy!")
        return True

    status, change = getChange(expected_change)
    if not status:
        print(f"Issues with the change. You only get back ${change}")
        print(f"Here is your {drink}. Enjoy!")
        return True

    print(f"Here is ${change} in change.")
    print(f"Here is your {drink}. Enjoy!")
    return True

def shouldQuit(user_input):
    return user_input.lower() == "off"

def shouldPrintReport(user_input):
    return user_input.lower() == "report"

def shouldMakeCoffee(user_input):
    return user_input.lower() in MENU

def inputToActionMapping(user_input):
    if shouldQuit(user_input):
        return lambda _: False
    if shouldPrintReport(user_input):
        return lambda _: printReport()
    if shouldMakeCoffee(user_input):
        return lambda _: makeCoffe(user_input)
    else:
        print("Unknown input")
        return lambda _: True

def execute(user_input):
    action = inputToActionMapping(user_input)
    return action(None)


def main():
    keepGoing = True
    while keepGoing:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        keepGoing = execute(user_input)

main()

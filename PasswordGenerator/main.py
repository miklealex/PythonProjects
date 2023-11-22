import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def all_numbers(inputStr):
    return all(char.isdigit() for char in inputStr)

def handle_integer_input(collection_name):
    while True:
        output_str = "How many " + collection_name + " would you like in your password?"
        value = input(output_str)
        if not all_numbers(value):
            print("Please, enter a valid digit")
        else:
            return int(value)

def random_pick_from_container_to_pwd(container, amount_of_items, pwd):
    for iteration in range(1, amount_of_items + 1):
        pwd += random.choice(container)
    return pwd

print("Welcome to the PyPassword Generator!")
letters_amount = handle_integer_input("letters")
symbols_amount = handle_integer_input("symbols")
numbers_amount = handle_integer_input("numbers")

resultedPwd = ""
total_amount_of_characters = letters_amount + symbols_amount + numbers_amount

resultedPwd = random_pick_from_container_to_pwd(letters, letters_amount, resultedPwd)
resultedPwd = random_pick_from_container_to_pwd(symbols, symbols_amount, resultedPwd)
resultedPwd = random_pick_from_container_to_pwd(numbers, numbers_amount, resultedPwd)

l = list(resultedPwd)
random.shuffle(l)
resultedPwd = ''.join(l)

print(f"Here is your password: {resultedPwd}")

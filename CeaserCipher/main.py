from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def ceasar(input_message, action, shift_key):
    result = ""
    if action == "decrypt":
        shift_key *= -1
    for letter in input_message:
        if letter in alphabet:
            current_position = alphabet.index(letter)
            new_position = (current_position + shift_key) % len(alphabet)
            result += alphabet[new_position]
        else:
            result += letter
    return result

print("Welcome to Ceasar Cipher method.")

while True:
    message = input("Please, enter your message: ")
    action = input("Please, select whether you want to encrypt or decrypt the message? ")
    shift_key = int(input("Please, enter shift key: "))

    print(f"The result is {ceasar(message.lower(), action, shift_key)}")
    again = input("Would you like to go again? y/n")
    if again.lower() == 'n':
        print("Good bye")
        break

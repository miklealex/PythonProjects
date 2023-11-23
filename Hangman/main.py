import random
from os import system
from hangman_art import logo, stages
from hangman_words import word_list


generated_word = random.choice(word_list)
generated_word_length = len(generated_word)

user_lives = len(stages) - 1
game_over = False
display_symbols = []
print(generated_word)

for iteration in range(0, generated_word_length):
    display_symbols += '_'

print(logo)

while not game_over:
    system("cls")
    print(display_symbols)
    print(stages[user_lives])

    if not '_' in display_symbols:
        print("You win.")
        break

    guess = input("Guess the letter.")
    
    if not guess in generated_word:
        user_lives -= 1
        if user_lives == 0:
            print("You've lost.")
            print(f"The word was {generated_word}")
            game_over = True
    else:
        for index in range(0, generated_word_length):
            if guess == generated_word[index]:
                display_symbols[index] = guess

print("Game over.")

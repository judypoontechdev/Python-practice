# **Task description** #
# Implements a number guessing game.
# Prompts the user for a level n, generates a secret random integer between 1 and n, 
# and repeatedly prompts the player to guess the target number—outputting "Too small!", 
# "Too large!", or "Just right!" while ignoring any invalid inputs.

import random

def main():

    while True:
        try:
            level = int(input('Level: '))
            if level > 0:
                break
        except ValueError:
            continue

    answer = random.randint(1, level)

    while True:
        try:
            guess = int(input('Guess: '))
            if guess <= 0:
                continue
        except ValueError:
            continue
        else:
            if generate(answer, guess):
                break

def generate(answer, guess):
    if guess < answer:
        print('Too small!')
        return False
    elif guess == answer:
        print('Just right!')
        return True
    else:
        print('Too large!')
        return False

if __name__ == "__main__":
    main()
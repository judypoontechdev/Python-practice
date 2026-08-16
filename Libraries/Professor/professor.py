## Task Description ##
# This program simulates the 'Little Professor' educational toy by prompting the user for
#  a difficulty level (1, 2, or 3) and generating 10 addition problems using randomly 
# generated numbers based on the selected level: 0–9 for Level 1, 10–99 for Level 2, 
# and 100–999 for Level 3. For each problem, it gives the user up to 3 attempts 
# (printing 'EEE' for incorrect answers or non-numeric inputs), reveals the correct 
# answer if all attempts are exhausted, and displays the user's final score out of 
# 10 upon completion.

import random

def main():

    level = get_level()
    total_score = 0

    for _ in range(10):
        num_tries = 0
        x = generate_integer(level)
        y = generate_integer(level)
        actual_answer = x + y

        while num_tries < 3:
            try:
                user_answer = int(input(f'{x} + {y} = '))
            except ValueError:
                num_tries += 1
                print('EEE')
                continue
            else:
                if user_answer != actual_answer:
                    num_tries += 1
                    print('EEE')
                else:
                    total_score += 1
                    break

        if num_tries == 3:
            print(f'{x} + {y} = {actual_answer}')


    print(f'{total_score}')

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
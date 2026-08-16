# **Task description**
# Prompts the user for a fruit name (case-insensitively) and outputs the 
# corresponding number of calories in one portion based on the FDA’s 
# nutrition poster, ignoring invalid entries.

def main():
    # Prompt the user for a fruit name and convert it to lowercase for matching
    fruit_name = input('What fruit do you want to enquire? ').lower()
    check(fruit_name)

def check(f):
    # Dictionary storing the 20 fruits and their corresponding calorie values
    fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
    }

    # Extract all fruit keys into a list for lookup
    a = list(fruits.keys())

    # Check if the entered fruit exists in the list
    if f in a:
        # If found, print the corresponding calorie count
        print(f'Calories: {fruits[f]}')
    else:
        # If not found, ignore and print nothing
        print()

main()

# **Task description**
# Prompts the user for a string of text and outputs it with 
# all uppercase and lowercase vowels (A, E, I, O, U) omitted.

def main():
    # Prompt the user to input a word or string
    word = input('Input: ')
    modify(word)

def modify(word):

    my_list = []

    for w in range(len(word)):
        # Check if the character (converted to lowercase) is NOT a vowel
        if word[w].lower() not in ['a', 'e', 'i', 'o', 'u']:
            my_list.append(word[w])

    # Join all the characters in the list back into a single string
    output = ''.join(my_list)
    print(output)

main()

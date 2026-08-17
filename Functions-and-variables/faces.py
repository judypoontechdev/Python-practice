# **Task description**
# Implements a `convert()` function that replaces emoticons `:)` 
# with `🙂` and `:(` with `🙁`, and a `main()` function to 
# process and display user input.

def main():
    # Get user input and print the converted string with emojis
    text = input('Pls enter your text for conversion: ')
    result = change_emoji(text)
    print(result)

def change_emoji(wordings):
    # Converts :) to 🙂 and :( to 🙁 in the input string
    return wordings.replace(':)', '🙂').replace(':(', '🙁')

main()

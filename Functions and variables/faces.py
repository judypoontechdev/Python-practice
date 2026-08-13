
def main():
    # Get user input and print the converted string with emojis
    text = input('Pls enter your text for conversion: ')
    result = change_emoji(text)
    print(result)

def change_emoji(wordings):
    # Converts :) to 🙂 and :( to 🙁 in the input string
    return wordings.replace(':)', '🙂').replace(':(', '🙁')

main()

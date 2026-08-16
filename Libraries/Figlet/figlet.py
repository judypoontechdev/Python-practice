# **Task description**
# Expects zero command-line arguments (for a random font) or two arguments (`-f` or `--font` 
# followed by a font name), prompts the user for text, and outputs it as ASCII art using 
# `pyfiglet`, exiting with an error message on invalid CLI inputs.

# Import required libraries
import random
from pyfiglet import Figlet
import sys

# Instantiate the Figlet object
figlet = Figlet()

def main():

    # User is expected to input the type of font they
    # desire after the file name before execution.
    # Two different use cases are anticipated

    # Retrieve the list of available fonts
    fonts = figlet.getFonts()

    # Case 1: Zero command-line arguments (random font selection)
    if len(sys.argv) == 1:
        f = random.choice(fonts)
        figlet.setFont(font=f)

     # Case 2: two command-line arguments (-f / --font followed by font name)
        # Validate both the flag and whether the font exists
    elif len(sys.argv) == 3:
        if sys.argv[1] in ['-f', '--font'] and sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit('Invalid usage')

    else:
        sys.exit('Invalid usage')

    # Prompt user for text input and render it using the selected font
    word = input('Input: ')
    print(figlet.renderText(word))

main()
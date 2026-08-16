# **Task description**
# Prompts the user for input and outputs the exact text, 
# replacing every space with `...` (three periods) to 
# simulate a slower playback speed.

# Prompt user for input
wordings = input('Pls enter text: ')
# Replace each space with ...
finalWordings = wordings.replace(' ', '...')
print(finalWordings)

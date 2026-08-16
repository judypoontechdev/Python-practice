# **Task description**
# Prompts the user for a string in English and outputs the "emojized" 
# version by converting any emoji codes or aliases (e.g., `:thumbs_up:` 
# or `:thumbsup:`) into their corresponding emoji.

import emoji

# Prompt user for input
emoji_name = input("Input: ")

# Convert input to emoji using aliases support
output = emoji.emojize(emoji_name, language='alias')

# Output the result
print("Output:", output)
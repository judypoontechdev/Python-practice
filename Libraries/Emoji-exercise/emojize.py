import emoji

# Prompt user for input
emoji_name = input("Input: ")

# Convert input to emoji using aliases support
output = emoji.emojize(emoji_name, language='alias')

# Output the result
print("Output:", output)
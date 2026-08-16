# **Task description**
# Prompts the user for a variable name in camelCase and converts 
# it into Python's recommended snake_case by inserting 
# underscores before uppercase letters and converting them to lowercase.

def main():
    # Prompt the user for camelCase input
    camel = input('camelCase: ')
    snake(camel)

def snake(camel):

     # Define an empty list to store the converted characters
     my_list = []

     # Loop through each character index in the camelCase string
     for c in range(len(camel)):
          # If the character is uppercase, prepend an underscore and convert it to lowercase
          if camel[c].isupper():
               my_list.append('_' + camel[c].lower())
          # Otherwise, keep the lowercase character as it is
          else:
               my_list.append(camel[c])

     # Join all elements in the list into a single string and print the result
     final = ''.join(my_list)
     print(final)

main()

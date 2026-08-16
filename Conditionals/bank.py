## **Task description**
# Prompts the user for a greeting, returning `$0` if it starts 
# with "hello", `$20` if it starts with an "h" (excluding "hello"), and `$100` 
# otherwise, ignoring leading whitespace and casing.

def main():
    # Prompt users for greeting
    greeting = input('Pls input your greeting: ').lower().strip()
    money(greeting)

def money(g):
    if g.startswith('hello'):
        print('$0')
    elif g.startswith('h'):
        print('$20')
    else:
        print('$100')

main()


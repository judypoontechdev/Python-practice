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


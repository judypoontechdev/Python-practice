### Task Description: Adieu, Adieu (`adieu.py`)

# Implement a program that continuously prompts the user for names
# (one per line) until the user terminates input with `Control-D` (`EOFError`).
# The program then outputs a farewell message based on the total number of names provided:

# 1 Name: `Adieu, adieu, to [Name]`
# 2 Names: `Adieu, adieu, to [Name 1] and [Name 2]`
# 3+ Names: `Adieu, adieu, to [Name 1], [Name 2], ..., and [Name N]`


def main():

    names = []

    while True:
        try:
            name = input('Name: ')

            if name.strip():
                names.append(name)
        except EOFError:
            print()
            break

    output(names)

def output(names):
    if len(names) == 1:
        print(f'Adieu, adieu, to {names[0]}')
    elif len(names) == 2:
        print(f'Adieu, adieu, to {names[0]} and {names[1]}')
    else:
        print(f'Adieu, adieu, to {names[0]}, {', '.join(names[1:-1])}, and {names[-1]}')

if __name__ == "__main__":
    main()

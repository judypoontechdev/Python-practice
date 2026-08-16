# **Task description**
# Prompts the user for mass as an integer in kilograms ($m$)
# and calculates the equivalent energy ($E$) in Joules using 
# Einstein's formula $E = mc^2$ ($c = 300,000,000\text{ m/s}$).


def main():
    #Prompt users for mass as an integer (in kilograms)
    mass = int(input('m: '))
    #Print equivalent number of Joules as an integer
    result = einstein(mass)
    print(f'E: {result}')

def einstein(mass):
    # E = mc^2
    return mass * 300000000 ** 2

main()

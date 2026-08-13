
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

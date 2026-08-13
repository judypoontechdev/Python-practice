def main():
    # prompt user to input maths formula
    formula = input('Pls provide maths formula: ').split()
    x = int(formula[0])
    y = formula[1]
    z = int(formula[2])
    calculate(x, y, z)

def calculate(x, y, z):
    # Check which operator y is, then perform the corresponding math operation and output as float
    match y:
        case '+':
            print(float(x) + float(z))
        case '-':
            print(float(x) - float(z))
        case '*':
            print(float(x) * float(z))
        case '/':
            print(float(x) / float(z))

main()

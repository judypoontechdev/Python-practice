# **Task description**
# Prompts the user for a fraction `X/Y` and calculates the fuel level percentage 
# rounded to the nearest integer, outputting `E` for 1% or less, `F` for 99% or 
# more, and reprompting on invalid inputs or exceptions (`ValueError`, `ZeroDivisionError`).

def main():
    while True:
        try:
            # Prompt user for fraction input and split it by the slash
            amount = input('Fraction: ')
            amounts = amount.split('/')

            # Convert string inputs into a list of integers
            z = [int(a) for a in amounts]

            # Test division to catch ZeroDivisionError if denominator is 0
            z[0] / z[1]

        except ValueError:
            # Catch invalid integer conversions (e.g. letters or decimals)
            print('Your input is not an integer')

        except ZeroDivisionError:
                # Catch division by zero errors
                print('y cannot be 0')

        else:
            # Validate business rules: X >= 0, Y > 0, and X <= Y
            if z[0] >= 0 and z[1] > 0 and z[0] <= z[1]:
                break
            else:
                print('Invalid numbers according to requirement.  Try again!')

    # Calculate percentage and round to the nearest integer
    output = (z[0] / z[1]) * 100

    judge(round(output))

def judge(output):
     # Evaluate percentage and print corresponding fuel level message
     if output <= 1:
          print('E')
     elif output >= 99:
        print('F')
     else:
        print(f'{output}%')

main()






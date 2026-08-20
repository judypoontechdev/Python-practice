def main():
    while True:
        try:
            # Prompt user for fraction input and split it by the slash
            fraction = input('Fraction: ')
            percentage = convert(fraction)
        except ValueError:
            print('Invalid numbers according to requirement. Try again!')
        except ZeroDivisionError:
            print('y cannot be 0')
        else:
            print(gauge(percentage))
            break

def convert(fraction):

    if '/' not in fraction:
        raise ValueError

    fractions = fraction.split('/')

    if len(fractions) != 2:
        raise ValueError

    # Convert string inputs into a list of integers
    z = [int(f) for f in fractions]

    # Validate business rules: X >= 0, Y > 0, and X <=
    if z[1] == 0:
        raise ZeroDivisionError

    if z[0] < 0 or z[1] < 0 or z[0] > z[1]:
        raise ValueError

    percentage = round((z[0] / z[1]) * 100)

    return percentage

def gauge(percentage):
     # Evaluate percentage and print corresponding fuel level message
     if percentage <= 1:
          return 'E'
     elif percentage >= 99:
        return 'F'
     else:
        return f'{percentage}%'

if __name__ == '__main__':
    main()
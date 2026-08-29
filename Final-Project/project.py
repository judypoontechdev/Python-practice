import os
import csv
import argparse

def main():
    output()

def user_input():

    total = get_previous_total()

    # Use argsparse to allow user to define Income, expense, and source
    parser = argparse.ArgumentParser(
        description='Pls enter your income and expense along with the source',
        epilog='Example: -- income 30 --source stock or -i 30 -s stock'
    )

    # Define --income -i flag
    parser.add_argument('-i', '--income', default=0)

    # Define --expense -e flag
    parser.add_argument('-e', '--expense', default=0)

    # Define --source -s flag
    parser.add_argument('-s', '--source', nargs='+', default='Unspecified')

    # Storing all values in output object
    output = parser.parse_args()

    # Income
    income = validate_float(output.income)
    total += income

    # Expense
    expense = validate_float(output.expense)
    total -= float(expense)

    # Source
    s = output.source
    source = ' '.join(s)
    if validate_string(s):
        pass

    return {"Income": income, "Expense": expense, "Source": source, "Total": total}

def validate_float(amount):
    try:
        value = float(amount)

    except ValueError:
        raise ValueError('Pls input integers or floats!')

    else:
        if value < 0:
            raise ValueError('Pls input positive integers!')

    return value

def validate_string(source):
    if not source or not source.strip():
        raise ValueError('Pls input strings for source!')
    return source.strip()

def get_previous_total():
    if not os.path.exists('finance.csv'):
        return 0.0

    with open('finance.csv') as file:
        reader = list(csv.DictReader(file))

        if not reader:
            return 0.0

        return float(reader[-1]["Total"])

def output():

    file_exists = os.path.exists('finance.csv') and os.path.getsize('finance.csv') > 0

    # Use File I/O to open a file and append the Dictionary
    with open('finance.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=["Income", "Expense", "Source", "Total"])

        if not file_exists:
            writer.writeheader()

        writer.writerow(user_input())

if __name__ == '__main__':
    main()

# Render the CSV file (containing pizza types, sizes, and prices) as an ASCII table using tabulate

import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif sys.argv[1][-4:] != '.csv':
        sys.exit('Not a CSV file')

    try:
        with open(sys.argv[1]) as file:
            table = csv.DictReader(file)
            print(tabulate(list(table), headers='keys', tablefmt='grid'))

    except FileNotFoundError:
        sys.exit('File does not exist')

main()
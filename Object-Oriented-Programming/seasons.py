from datetime import date
import sys
import inflect
import re

p = inflect.engine()

def main():
    dob = input('Date of Birth: ')
    print(transfer(dob))

def transfer(dob):

    outcome = re.search(r'[\d][\d][\d][\d]-([\d][\d])-([\d][\d])', dob)

    if not outcome:
        sys.exit('Invalid date format, pls input with YYYY-MM-DD')

    if not 1 <= int(outcome.group(1)) <= 12 or not 1 <= int(outcome.group(2)) <= 31:
        raise ValueError('Pls input valid date')

    birthday = date.fromisoformat(dob)
    today = date.today()
    difference = today - birthday
    minutes = difference.days * 24 * 60

    return f'{p.number_to_words(minutes, andword="").capitalize()} minutes'

if __name__ == '__main__':
    main()
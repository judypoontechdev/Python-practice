# Program: scourgify.py (CS50P)
# Objective: Clean and reformat CSV data by splitting combined name strings.
# Processes input CSV containing "name" ("Last, First") and "house" fields.
# Writes output to a new CSV with restructured headers: "first", "last", and "house".

import sys
import csv

def main():

    # Check whether the user inputs exactly two files and the files can be opened
    if len(sys.argv) < 3:
        sys.exit('Too few command line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command line arguments')

    try:
        students = []

        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)

        with open(sys.argv[2], 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            for student in students:
                writer.writerow({'first': student['name'].split(',')[1].strip(), 'last': student['name'].split(',')[0].strip(), 'house': student['house']})

    except FileNotFoundError:
        sys.exit('File not found')

main()
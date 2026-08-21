"""
lines.py exercise objectives:

1. Accept exactly 1 command-line argument: a path to a Python (.py) file.
2. Exit via sys.exit if args are invalid or file does not exist.
3. Count and output effective Lines of Code (LOC) in the specified file:
   - EXCLUDE: Blank lines (only whitespace)
   - EXCLUDE: Comment lines (lines starting with '#', ignoring leading whitespace)
   - INCLUDE: All actual code lines and docstrings
"""

import sys

def main():

    # Check whether the user has passed in python file and in the correct format
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif sys.argv[1][-3:] != '.py':
        sys.exit('Not a Python file')

    # Check whether the file exists:
    count = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:

                # Strip away the white spaces in the line
                stripped = line.strip()

                # ount valid code lines (excluding blank lines and comments)
                if stripped and not stripped.startswith('#'):
                    count += 1

    except FileNotFoundError:
        sys.exit('File does not exist')

    print(f'{count}')

main()
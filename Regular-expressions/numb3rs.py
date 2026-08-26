"""
Task: Validate IPv4 Addresses Using Regular Expressions
Description: This script validates whether a given string is a legally formatted 
IPv4 address (consisting of four numbers separated by dots, each ranging from 0 to 255 
without invalid leading zeros) using regex pattern matching and loop control flow.
"""

import re

def main():
    print(validate(input('IPv4 Address: ')))

def validate(ip):
    if len(ip.split('.')) != 4:
        return False
    for i in ip.split('.'):
        if not re.search(r"^(0|[1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$", i):
            return False
    return True

if __name__ == '__main__':
    main()

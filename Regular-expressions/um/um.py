# The task requires writing a program that takes a sentence or text input 
# and counts how many times the independent word "um" (case-insensitive) appears.

import re

def main():
    print(count(input("Text: ")))


def count(s):
    text = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(text)

if __name__ == "__main__":
    main()
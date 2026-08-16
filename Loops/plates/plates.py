# **Task description**
# Implements an `is_valid()` function to validate custom license plate 
# strings against specific rules (2–6 characters, starts with two letters, 
# numbers only at the end without a leading '0', and no punctuation/spaces).

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    # No periods, spaces, or punctuation marks are allowed
    for p in plate:
        if not p.isalpha() and not p.isnumeric():
            return False

    # Must have two English alphabets as starting
    if not plate[0].isalpha() and not plate[1].isalpha():
        return False

    # Length MIN 2 MAX 6
    if not 2 <= len(plate) <= 6:
        return False

    # Numbers can't be in between alphabets
    for p in range(len(plate)):
        if plate[p].isnumeric():
            break

    if plate[p] == '0':
        return False

    for q in plate[p + 1:]:
        if q.isalpha():
            return False

    return True

main()
